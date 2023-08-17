#O(n) time complexity
def factorialhw(n):
    num_array = []
    for i in range(0,n+1):
        num_array.append(i)
    print(num_array)
    fact = 1
    fact_result_array = []
    for j in num_array:
        if j == 0:
            fact_result_array.append(1)
        else:
            fact = fact*j
            fact_result_array.append(fact)
    return fact_result_array


print(factorialhw(5))

#Factorial using dict to get O(n)

fact_dict = {0:1}

#dynamic programming is to create and store in memory table:dict
def better_factorial(n):
    if n in fact_dict:
        return fact_dict[n]
    fact_dict[n] = n*better_factorial(n-1)
    return fact_dict[n]

num = 5
fact_array = []

#for n in range(num+1,-1,-1): - reverse results
for n in range(0,num+1):
    fact_array.append(better_factorial(n))
print(fact_array)


#to get factorials of three numbers
def factorialhw(n):
    num_array_dict = {}
    for i in range(0,n+1):
        num_array_dict[i]
    print(num_array_dict)
    # fact = 1
    # fact_result_array = []
    # for j in num_array:
    #     if j == 0:
    #         fact_result_array.append(1)
    #     else:
    #         fact = fact*j
    #         fact_result_array.append(fact)
    # return fact_result_array


print(factorialhw(5))
print(factorialhw(6))
print(factorialhw(7))

