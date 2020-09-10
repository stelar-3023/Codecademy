# class Student:
#   def __init__(self, name, year):
#     self.name = name
#     self.year = year
#     self.grades = [] # list
#     self.attendance = {} # dictionary

#   def __repr__(self):
#       return "{0} is in year {1}.  This student's grades are {2}.".format(self.name, self.year, self.grades)
  
#   def add_grade(self, grade):
#       self.grade = grade
#       if type(grade) == Grade:
#           self.grades.append(self.grade.score) # attr from Grade
#   def get_average(self):
#       return "{0}'s average is {1}.".format(self.name, sum(self.grades) / len(self.grades))      

# class Grade:
#   minimum_passing = 65
  
#   def __init__(self, score):
#     self.score = score

#   def is_passing(self):
#       return self.score >= self.minimum_passing
    
# roger = Student("Roger van der Weyden", 10)
# sandro = Student("Sandro Botticelli", 12)
# pieter = Student("Pieter Bruegel the Elder", 8)

# pieter.attendance["2019-5-14"] = True
# pieter.attendance["2019-5-15"] = False

# for i in range(95, 101):
#     roger.add_grade(Grade(i))

# print(roger)
# print(sandro)
# print(pieter)   
# thumbs_up = Grade(99)
# thumbs_down = Grade(64)

# print(roger.get_average())
# print(thumbs_up.is_passing())
# print(thumbs_down.is_passing())

# print(pieter.attendance)

# Inheritance and Polymorphism
# class Bin:
#   pass
# class RecyclingBin(Bin):
#   pass
# Define your exception up here:
# class OutOfStock(Exception):
#   pass

# # Update the class below to raise OutOfStock
# class CandleShop:
#   name = "Here's a Hot Tip: Buy Drip Candles"
#   def __init__(self, stock):
#     self.stock = stock
    
#   def buy(self, color):
#     if self.stock[color] < 1:
#       raise OutOfStock
#     self.stock[color] = self.stock[color] - 1

# candle_shop = CandleShop({'blue': 6, 'red': 2, 'green': 0})
# candle_shop.buy('blue')

# # This should raise OutOfStock:
# candle_shop.buy('green')

# Overriding Methods

# class Message:
#   def __init__(self, sender, recipient, text):
#     self.sender = sender
#     self.recipient = recipient
#     self.text = text

# class User:
#   def __init__(self, username):
#     self.username = username
    
#   def edit_message(self, message, new_text):
#     if message.sender == self.username:
#       message.text = new_text

# class Admin(User):
#   def edit_message(self, message, new_text):
#     message.text = new_text

# Super()
# class PotatoSalad:
#   def __init__(self, potatoes, celery, onions):
#     self.potatoes = potatoes
#     self.celery = celery
#     self.onions = onions

# class SpecialPotatoSalad(PotatoSalad):
#     def __init__(self, potatoes, celery, onions):
#         super().__init__(potatoes, celery, onions)
#         self.raisins = 40

# Interfaces
# class InsurancePolicy:
#   def __init__(self, price_of_item):
#     self.price_of_insured_item = price_of_item

# class VehicleInsurance(InsurancePolicy):
#     def get_rate(self):
#         return .001 * self.price_of_insured_item

# class HomeInsurance(InsurancePolicy):
#     def get_rate(self):
#         return .00005 * self.price_of_insured_item

# Polymorphism
# a_list = [1, 18, 32, 12]
# a_dict = {'value': True}
# a_string = "Polymorphism is cool!"
# print(len(a_list))
# print(len(a_dict))
# print(len(a_string))

# class Atom:
#   def __init__(self, label):
#     self.label = label
#   def __add__(self, other):
#       return Molecule([self, other])
    
# class Molecule:
#   def __init__(self, atoms):
#     if type(atoms) is list:
# 	    self.atoms = atoms
      
# sodium = Atom("Na")
# chlorine = Atom("Cl")
# salt = Molecule([sodium, chlorine])
# salt = sodium + chlorine

# class LawFirm:
#   def __init__(self, practice, lawyers):
#     self.practice = practice
#     self.lawyers = lawyers
#   def __len__(self):
#       return len(self.lawyers)
#   def __contains__(self, lawyer):
#       return lawyer in self.lawyers    
# d_and_p = LawFirm("Injury", ["Donelli", "Paderewski"])

# print(len(d_and_p))
 
# class SortedList (list):
#     def append(self, value):
#         super().append(value)
#         self.sort()
# new_sort = SortedList([4, 1, 5])
# print(new_sort)  