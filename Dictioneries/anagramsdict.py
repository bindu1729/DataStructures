word1 = "a"
word2 = "ab"

word1_dict = {}
word2_dict = {}

#O(n)

if len(word1) != len(word2):
    print("Not anagram")
else:

    for c1 in word1:
        if c1 not in word1_dict:
            word1_dict[c1] = 1
        else:
            word1_dict[c1] += 1
    print(word1_dict)
    for c2 in word2:
        if c2 not in word2_dict:
            word2_dict[c2] = 1
        else:
            word2_dict[c2] += 1
    print(word2_dict)

    anagram_found = True
    for key1  in word1_dict:
        if key1 not in word2_dict:
            anagram_found = False
            break
        else:
            if word1_dict[key1] != word2_dict[key1]:
                anagram_found = False
                break

    if anagram_found:
        print("Anagram found")
    else:
        print("Not anagram")