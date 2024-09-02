# The map() function applies a given function to each item of an iterable (such as a list) and returns a list of the results. The syntax for map() is as follows:

# map(function, iterable)
# The function argument is the function that will be applied to each item of the iterable, and the iterable argument is the list or other iterable that you want to apply the function to. Here is an example of using map() to convert a list of strings to uppercase:

names = ["alice", "bob", "charlie"]
upper_names = list(map(str.upper, names))
print(upper_names)  # Output: ['ALICE', 'BOB', 'CHARLIE']
# In this example, the str.upper function is applied to each item in the names list to convert them to uppercase. The result is a new list containing the uppercase versions of the original strings.

# Converting strings to integers 

str_nums = ['1', '2', '3', '4', '5'] 

int_nums = list(map(int, str_nums)) 

print(int_nums)  # Output: [1, 2, 3, 4, 5] 
# In this example, the int function is applied to each item in the str_nums list to convert them to integers. The result is a new list containing the integer versions of the original strings.

# Finding the length of strings 

words = ['apple', 'banana', 'cherry'] 

word_lengths = list(map(len, words)) 

print(word_lengths)  # Output: [5, 6, 6] 
# In this example, the len function is applied to each item in the words list to find the length of each string. The result is a new list containing the lengths of the original strings.
