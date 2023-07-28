n = int(input("Enter number of rows: "))
for i in range(0,n+1):
    k = n
    for j in range(k,i,-1):
        print(j, end="")
        k -= 1
    print()



# n = int(input("Enter number of rows: "))
# for i in range(n,0,-1):
#     for j in range(i,0,-1):
#         print(j, end="")
#     print()