# a word formed by rearranging the other word.
# example: race,care

word1 = "race"
word2 = "care"
#anagram without repitition
# for c1 in word1:
#     print(c1)
#O(n2)
if len(word1) != len(word1):
    print("Not anagram")
else:
    anagram_found = True
    for c1 in word1:
        c1_found = False
        for c2 in word2:
            if c1 == c2:
                c1_found = True
                break
        if not c1_found:
            anagram_found = False
            break
    if anagram_found:
        print("Anagarams")
    else:
        print("not anagrams")