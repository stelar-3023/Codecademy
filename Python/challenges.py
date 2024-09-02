# Create a function named in_range() that has three parameters named num, lower, and upper. The function should return True if num is greater than or equal to lower and less than or equal to upper. Otherwise, return False.

# Write your function here
def in_range(num, lower, upper):
  if num >= lower and num <= upper:
    return True
  else:
    return False

# Create a function named same_name() that has two parameters named your_name and my_name. If our names are identical, return True. Otherwise, return False.
def same_name(your_name, my_name):
  if (your_name == my_name):
    return True
  else:
    return False

# Create a function named always_false() that has one parameter named num. Using an if statement, your variable num, return False.
def always_false(num):
  if (num > 0 and num < 0):
    return True
  else:
    return False
  
# Create a function named movie_review() that has one parameter named rating. If rating is less than or equal to 5, return "Avoid at all costs!". If rating is between 5 and 9, return "This one was fun.". If rating is 9 or above, return "Outstanding!"
def movie_review(rating):
  if(rating <= 5):
    return "Avoid at all costs!"
  if(rating < 9):
    return "This one was fun."
  return "Outstanding!"

# Create a function named max_num() that has three parameters named num1, num2, and num3. The function should return the largest of these three numbers. If any of two numbers tie as the largest, you should return "It's a tie!".
def max_num(num1, num2, num3):
  if num1 > num2 and num1 > num3:
    return num1
  elif num2 > num1 and num2 > num3:
    return num2
  elif num3 > num1 and num3 > num2:
    return num3
  else:
    return "It's a tie!"
  
# Create a function called append_size that has one parameter named lst. The function should append the size of lst (inclusive) to the end of lst. The function should then return this new list.
def append_size(lst):
  lst.append(len(lst))
  return lst

# print(append_size([23, 42, 108]))

# Create a function called append_sum that has one parameter — a list named lst. The function should add the last two elements of lst together and append the result to lst. It should do this process three times and then return lst.
def append_sum(lst):
  for i in range(3):
    lst.append(lst[-1] + lst[-2])
  return lst

# print(append_sum([1, 1, 2]))

# Create a function named larger_list that has two parameters named lst1 and lst2. The function should return the last element of the list that contains more elements. If both lists are the same size, then return the last element of lst1.
def larger_list(lst1, lst2):
  if len(lst1) >= len(lst2):
    return lst1[-1]
  else:
    return lst2[-1]
  
# print(larger_list([4, 10, 2, 5], [-10, 2, 5, 10]))

# Create a function named more_than_n that has three parameters named lst, item, and n. The function should return True if item appears in the list more than n times. The function should return False otherwise.
def more_than_n(lst, item, n):
  if lst.count(item) > n:
    return True
  else:
    return False
  
# print(more_than_n([2, 4, 6, 2, 3, 2, 1, 2], 2, 3))

# Create a function named combine_sort that has two parameters named lst1 and lst2. The function should combine these two lists into one new list and sort the result. Return the new sorted list.
def combine_sort(lst1, lst2):
  new_list = lst1 + lst2
  return sorted(new_list)

# print(combine_sort([4, 10, 2, 5], [-10, 2, 5, 10]))

# Create a function named divisible_by_ten() that takes a list of numbers named nums as a parameter. Return the count of how many numbers in the list are divisible by 10.
def divisible_by_ten(nums):
  count = 0
  for num in nums:
    if num % 10 == 0:
      count += 1
  return count

# print(divisible_by_ten([20, 25, 30, 35, 40]))

# Create a function named add_greetings() which takes a list of strings named names as a parameter. In the function, create an empty list that will contain each greeting. Add the string "Hello, " in front of each name in names and append the greeting to the list. Return the new list containing the greetings.
def add_greetings(names):
  greetings = []
  for name in names:
    greetings.append("Hello, " + name)
  return greetings

# print(add_greetings(["Owen", "Max", "Sophie"]))

# Create a function named delete_starting_evens() that has one parameter named lst. The function should remove elements from the front of lst until the front of the list is not even. The function should then return lst.
def delete_starting_evens(lst):
  while (len(lst) > 0 and lst[0] % 2 == 0):
    lst = lst[1:]
  return lst

# print(delete_starting_evens([4, 8, 10, 11, 12, 15]))

# Create a function named odd_indices() that has one parameter named lst. The function should create a new empty list and add every element from lst that has an odd index. The function should then return this new list.
def odd_indices(lst):
  new_lst = []
  for i in range(1, len(lst), 2):
    new_lst.append(lst[i])
  return new_lst

# print(odd_indices([4, 3, 7, 10, 11, -2]))

# Create a function named exponents() that takes two lists as parameters named bases and powers. Return a new list containing every number in bases raised to the power of every number in powers.
def exponents(bases, powers):
  new_lst = []
  for base in bases:
    for power in powers:
      new_lst.append(base ** power)
  return new_lst

# print(exponents([2, 3, 4], [1, 2, 3]))

# Create a function named larger_sum() that takes two lists of numbers as parameters named lst1 and lst2. The function should return the list whose elements sum to the greater number. If the sum of the elements of each list are equal, return lst1.
def larger_sum(lst1, lst2):
  if sum(lst1) >= sum(lst2):
    return lst1
  else:
    return lst2
  
# print(larger_sum([1, 9, 5], [2, 3, 7]))

# Create a function named over_nine_thousand() that takes a list of numbers named lst as a parameter. The function should sum the elements of the list until the sum is greater than 9000. When this happens, the function should return the sum. If the sum of all of the elements is never greater than 9000, the function should return total sum of all the elements. If the list is empty, the function should return 0.
def over_nine_thousand(lst):
  sum = 0
  for num in lst:
    sum += num
    if sum > 9000:
      break
  return sum

# print(over_nine_thousand([8000, 900, 120, 5000]))

# Create a function named max_num() that takes a list of numbers named nums as a parameter. The function should return the largest number in nums
def max_num(nums):
  max = nums[0]
  for num in nums:
    if num > max:
      max = num
  return max

# print(max_num([50, -10, 0, 75, 20]))

# Create a function named same_values() that takes two lists of numbers of equal size as parameters. The function should return a list of the indices where the values were equal in lst1 and lst2.
def same_values(lst1, lst2):
  equal_indices = []
  for i in range(len(lst1)):
    if lst1[i] == lst2[i]:
      equal_indices.append(i)
  return equal_indices

# print(same_values([5, 1, -10, 3, 3], [5, 10, -10, 3, 5]))

# Create a function named reversed_list() that takes two lists of the same size as parameters named lst1 and lst2. The function should return True if lst1 is the same as lst2 reversed. The function should return False otherwise.
def reversed_list(lst1, lst2):
  for i in range(len(lst1)):
    # We get the element at the current index from our first list with lst1[index] and we test it against the last index of the second list minus the current index len(lst2) - 1 – index
    if lst1[i] != lst2[len(lst2) - 1 - i]:
      return False
  return True

# print(reversed_list([1, 2, 3], [3, 2, 1]))

#Write a function named tenth_power() that has one parameter named num.  The function should return num raised to the 10th power.
def tenth_power(num):
  return num ** 10

# print(tenth_power(1))

# Write a function named square_root() that has one parameter named num. The function should return the square root of num.
def square_root(num):
  return num ** 0.5

# print(square_root(16))

# Write a function named win_percentage() that takes two parameters named wins and losses. The function should return the total percentage of games won by a team.
def win_percentage(wins, losses):
  return (wins / (wins + losses)) * 100

# print(win_percentage(5, 5))

# Create a function named average() that has two parameters named num1 and num2. The function should return the average of these two numbers.
def average(num1, num2):
  return (num1 + num2) / 2

# print(average(1, 100))

# Create a function named remainder() that has two parameters named num1 and num2. The function should return the remainder of twice num1 divided by half of num2.
def remainder(num1, num2):
  return (2 * num1) % (num2 / 2)

# print(remainder(15, 14))

# Create a function named first_three_multiples() that takes an integer named num. The function should return a list of the first three multiples of num in ascending order. Then it should return the 3rd multiple. For example, first_three_multiples(7) should return [7, 14, 21] and 21.
def first_three_multiples(num):
  multiples =  [num, num * 2, num * 3]
  return multiples, multiples[2]

# print(first_three_multiples(7))

# Create a function named tip() that has two parameters named total and percentage. The function should return the amount you should tip given a total and the percentage you want to tip.
def tip(total, percentage):
  return total * (percentage / 100)

# print(tip(10, 25))

# Create a function named introduction() that has two parameters named first_name and last_name. The function should return the last_name, followed by a comma, a space, first_name another space, and finally last_name.
def introduction(first_name, last_name):
  return last_name + ", " + first_name + " " + last_name

# print(introduction("James", "Bond"))

# Create a function named dog_years() that has two parameters named name and age. The function should compute the age in dog years and return the following string: "{name}, you are {age} years old in dog years"
def dog_years(name, age):
  return name + ", you are " + str(age * 7) + " years old in dog years"

# print(dog_years("Lola", 16))

# Create a function named lots_of_math(). This function should have four parameters named a, b, c, and d. The function should print 3 lines and return 1 value. Print the sum of a and b. Print d subtracted from c. Print the first number printed, multiplied by the second number printed. Finally return the third number printed mod a.
def lots_of_math(a, b, c, d):
  first = a + b
  second = c - d
  third = first * second
  print(first)
  print(second)
  print(third)
  return third % a

# print(lots_of_math(1, 2, 3, 4))
