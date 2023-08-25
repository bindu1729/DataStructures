#exit 0 is process is successfully executed and exit 1 is error
#improve code to throw exception


absolute_path = "/Users/bindugutta/Desktop/Nanduri Algo/student.txt"

with open(absolute_path, "r") as file:
    content = file.read()

absolute_path = "/Users/bindugutta/Desktop/Nanduri Algo/student2.txt"

with open(absolute_path, "w") as file:
    file.write(content)



