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

# .strip() method
love_maybe_lines = ['Always    ', '     in the middle of our bloodiest battles  ', 'you lay down your arms',
                    '           like flowering mines    ', '\n', '   to conquer me home.    ']
love_maybe_lines_stripped = []
for line in love_maybe_lines:
    love_maybe_lines_stripped.append(line.strip())
    love_maybe_full = "\n".join(love_maybe_lines_stripped)
print(love_maybe_lines_stripped)
print(love_maybe_full)


# .replace() method
toomer_bio = \
"""
Nathan Pinchback Tomer, who adopted the name Jean Tomer early in his literary career, was born in Washington, D.C. in 1894. Jean is the son of Nathan Tomer was a mixed-race freedman, born into slavery in 1839 in Chatham County, North Carolina. Jean Tomer is most well known for his first book Cane, which vividly portrays the life of African-Americans in southern farmlands.
"""
toomer_bio_fixed = toomer_bio.replace("Tomer", "Toomer")

# .find() method
god_wills_it_line_one = "The very earth will disown you"
disown_placement = god_wills_it_line_one.find("disown")
print(disown_placement)

# .format() method
def poem_title_card(title, poet):
    print("The poem \"{}\" is written by {}.".format(title, poet))

poem_title_card("I Hear America Singing", "Walt Whitman")

# .format() method with multiple arguments
def poem_description(publishing_date, author, title, original_work):
    poem_desc = "The poem {title} by {author} was originally published in {original_work} in {publishing_date}.".format(publishing_date=publishing_date, author=author, title=title, original_work=original_work)
    return poem_desc

my_beard_description = poem_description("1974", "Shel Silverstein", "My Beard", "Where the Sidewalk Ends")

# Preserve the Verse
highlighted_poems = "Afterimages:Audre Lorde:1997,  The Shadow:William Carlos Williams:1915, Ecstasy:Gabriela Mistral:1925,   Georgia Dusk:Jean Toomer:1923,   Parting Before Daybreak:An Qi:2014, The Untold Want:Walt Whitman:1871, Mr. Grumpledump's Song:Shel Silverstein:2004, Angel Sound Mexico City:Carmen Boullosa:2013, In Love:Kamala Suraiyya:1965, Dream Variations:Langston Hughes:1994, Dreamwood:Adrienne Rich:1987"

print(highlighted_poems)

highlighted_poems_list = highlighted_poems.split(",")

print(highlighted_poems_list)

highlighted_poems_stripped = []

for poem in highlighted_poems_list:
    highlighted_poems_stripped.append(poem.strip())
print(highlighted_poems_stripped)

highlighted_poems_details = []

for poem in highlighted_poems_stripped:
    highlighted_poems_details.append(poem.split(":"))
print(highlighted_poems_details)

titles = []
poets = []
dates = []

for poem in highlighted_poems_details:
    titles.append(poem[0])
    poets.append(poem[1])
    dates.append(poem[2])
    
for i in range(len(titles)):
    print("The poem {} was published by {} in {}".format(titles[i], poets[i], dates[i]))

