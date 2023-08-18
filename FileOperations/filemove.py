import os

file_path = "/Users/bindugutta/Desktop/Nanduri Algo/student5.txt"

# with open(file_path, "r") as file:
#     content = file.read()

file_path2 = "/Users/bindugutta/Desktop/CPT/student6.txt"

# with open(file_path2, "w") as file2:
#     file2.write(content)
os.rename(file_path,file_path2)
