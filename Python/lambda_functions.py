# Lambda functions, also known as anonymous functions, are small, inline functions that can have any number of arguments but only one expression. They are defined using the lambda keyword, which has no meaning other than “we are defining a lambda function.” The syntax is as follows:

# lambda arguments: expression

# The arguments are the inputs to the function, and the expression is the output. Here is an example of a lambda function that takes two arguments and returns their sum:

add = lambda x, y: x + y
print(add(5, 3))  # Output: 8


# Lambda function to print a name 

greeting = lambda name: f"Hello, {name}!" 

print(greeting("Steve"))  # Output: Hello, Steve!

# Using Lambda with map(), filter(), and reduce()
# Lambda functions are often used with map(), filter(), and reduce() to perform operations on sequences. Here is an example of using a lambda function with map() to double each element in a list:

numbers = [1, 2, 3, 4, 5]
doubled = list(map(lambda x: x * 2, numbers))
print(doubled)  # Output: [2, 4, 6, 8, 10]

# Using a lambda function with filter() to filter out even numbers from a list:

numbers = [1, 2, 3, 4, 5]
evens = list(filter(lambda x: x % 2 == 0, numbers))
print(evens)  # Output: [2, 4]

# Using a lambda function with reduce() to calculate the sum of a list:

from functools import reduce

numbers = [1, 2, 3, 4, 5]
total = reduce(lambda x, y: x + y, numbers)
print(total)  # Output: 15


# Using Lambda with sorted()
# Lambda functions are also commonly used with the sorted() function to specify a custom key for sorting. Here is an example of using a lambda function to sort a list of tuples based on the second element of each tuple:

students = [("Alice", 25), ("Bob", 22), ("Charlie", 28)]
sorted_students = sorted(students, key=lambda x: x[1])
print(sorted_students)  # Output: [('Bob', 22), ('Alice', 25), ('Charlie', 28)]
