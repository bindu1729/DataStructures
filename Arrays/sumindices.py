#with less time and more space
# a+b = target  --> target-b=a

# if array elements are not repeated
nums = [5,4,3,7]
target = 7

dict_nums = {}
for index in range(len(nums)):
    dict_nums[nums[index]] = index  # {5:0,....}
for key in dict_nums:
    if target - key in dict_nums:
        print(dict_nums[key],dict_nums[target-key])
        break



# with two for loops
# nums = [2,7,11,15]
# target = 9
# found = False
# for i in range(len(nums)):
#     for j in range(len(nums)):
#         if i != j and nums[i] + nums[j] == target:
#             print(i,j)
#             found = True
#             break
#     if found:
#         break