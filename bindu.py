from flask import Flask,Response,request,render_template,jsonify
from neo4j import GraphDatabase

app=Flask(__name__)

url="bolt://localhost:7687"
usr="neo4j"
pwd="4rfv4rfv"
driver = GraphDatabase.driver(url, auth=("neo4j", "4rfv4rfv"))

#Define the route for the Flask application to retrieve all the films using GET operation
@app.route('/film', methods=['GET'])
def get_film_in_database():
    try:
        query = '''MATCH(fi:Film)<-[:ACTED_IN]-(p:Actor) RETURN fi.title AS title'''
        with driver.session() as session:
            re = session.run(query)
            json_re = []
            #add all the records to json_re list
            for record in re:
                json_re.append(record.data())
            return jsonify(json_re)
    except Exception as ex:
        # Return an error response in case of any exception
        response = Response(f"Error in Operation: {ex}", status=500, mimetype="application/json")
        return response




#Reports
@app.route('/reports', methods=['GET'])
def get_film_report():
    try:
        query = '''MATCH (fi:Film)<-[:ACTED_IN]-(p:Actor)
                     WITH fi, COLLECT(p) AS actors, COUNT(p) AS num_actors
                     RETURN fi.title AS title, num_actors, actors'''
        
        with driver.session() as session:
            re = session.run(query)
            json_re = []

            for record in re:
                film_info = record.data()
                film_info["num_actors"] = film_info.pop("num_actors")  
                film_info["actors"] = [actor["name"] for actor in film_info["actors"]] 
                json_re.append(film_info)

           
            no_of_titles = len(json_re)
            no_of_actors = sum(len(film_info["actors"]) for film_info in json_re)

            report_data = {
                "total_titles": no_of_titles,
                "total_actors": no_of_actors,
                "films": json_re
            }

        
            return jsonify(report_data)

        
    except Exception as ex:
        # Return an error response in case of any exception
        response = Response(f"Error in Operation: {ex}", status=500, mimetype="application/json")
        return response




    
#Define the route to get film information using title including actor
@app.route('/film/<string:fname>', methods=['GET'])
def get_film_name_by_title(fname):
    try:
        query = '''MATCH (fi:Film) WHERE toLower(fi.title) CONTAINS toLower('{}')
                                              optional MATCH (actor:Actor)-[:ACTED_IN]->(fi:Film) RETURN fi,collect(distinct actor.name) as Actor_Names'''
        with driver.session() as session:
            re = session.run(query.format(fname))
            nodes_data = list(re.data())
            json_re = []
            #for all the records in the result,attach actor names aswell
            for each in nodes_data:
                film_node = each['fi']
                film_json = dict(film_node)
                film_json['actor_names'] = list(each['Actor_Names'])
                film_json.pop('list_actors', None)
                json_re.append(film_json)
            if len(json_re) > 0:
                return jsonify(json_re)
            else:
                response = Response(f"None Film title: {fname}", status=400)
                return response
    except Exception as ex:
        # Return an error response in case of any exception
        response = Response(f"Error in Operation: {ex}", status=500, mimetype="application/json")
        return response
    
# Define the route to delete film information using title
@app.route('/film/<string:fname>', methods=['DELETE'])
def delete_film_by_title(fname):
    try:
        query = '''MATCH (fi:Film {title: $filmName})Return fi as ShowInfo'''
        with driver.session() as session:
            re = session.run(query,filmName = fname)
            nodes_data = list(re.data())
            #check if there is a film with the given title
            if len(nodes_data) > 0:
                query = '''MATCH (fi:Film {title: $filmName})
                                DETACH DELETE fi'''
                with driver.session() as session:
                 session.run(query,filmName = fname)
                 response = Response(f"{fname} is Deleted .", status=200, mimetype="application/json")
                return response
            else:
                response = Response(f"No Film named : {fname}.", status=500, mimetype="application/json")
                return response
    except Exception as ex:
        # Return an error response in case of any exception
        response = Response(f"Error in Delete: {ex}", status=500, mimetype="application/json")
        return response

# Define the route to update film information using title and patch operation
@app.route('/film/<string:fname>', methods=['PATCH'])
def update_film_by_title(fname):
    try:
        # Extract data from the JSON request
        data = request.get_json()
        with driver.session() as session:
            query = '''
                    MATCH (film:Film {title: $filmName})
                    SET film.title = $title, film.description = $description, film.rating = $rating
                    RETURN film
                '''

            result = session.run(query, filmName=fname, title=data.get('title'), description=data.get('description'), rating=data.get('rating'))
            #check if the result's top element is present or not
            if result.peek() is not None:
                updated_film = result.single()
                return jsonify(f"{fname} updated successfully",dict(updated_film['film']))
            else:
                return jsonify({'error': 'Film not found'}), 404

    except Exception as ex:
        # Return an error response in case of any exception
        response = Response(f"Error in Update: {ex}", status=500, mimetype="application/json")
        return response

#Define the route to insert film information with post operation
@app.route('/film', methods=['POST'])
def insert_film_with_all_details():
    try:
        data = request.get_json()
        actors_data = data.pop('list_actors', [])
        with driver.session() as session:
            #to auto increment film id when new film is inserted
            result = session.run('''MATCH (film:Film) RETURN count(film) AS count''')
            film_count = result.single()["count"]
            next_film_id = film_count + 1
            #query to create and insert new film data in the database
            query = (
                '''CREATE (fi:Film {film_id: $film_id, title: $title, description: $description, rental_duration: $rental_duration, rental_rate: $rental_rate, length: $length, replacement_cost: $replacement_cost, rating: $rating})'''
            )
            session.run(query, film_id=next_film_id, title=data.get('title'), description=data.get('description'), rental_duration=data.get('rental_duration'), rental_rate=data.get('rental_rate'), length=data.get('length'), replacement_cost=data.get('replacement_cost'), rating=data.get('rating'))

            # Create relationships between the newly inserted film and actors
            for actor_data in actors_data:
                # Merge a new node to attach the list of actors to the inserted new film node and establish the relationship
                session.run('''MERGE (p:Actor {name: $name})''', name=actor_data)
                session.run('''MATCH (p:Actor {name: $actor_name}), (fi:Film {film_id: $film_id}) MERGE (p)-[:ACTED_IN]->(fi)''', actor_name=actor_data, film_id=next_film_id)

            # Display the newly inserted film information along with the success message
            query_to_retrieve = '''MATCH (fi:Film {film_id: $film_id}) Return fi'''
            re = session.run(query_to_retrieve, film_id=next_film_id)
            json_re = []
            for each in re:
                film_node = each['fi']
                film_json = dict(film_node)
                json_re.append(film_json)

            return jsonify({"message": "Film added successfully", "Film": json_re}), 201

    except Exception as ex:
        # Return an error response in case of any exception
        response = Response(f"Error in Insert: {ex}", status=500, mimetype="application/json")
        return response


if __name__ == '__main__':
    app.run(port=5003, debug=True)
