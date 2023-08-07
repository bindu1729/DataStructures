students = [{"name":"bindu","math":99,"science":98,"english":100},
            {"name":"monica","math":100,"science":89,"english":85},
            {"name":"vaishu","math":70,"science":80,"english":50,"social":70}]


for student in students:
    total = 0
    exclude_keys = ['name']
    new_student = {x: student[x] for x in student.keys() if x not in exclude_keys}
    for k, v in new_student.items():
        total += v
    count = len(new_student.keys())
    student["avg"] = total//count
    print(f"avg of {student['name']}:{total//count}")
print(students)