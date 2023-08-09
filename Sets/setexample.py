string_example = "bbindu"

#with set
print(set(string_example))

#with dict
#search is O(1)
example_dict = {}
for c1 in string_example:
    if c1 not in example_dict:
        example_dict[c1] = True
print(list(example_dict.keys()))

#with arrays
#search is O(n)
example_arr = []
for c1 in string_example:
    if c1 not in example_arr:
        example_arr.append(c1)
print(list(example_dict.keys()))