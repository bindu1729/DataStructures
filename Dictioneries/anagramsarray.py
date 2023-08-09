word1 = "race"
word2 = "care"

#O(n2)
# found = False
# if len(word1) != len(word2):
#     print("not anagram")
# else:
#     for elem in range(0, len(word1)):
#         if word1[elem] in word2 and word2[elem] in word1:
#             for char in range(0, len(word2)):
#                 if word1.count(word1[elem]) == word2.count(word2[char]):
#                     found = True
#         else:
#             found = False
#             break
#     if found:
#         print("anagram")
#     else:
#         print("not anagram")



#convert word to small letter
result_arr1 = [0]*26
#print(result_arr)
result_arr2 = [0]*26
#print(ord('a'))

for c1 in word1:
    index = ord(c1)-ord('a')
    #print(index)
    result_arr1[index] += 1
#print(result_arr1)
for c2 in word2:
    index2 = ord(c2)-ord('a')
    result_arr2[index2] += 1

found = True
for index in range(0,len(result_arr1)-1):
    if result_arr1[index] != result_arr2[index]:
        found = False
if found:
    print("anagram")
else:
    print("not anagram")