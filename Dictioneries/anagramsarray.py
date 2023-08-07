word1 = "race"
word2 = "care"

found = False
if len(word1) != len(word2):
    print("not anagram")
else:
    for elem in range(0, len(word1)):
        if word1[elem] in word2 and word2[elem] in word1:
            for char in range(0, len(word2)):
                if word1.count(word1[elem]) == word2.count(word2[char]):
                    found = True
        else:
            found = False
            break
    if found:
        print("anagram")
    else:
        print("not anagram")
