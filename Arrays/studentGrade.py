# You are tasked with building a student grades tracker. Create an array to store the grades of a class for a particular subject and implement functions to perform basic operations.
# Create an array to store the grades of five students in a subject.
# Calculate the average marks of the class
# find and return the highest grade obtained in the class.
# find and return the lowest grade obtained in the class.
# count and return the number of passing grades
# count and return the number of failing


grades = [35,70,48,98,23]

total = 0
for grade in grades:
    total += grade
print(f"total is  {total}")

avg_grade = int(total/len(grades))
print(f"avg is  {avg_grade}")

highest = grades[0]
for grade in grades:
    if highest < grade:
        highest = grade

print(f"highest grade is  {highest}")

lowest = grades[0]
for grade in grades:
    if lowest > grade:
        lowest = grade

print(f"highest grade is  {lowest}")


count_pass = 0
count_fail = 0
for grade in grades:
    if grade >= 35:
        count_pass += 1
    else:
        count_fail += 1
print(f"count is  {count_pass} and {count_fail}")

count_fail = 0
for grade in grades:
    if grade < 35:
        count_fail += 1
count_pass = len(grades)-count_fail
print(f"count is  {count_pass} and {count_fail}")



