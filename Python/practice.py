# Strings
# favorite_word = "String"
# print(favorite_word)
#
# my_name = "Steve"
# first_initial = my_name[0]
# print(first_initial)

# first_name = "Rodrigo"
# last_name = "Villanueva"
# new_account = last_name[:5]
# temp_password = last_name[2:6]
# print(new_account)
# print(temp_password)


# first_name = "Julie"
# last_name = "Blevins"
#
#
# def account_generator(first_name, last_name):
#     account_name = first_name[:3] + last_name[:3]
#     return account_name
#
#
# new_account = account_generator(first_name, last_name)
#
# print(new_account)

# first_name = "Reiko"
# last_name = "Matsuki"
#
#
# def password_generator(first_name, last_name):
#     password = first_name[-3:] + last_name[-3:]
#     return password
#
#
# temp_password = password_generator(first_name, last_name)
# print(temp_password)

# company_motto = "Copeland's Corporate Company helps you capably cope with the constant cacophony of daily life"
# second_to_last = company_motto[-2]
# final_word = company_motto[-4:]
# print(second_to_last)
# print(final_word)

# Strings are immutable
# first_name = "Bob"
# last_name = "Daily"
# # first_name[0] = "R" # This will give an error
# new_first_name = "R" + first_name[1:]
# print(new_first_name)

# Escape characters
# password = "theycallme\"crazy\"91"

# Iterating through strings
# def get_length(string):
#     count = 0
#     for letter in string:
#         count += 1
#     return count
#
#
# print(get_length("test"))

# Strings and conditionals
# def letter_check(word, letter):
#     for character in word:
#         if character == letter:
#             return True
#     return False
#
#
# letter_check("strawberry", "o")

# def contains(big_string, little_string):
#     if little_string in big_string:
#         return True
#     else:
#         return False
#
#
# print(contains("watermelon", "melon"))

# def common_letters(string_one, string_two):
#     common = []
#     for letter in string_one:
#         if letter in string_two and letter not in common:
#             common.append(letter)
#     return common
#
#
# print(common_letters("banana", "cream"))


