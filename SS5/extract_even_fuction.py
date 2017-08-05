
""" Define a fuction extract all even number in a list"""
def extract_even(input_list):
	return [item for item in input_list if item%2 == 0]


### Test case with Huy béo's list
### Sorry my fuction's name is not:"get_even_list", it's "extract_even"
#even_list = get_even_list([1, 2, 5, -10, 9, 6])
even_list = extract_even([1, 2, 5, -10, 9, 6])

if set(even_list) == set([2, -10, 6]):
    print("Your function is correct")
else:
    print("Ooops, bugs detected")
