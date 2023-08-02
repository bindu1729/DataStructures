grades = [35,70,48,98,23]

last_elem = grades[len(grades)-1]
print(f"last element is {last_elem}")
print(f"last element is {grades[-1]}")

#reversing of array without neg index and without inplace
reverse_grades = []
for index in range(len(grades)-1,-1,-1):
    reverse_grades.append(grades[index])
print(f"Reversed array is {reverse_grades}")

reverse_grades = []
reverse_grades = [grades[x] for x in range(len(grades)-1,-1,-1)]
print(f"Reversed array is {reverse_grades}")

#reversing of array without neg index and with inplace

grades = [35,70,48,98,23]
for index in range(0,len(grades)//2):
    reverse_index = len(grades)-1-index
    temp = grades[index]
    grades[index] = grades[reverse_index]
    grades[reverse_index] = temp

print(f"Reversed array is {grades}")

#reversing of array with last as neg index and with inplace
grades = [35,70,48,98,23]
reverse_index = -1
for index in range(0,len(grades)//2):
    reverse_index -= index
    grades[index],grades[reverse_index] = grades[reverse_index],grades[index]
print(f"Reversed array is {grades}")
