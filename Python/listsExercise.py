# names = ['Jenny', 'Alexus', 'Sam', 'Grace']

# dogs_names = ['Elphonse', 'Dr. Doggy DDS', 'Carter', 'Ralph']

# names_and_dogs_names = zip(names, dogs_names)

# list_of_names_and_dogs_names = print(list(names_and_dogs_names))

# empty_list = []

# orders = ['daisies', 'periwinkle']

# print(orders)

# orders.append('tulips')

# orders.append('roses')

# print(orders)

# orders = ['daisy', 'buttercup', 'snapdragon', 'gardenia', 'lily']

# # Create new orders here:
# new_orders = orders + ['lilac', 'iris']

# print(new_orders)

# broken_prices = [5, 3, 4, 5, 4] 
# broken_prices = broken_prices + [10]

# print(broken_prices)

# range_list = range(10)
# print(range_list)
# print(list(range_list))

# list2 = range(0, 40, 5)
# print(list(list2))

# first_names = ['Ainsley', 'Ben', 'Chani','Depak']
# age = []
# age.append(42)
# all_ages = age + [32, 41, 29]
# name_and_age = zip(first_names, all_ages)
# print(list(name_and_age))
# ids = range(4)
# print(list(ids))
# name_and_age = zip(first_names, ids, all_ages)
# print(list(name_and_age))

# list1 = range(2, 20, 2)
# print(list(list1))
# list1_len = print(len(list1))

# employees = ['Michael', 'Dwight', 'Jim', 'Pam', 'Ryan', 'Andy', 'Robert']
# index4 = employees[4]
# print(index4)
# print(len(employees))

# shopping_list = ['eggs', 'butter', 'milk', 'cucumbers', 'juice', 'cereal']
# print(len(shopping_list))
# last_element = shopping_list[-1]
# element5 = shopping_list[5]
# print(element5, last_element)

# suitcase = ['shirt', 'shirt', 'pants', 'pants', 'pajamas', 'books']
# beginning = suitcase[0:4]
# print(beginning)
# middle = suitcase[2:4]
# print(middle)

# suitcase = ['shirt', 'shirt', 'pants', 'pants', 'pajamas', 'books']
# start = suitcase[:3]
# end = suitcase[-2:]
# print(start)
# print(end)

# votes = ['Jake', 'Jake', 'Laurie', 'Laurie', 'Laurie', 'Jake', 'Jake', 'Jake', 'Laurie', 'Cassie', 'Cassie',
# 'Jake', 'Jake', 'Cassie', 'Laurie', 'Cassie', 'Jake', 'Jake', 'Cassie', 'Laurie'] jake_votes = votes.count('Jake')
# print(jake_votes)

# addresses = ['221 B Baker St.', '42 Wallaby Way', '12 Grimmauld Place', '742 Evergreen Terrace', '1600 Pennsylvania
# Ave', '10 Downing St.'] addresses.sort() print(addresses) names = ['Ron', 'Hermione', 'Harry', 'Albus',
# 'Sirius'] names.sort() print(names) cities = ['London', 'Paris', 'Rome', 'Los Angeles', 'New York'] sorted_cities =
# cities.sort() print(sorted_cities) cities.sort() print(cities)

# games = ['Portal', 'Minecraft', 'Pacman', 'Tetris', 'The Sims', 'Pokemon']
# games_sorted = sorted(games)
# print(games_sorted)

# inventory = ['twin bed', 'twin bed', 'headboard', 'queen bed', 'king bed', 'dresser', 'dresser', 'table', 'table',
# 'nightstand', 'nightstand', 'king bed', 'king bed', 'twin bed', 'twin bed', 'sheets', 'sheets', 'pillow',
# 'pillow'] inventory_len = len(inventory) print(inventory_len) first = inventory[0] last = inventory[-1]
# inventory_2_6 = inventory[2:6] first_3 = inventory[:3] print(first_3) twin_beds = inventory.count('twin bed')
# print(twin_beds) inventory.sort() print(inventory)

# Zip Exercise
# names = ["Jenny", "Alexus", "Sam", "Grace"]
# heights = [61, 70, 67, 64]
#
# names_and_heights = zip(names, heights)
# print(names_and_heights)
# print(list(names_and_heights))

# Nested Loops
# sales_data = [[12, 17, 22], [2, 10, 3], [5, 12, 13]]
# scoops_sold = 0
# for location in sales_data:
#     print(location)
#     for i in location:
#         scoops_sold += i
#         print(i)
# print(scoops_sold)

# List Comprehensions
numbers = [2, -1, 79, 33, -45]
doubled = [num * 2 for num in numbers]
print(doubled)

# List Comprehensions with Conditional Logic
heights = [161, 164, 156, 144, 158, 170, 163, 163, 157]

can_ride_coaster = [height for height in heights if height > 161]
print(can_ride_coaster)

single_digits = list(range(10))

squares = []

for digit in single_digits:
    print(digit)
    squares.append(digit ** 2)
print(squares)

cubes = [digit ** 3 for digit in single_digits]
print(cubes)

for i in range(3):
    print(i)

j = 1
while j <= 10:
    print(j)
    j += 1

desired_list = [x - 1 for x in range(5)]
print(desired_list)

drink_choices = ["coffee", "tea", "water", "juice", "soda"]
for drink in drink_choices:
    print(drink)

for i in range(3):
    print(5)
