#array of expenses of a week and retrieve useful information

arr = [10,20,30,40,50,60,70]

total = sum(arr)
print(f"max expenses is {max(arr)}")
print(f"min expenses is {min(arr)}")
print(f"total expenses is {total}")
avg_exp = total/len(arr)
print(f"average expenses is {avg_exp}")


