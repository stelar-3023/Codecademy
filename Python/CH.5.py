# favorite_word = 'What'
# print(favorite_word)

# my_name = 'Steve'
# first_initial = my_name[0]
# print(first_initial)

# first_name = "Steve"
# last_name = "Larsen"
# new_account = last_name[:2]
# temp_password = last_name[1:4]
# print(new_account)
# print(temp_password)

# first_name = "Steve"
# last_name = "Larsen"

# def account_generator(first_name, last_name):
#     account_name = first_name[:3] + last_name[:3]
#     return account_name

# new_account = account_generator(first_name, last_name)
# print(new_account)

# first_name = "Steve"
# last_name = "Larsen"

# def password_generator (first_name, last_name):
#     new_password = first_name[-3:] + last_name[-3:]
#     return new_password

# temp_password = password_generator(first_name, last_name)
# print(temp_password)

# company_motto = "Copeland's Corporate Company helps you capably cope with the constant cacophony of daily life"

# second_to_last = company_motto[-2]
# final_word = company_motto[-4:]
# print(second_to_last)
# print(final_word)

# first_name = "Bob"
# last_name = "Daily"
# fixed_first_name = str("R") + first_name[1:]
# print(fixed_first_name)

# def get_length(word):
#   counter = 0
#   for letter in word:
#       counter += 1
#   return len(word)
# print(get_length('Steve'))

# def letter_check(word, letter):
#     for character in word:
#         if character == letter:
#             return True
#     return False
# print(letter_check("strawberry", "a"))

# def contains(big_string, little_string):
#   return little_string in big_string

# def common_letters(string_one, string_two):
#   common = []
#   for letter in string_one:
#     if (letter in string_two) and not (letter in common):
#       common.append(letter)
#   return common

# def username_generator(first_name, last_name):
#     username = first_name[:3] + last_name[:4]
#     return username
#     if len(first_name <= 3) or len(last_name <=3):
#         return (first_name, last_name)
# print(username_generator('Steve', 'Larsen'))
# def password_generator(username):
#     password = ''
#     for letter in range(0, len(username)):
#         password += username[letter - 1]
#     return password
# print(password_generator('SteLars'))

# STRING METHODS
# poem_title = "spring storm"
# poem_author = "William Carlos Williams"
# poem_title_fixed = poem_title.title()
# print(poem_title_fixed)
# poem_author_fixed = poem_author.upper()
# print(poem_author_fixed)

# line_one = "The sky has given over"

# line_one_words = line_one.split()
# print(line_one_words)

# authors = "Audre Lorde,Gabriela Mistral,Jean Toomer,An Qi,Walt Whitman,Shel Silverstein,Carmen Boullosa,
# Kamala Suraiyya,Langston Hughes,Adrienne Rich,Nikki Giovanni"

# author_names = authors.split(',')
# print(author_names)

# author_last_names = []
# for name in author_names:
#     author_last_names.append(name.split()[-1])
# print(author_last_names)

# spring_storm_text = \
# """The sky has given over 
# its bitterness. 
# Out of the dark change 
# all day long 
# rain falls and falls 
# as if it would never end. 
# Still the snow keeps 
# its hold on the ground. 
# But water, water 
# from a thousand runnels! 
# It collects swiftly, 
# dappled with black 
# cuts a way for itself 
# through green ice in the gutters. 
# Drop after drop it falls 
# from the withered grass-stems 
# of the overhanging embankment."""

# spring_storm_lines = spring_storm_text.split('\n')
# print(spring_storm_lines)

# reapers_line_one_words = ["Black", "reapers", "with", "the", "sound", "of", "steel", "on", "stones"]

# reapers_line_one = ' '.join(reapers_line_one_words)
# print(reapers_line_one)

# winter_trees_lines = ['All the complicated details', 'of the attiring and', 'the disattiring are completed!',
# 'A liquid moon', 'moves gently among', 'the long branches.', 'Thus having prepared their buds', 'against a sure
# winter', 'the wise trees', 'stand sleeping in the cold.']

# winter_trees_full = '\n'.join(winter_trees_lines)
# print(winter_trees_full)

# love_maybe_lines = ['Always    ', '     in the middle of our bloodiest battles  ', 'you lay down your arms',
# '           like flowering mines    ','\n' ,'   to conquer me home.    '] love_maybe_lines_stripped = [] for line
# in love_maybe_lines: love_maybe_lines_stripped.append(line.strip()) print(love_maybe_lines_stripped)
# love_maybe_full = '\n'.join(love_maybe_lines_stripped) print(love_maybe_full)

# toomer_bio = \ """ Nathan Pinchback Tomer, who adopted the name Jean Tomer early in his literary career,
# was born in Washington, D.C. in 1894. Jean is the son of Nathan Tomer was a mixed-race freedman, born into slavery
# in 1839 in Chatham County, North Carolina. Jean Tomer is most well known for his first book Cane, which vividly
# portrays the life of African-Americans in southern farmlands. """ toomer_bio_fixed = toomer_bio.replace('Tomer',
# 'Toomer') print(toomer_bio_fixed)

# god_wills_it_line_one = "The very earth will disown you"

# disown_placement = god_wills_it_line_one.find('disown')
# print(disown_placement)

# def poem_title_card(poet, title):
#     poem_desc = 'The poem \"{}\" is written by {}.'.format(title, poet)
#     return poem_desc
# print(poem_title_card('Walt Whitman', 'I Hear America Singing'))

# def poem_description(publishing_date, author, title, original_work): poem_desc = "The poem {title} by {author} was
# originally published in {original_work} in {publishing_date}.".format(publishing_date = publishing_date,
# author = author, title = title, original_work = original_work) return poem_desc

# author = "Shel Silverstein"
# title = "My Beard"
# original_work = "Where the Sidewalk Ends"
# publishing_date = "1974"

# my_beard_description = poem_description(publishing_date, author, title, original_work)

# print(my_beard_description)

highlighted_poems = "Afterimages:Audre Lorde:1997,  The Shadow:William Carlos Williams:1915, Ecstasy:Gabriela " \
                    "Mistral:1925,   Georgia Dusk:Jean Toomer:1923,   Parting Before Daybreak:An Qi:2014, The Untold " \
                    "Want:Walt Whitman:1871, Mr. Grumpledump's Song:Shel Silverstein:2004, Angel Sound Mexico " \
                    "City:Carmen Boullosa:2013, In Love:Kamala Suraiyya:1965, Dream Variations:Langston Hughes:1994, " \
                    "Dreamwood:Adrienne Rich:1987 "


print(highlighted_poems)

# highlighted_poems_list = highlighted_poems.split(',')
# print(highlighted_poems_list)

# highlighted_poems_stripped = []
# for poem in highlighted_poems_list:
#     highlighted_poems_stripped.append(poem.strip())
#     print(highlighted_poems_stripped)

# highlighted_poems_details = []
# for poem in highlighted_poems_stripped:
#     highlighted_poems_details.append(poem.split(':'))
#     print(highlighted_poems_details)

# titles = []
# poets = []
# dates = []
# for poem in highlighted_poems_details:
#     titles.append(poem[0])
#     poets.append(poem[1])
#     dates.append(poem[2])

# for i in range(0, len(highlighted_poems_details)):
#     print('The poem {} was published by {} in {}'.format(titles[i], poets[i], dates[i]))

# dirty_harry = "Go ahead, make my day."
# split_hairs = dirty_harry.split("a")
# print(split_hairs)


# to see all objects and functions in a module
# import datetime
# print(dir(datetime))

# from datetime import datetime
# current_time = datetime.now()
# print(current_time)

# Import random below:
# import random

# Create random_list below:
# random_list = []
# random_list.append(random.randint(1, 101))
# random_list = [random.randint(1, 101) for i in range(101)]
# print(random_list)

# Create randomer_number below:
# randomer_number = random.choice(random_list)

# Print randomer_number below:
# print(randomer_number)

# from matplotlib import pyplot as plt
# import random

# numbers_a = range(1, 13)
# numbers_b = random.sample(range(1000), 12)

# plt.plot(numbers_a, numbers_b)
# plt.show()

# Import Decimal below:
# from decimal import Decimal

# Fix the floating point math below:
# two_decimal_points = Decimal('0.2') + Decimal('0.69')
# print(two_decimal_points)

# four_decimal_points = Decimal('0.53') * Decimal('0.65')
# print(four_decimal_points)

# parsing date using strptime
# from datetime import datetime
# parsed_date = datetime.strptime('Jan 15, 2018', '%b %d, %Y')
# print(parsed_date.day)
# print(parsed_date.year)

# date_string = datetime.strftime(datetime.now(), '%b %d, %Y')
# print(date_string)


# Creating Dictionaries
# translations = {'mountain': 'orod', 'bread':'bass', 'friend':'mellon', 'horse':'roch'}
# print(translations)

# animals_in_zoo = {}
# animals_in_zoo['zebras'] = 8
# animals_in_zoo['monkeys'] = 12
# animals_in_zoo['dinosaurs'] = 0
# print(animals_in_zoo)

# user_ids = {"teraCoder": 9018293, "proProgrammer": 119238}
# user_ids.update({"theLooper": 138475, "stringQueen": 85739})
# print(user_ids)

# oscar_winners = {"Best Picture": "La La Land", "Best Actor": "Casey Affleck", "Best Actress": "Emma Stone",
# "Animated Feature": "Zootopia"} oscar_winners.update({"Supporting Actress": "Viola Davis"}) oscar_winners["Best
# Picture"] = "Moonlight" print(oscar_winners)

# drinks = ["espresso", "chai", "decaf", "drip"]
# caffeine = [64, 40, 0, 120]
# zipped_drinks = zip(drinks, caffeine)
# drinks_to_caffeine = {key:value for key, value in zip(drinks, caffeine)}
# print(drinks_to_caffeine)

# songs = ["Like a Rolling Stone", "Satisfaction", "Imagine", "What's Going On", "Respect", "Good Vibrations"]
# playcounts = [78, 29, 44, 21, 89, 5]
# plays = {song:playcount for song, playcount in zip(songs, playcounts)}
# # print(plays)
# plays["Purple Haze"] = 1
# print(plays)
# library = {"The Best Songs": plays, "Sunday Feelings": {}}
# print(library)

# Using Dictionaries zodiac_elements = {"water": ["Cancer", "Scorpio", "Pisces"], "fire": ["Aries", "Leo",
# "Sagittarius"], "earth": ["Taurus", "Virgo", "Capricorn"], "air":["Gemini", "Libra", "Aquarius"]} key_to_check =
# 'energy' if key_to_check in zodiac_elements: print(zodiac_elements['energy']) else: print('Not a Zodiac element')
# print(zodiac_elements['earth']) print(zodiac_elements['fire'])

# try / except
# caffeine_level = {"espresso": 64, "chai": 40, "decaf": 0, "drip": 120}
# key_to_check = 'matcha'
# try:
#     print(caffeine_level[key_to_check])
# except KeyError:
#     print('Unknown Caffeine Level')

# get a key user_ids = {"teraCoder": 100019, "pythonGuy": 182921, "samTheJavaMaam": 123112, "lyleLoop": 102931,
# "keysmithKeith": 129384}

# tc_id = user_ids.get('teraCoder', 1000000)
# print(tc_id)

# stack_id = user_ids.get('superStackSmash', 100000)
# print(stack_id)

# delete a key available_items = {"health potion": 10, "cake of the cure": 5, "green elixir": 20, "strength
# sandwich": 25, "stamina grains": 15, "power stew": 30} health_points = 20

# health_points += available_items.pop('stamina grains', 0)
# print(health_points)
# print(available_items)

# health_points += available_items.pop('power stew', 0)
# print(health_points)
# print(available_items)

# health_points += available_items.pop('mystic bread', 0)
# print(health_points)
# print(available_items)

# get all keys user_ids = {"teraCoder": 100019, "pythonGuy": 182921, "samTheJavaMaam": 123112, "lyleLoop": 102931,
# "keysmithKeith": 129384}

# num_exercises = {"functions": 10, "syntax": 13, "control flow": 15, "loops": 22, "lists": 19, "classes": 18,
# "dictionaries": 18}

# users = user_ids.keys()
# print(users)
# lessons = num_exercises.keys()
# print(lessons)

# get all values num_exercises = {"functions": 10, "syntax": 13, "control flow": 15, "loops": 22, "lists": 19,
# "classes": 18, "dictionaries": 18} total_exercises = 0 for exercises in num_exercises.values(): total_exercises +=
# exercises print(total_exercises)

# get all items pct_women_in_occupation = {"CEO": 28, "Engineering Manager": 9, "Pharmacist": 58, "Physician": 40,
# "Lawyer": 37, "Aerospace Engineer": 9}

# for key, value in pct_women_in_occupation.items():
#     print('Women make up ' + str(value) + ' percent of ' + str(key) + 's')

# Review Dictionaries tarot = { 1:	"The Magician", 2:	"The High Priestess", 3:	"The Empress", 4:	"The Emperor",
# 5:	"The Hierophant", 6:	"The Lovers", 7:	"The Chariot", 8:	"Strength", 9:	"The Hermit", 10:	"Wheel of
# Fortune", 11:	"Justice", 12:	"The Hanged Man", 13:	"Death", 14:	"Temperance", 15:	"The Devil",
# 16:	"The Tower", 17:	"The Star", 18:	"The Moon", 19:	"The Sun", 20:	"Judgement", 21:	"The World",
# 22: "The Fool"} spread = {} spread["past"] = tarot.pop(13) spread["present"] = tarot.pop(22) spread["future"] =
# tarot.pop(10) print(spread)

# for key, value in spread.items():
#     print('Your ' + str(key) + ' is the ' + str(value) + ' card.')

# print(type(5))

# my_dict = {}
# print(type(my_dict))

# my_list = []
# print(type(my_list))

# Classes


# class Facade:
#     pass
# facade_1 = Facade()
# facade_1_type = type(facade_1)
# print(facade_1_type)   

# class Rules:
#     pass
#     def washing_brushes(self):
#         return 'Point bristles towards the basin while washing your brushes.'

# class Circle:
#     pi = 3.14
#     def area(self, radius):
#         return Circle.pi * radius ** 2
# circle = Circle()
# pizza_area = circle.area(12 / 2)
# teaching_table_area = circle.area(36 / 2)
# round_room_area = circle.area(11460 / 2)
# print(pizza_area)

# class Circle:
#     pi = 3.14
#     def __init__(self, diameter):
#         print('New circle with diameter: {diameter}'.format(diameter=diameter))
# teaching_table = Circle(36)

# class Store:
#     pass
# alternative_rocks = Store()
# isabelles_ices = Store()
# alternative_rocks.store_name = 'Alternative Rocks'
# isabelles_ices.store_name = "Isabelle's Ices" 
# store_names = "{}, {}".format(alternative_rocks.store_name, isabelles_ices.store_name)
# print(store_names)

# how_many_s = [{'s': False}, "sassafrass", 18, ["a", "c", "s", "d", "s"]]
# for element in how_many_s:
#     if hasattr(element, 'count'):
#      print(element.count('s'))

class Circle:
    pi = 3.14

    def __init__(self, diameter):
        print("Creating circle with diameter {d}".format(d=diameter))
        # Add assignment for self.radius here:
        self.radius = diameter / 2

    def circumference(self):
        return 2 * self.pi * self.radius

    def __repr__(self):
        return 'Circle with radius {radius}'.format(radius=self.radius)


medium_pizza = Circle(12)
teaching_table = Circle(36)
round_room = Circle(11460)

print(medium_pizza.circumference())
print(teaching_table.circumference())
print(round_room.circumference())

print(medium_pizza)
print(teaching_table)
print(round_room)

# print(dir(5))
# def this_function_is_an_object(self):
#     print(dir(this_function_is_an_object))
