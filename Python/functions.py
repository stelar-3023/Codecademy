# def sing_song():
#   print("You may say I'm a dreamer")
#   print("But I'm not the only one")
#   print("I hope some day you'll join us")
#   print("And the world will be as one")

# # call sing_song() below:
# sing_song()

# def loading_screen():
#     print("This page is loading...")

# loading_screen()
# def mult_two_add_three(number):
#   print(number*2 + 3)

# # Call mult_two_add_three() here:
# mult_two_add_three(5)

# def mult_x_add_y(number, x, y):
#   print(number * x + y)

# mult_x_add_y(5, 2, 3)

# Define create_spreadsheet():
# def create_spreadsheet(title, row_count = 1000):
#   print("Creating a spreadsheet called "+title + " with " + str(row_count) + " rows")

# # Call create_spreadsheet() below with the required arguments:
# create_spreadsheet("Downloads")
# create_spreadsheet(title = "Applications", row_count = 10)

# def calculate_age(current_year, birth_year):
#   age = current_year - birth_year
#   return age
# my_age = calculate_age (2049, 1993)
# dads_age = calculate_age (2049, 1953)
# X = my_age
# Y = dads_age

# print("I am " +str(X) + " years old and my dad is " + str(Y) + " years old")

# def get_boundaries(target, margin):
#     low_limit = target - margin
#     high_limit = margin + target
#     return low_limit, high_limit

# low, high = get_boundaries(100, 20)
# print(low)
# print(high)

# current_year = 2048 # globally defined
# def calculate_age(birth_year):
#     age = current_year - birth_year
#     return age
# print(calculate_age(1974))
# print(current_year)

# def repeat_stuff(stuff, num_repeats = 10):
#     return stuff * num_repeats
# repeat_stuff ("Row", 3)
# lyrics = repeat_stuff("Row ", 3) + "Your Boat. "
# song = repeat_stuff(lyrics)
# print(song)

# def trip_planner(first_destination, second_destination, final_destination="Codecademy HQ"):
#     print("Here is what your trip will look like!")
#     print(
#         "First, we will stop in " + first_destination + ", then " + second_destination + ", and lastly " + final_destination)
#
#
# trip_planner("France", "Germany", "Denmark")

# def calculate_exchange_rate(us_dollars, exchange_rate):
#     return us_dollars * exchange_rate
#
#
# new_zealand_exchange = calculate_exchange_rate(100, 1.4)
#
# print("100 US dollars is " + str(new_zealand_exchange) + " New Zealand dollars")

# current_budget = 3500.75
# shirt_expense = 9
#
#
# def print_remaining_budget(budget):
#     print("Your remaining budget is: $" + str(budget))
#
#
# def deduct_expense(budget, expense):
#     return budget - expense
#
#
# new_budget_after_shirt = deduct_expense(current_budget, shirt_expense)
# print_remaining_budget(current_budget)
# print_remaining_budget(new_budget_after_shirt)

# def top_tourist_locations_italy():
#     first = "Rome"
#     second = "Venice"
#     third = "Florence"
#     return first, second, third
#
#
# most_popular1, most_popular2, most_popular3 = top_tourist_locations_italy()
# print(most_popular1)
# print(most_popular2)
# print(most_popular3)

# def trip_planner_welcome(name):
#     print("Welcome to tripplanner v1.0 " + name)
#
#
# trip_planner_welcome("steve")
#
#
# def estimated_time_rounded(estimated_time):
#     rounded_time = round(estimated_time)
#     return rounded_time
#
#
# estimate = estimated_time_rounded(3.4)
#
#
# def destination_setup(origin, destination, estimated_time, mode_of_transport="Car"):
#     print("Your trip starts off in " + origin)
#     print("And you are traveling to " + destination)
#     print("You will be traveling by " + mode_of_transport)
#     print("It will take approximately " + str(estimated_time) + " hours")
#
#
# destination_setup("New York", "Los Angeles", estimate, "Car")

# time = "3pm"
# mood = "good"
#
#
# def report():
#     print("The current time is " + time)
#     print("The mood is " + mood)
#
#
# print("Beginning of report")
#
# report()


# def large_power(base, exponent):
#     result = base ** exponent
#     if result > 5000:
#         return True
#     else:
#         return False

# def twice_as_large(num1, num2):
#     if num1 > num2 * 2:
#         return True
#     else:
#         return False

# def divisible_by_ten(num):
#     if num % 10 == 0:
#         return True
#     else:
#         return False
