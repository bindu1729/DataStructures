abc_str = 'abc'
for i in range(0,len(abc_str)):
    print(i,abc_str[i])

abc_str = ['abc','def']
for i in range(0,len(abc_str)):
    print(i,abc_str[i])

print("Two dimensional array")

twod_arr = [[1,2,3],[4,5,6],[7,8,9],[10,11]]
print(twod_arr[0][0])

for elem_arr in twod_arr:
    print(elem_arr)
    for elem in elem_arr:
        print(elem)

print("two d array indexes")

for index_1 in range(0,len(twod_arr)):
    for index_2 in range(0,len(twod_arr[index_1])):
        print(twod_arr[index_1][index_2])

print("Array manipulation")
arr = [1,2,3,4,5]

#other lang
temp = []
s = 2
for i in range(s,len(arr)):
    temp.append(arr[i])
print(temp)

#in python
print(arr[s:])