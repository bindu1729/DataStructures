arr = [1,2,3,4]
print(arr[0])
print(arr) #python

#in other langs use loops to access

for elem in arr:
    print(elem)

print("using indexes")
for i in range(0,len(arr)):
    print(i,arr[i])

#two ways to add element to array
arr += [9]
arr.append(10)
print(arr)