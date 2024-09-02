# dog_breeds = ['french_bulldog', 'dalmatian', 'shihtzu', 'poodle', 'collie']
# for breed in dog_breeds:
#     print(breed)

# sport_games = ['football', 'football - American', 'hockey', 'baseball', 'cricket']
# for sport in sport_games:
#     print(sport)

# promise = "I will not chew gum in class"
# for i in range(5):
#   print(promise)

# students_period_A = ["Alex", "Briana", "Cheri", "Daniele"]
# students_period_B = ["Dora", "Minerva", "Alexa", "Obie"]
# for student in students_period_A:
#     students_period_B.append(student)
# print(students_period_B) 

# dog_breeds_available_for_adoption = ['french_bulldog', 'dalmation', 'shihtzu', 'poodle', 'collie']
# dog_breed_I_want = 'dalmation'  
# for dog in dog_breeds_available_for_adoption:
#     print(dog)
#     if dog == dog_breed_I_want:
#         print("They have the dog that I want!")
#         break

# ages = [12, 38, 34, 26, 21, 19, 67, 41, 17]
# for i  in ages:
#     if i < 21:
#         continue
#     print(i)

# all_students = ["Alex", "Briana", "Cheri", "Daniele", "Dora", "Minerva", "Alexa", "Obie", "Arius", "Loki"]
# students_in_poetry = []
# while len(students_in_poetry) < 6:
#     student = all_students.pop()
#     students_in_poetry.append(student)
#     print(students_in_poetry)

# sales_data = [[12, 17, 22], [2, 10, 3], [5, 12, 13]]
# scoops_sold = 0
# for location in sales_data:
#     print(location)
#     for element in location:
#         scoops_sold += element
#     print(scoops_sold)

# List Comprehension
# heights = [161, 164, 156, 144, 158, 170, 163, 163, 157]
# can_ride_coaster = [height for height in heights if height > 161]
# print(can_ride_coaster)

# celsius = [0, 10, 15, 32, -5, 27, 3]
# fahrenheit = [temp * 9/5 + 32 for temp in celsius]
# print(fahrenheit)

# single_digits = range(10)
# print(list(single_digits))
# squares = []
# for i in range(10):
#     print(i)
#     squares.append(i ** 2)
#     cubes = [num ** 3 for num in single_digits]
#     print(squares)
#     print(cubes)

