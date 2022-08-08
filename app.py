# -----
# Methods
# -----

# Strip method = removes unwanted spaces ("white" spaces)
# Find method = locates string (returns index of first instance)

# MyName = "      Nick Gotsy"
# MyNameStripped = MyName.strip()
# print(MyNameStripped)
# print(MyNameStripped.find("Gotsy"))

# -----
# String Slicing
# -----

# Nick = 'Knows english and georgian '
# print(f"Nick knows {Nick[6:13]}/\"{Nick[-9:-1]}\"...\nHe's Bilingual")


# ----
# "Concatination" = linking variables together
# ----

# Greet_1 = "Hello "
# Greet_2 = "There"
# print(Greet_1 + Greet_2)


# -----
# Assignment operator = incrementing numbers
# -----

# Maria = 17
# Maria += 6
# print(f"If Maria was 6 years older, she would be {Maria}")

# -----
# Input function = user inputs the value
# -----

# while True:
#     CountryName = input("Country Name: ")
#     # break statement needs to go directly in the line below the variable in reference (CountryName)
#     if CountryName.lower() == "quit":
#         break
#     YearFounding = input(f"\"{CountryName}\" was founded in the year: ")
#     Statement = f"The country of {CountryName} was founded in {int(YearFounding)}"
#     print(Statement)


# # Below = "Concatinating" input values

# Variable_1 = input("What is x?: ")
# Variable_2 = int(Variable_1) + 1
# print(f"x: {Variable_1}, y: {Variable_2}")


# -----
# Input function (+ if statements)
# -----

# temperature = input("temperature: ")
# if int(temperature) >= 75:
#     print("It's hot outside")
# elif 75 >= int(temperature) >= 50:
#     print("It's nice outside")
# else:
#     print("It's cold outside")

# -----
# If statement (default for if-then statements = true)
# -----

# HighIncome = 1_000_000
# GoodCredit = 500
# if HighIncome and good_credit:
#     print("approved")

# -----
# Ternary Operator
# -----

# age = 22

# # if age >= 18:
# #     print("Eligible")
# # else:
# #     print("Not eligible")

# # Below = simplified version...
# EligibilityMessage = "Eligible" if age >= 18 else "Not eligible"

# print(EligibilityMessage)

# # Known as "chaining comparison operators"

# -----
# For Loop = used to iterate arguments in a function
# -----

# Goal = create a loading screen

# for number in range(1, 3, 1):
#     print("Attempting", number * ".")
# for number in range(3, 0, -1):
#     print("Attempting", number * ".")

# -----
# Break statement = used to get out a loop (once a condition is met)
# -----

# for number in range(5):
#     successful = number
#     print("Attempt", number)
#     if successful == 2:
#         print("Successful")
#         break
# else:
#     print("Attempted 5 times and failed")

# Comment out the break statement and see how that changes the return
# -----
# Nested Loops = Bigger loop and smaller loop
# -----

# for x in range(5):
#     for y in range(3):
#         print(f"({x},{y})")

# -----
# Iterable Objects = things that can be broken down in loops
# -----

# for x in [1, 2, 3, 4, 5]:
#     print(x)

# for x in "NickGotsy":
#     print(x)

## Start, stop, increment
# for x in range(2, 5, 1):
#     print(x)

# ShoppingCart = ["Tacos", "Beans", "Ravioli", "Chicken", "Chickpeas"]
# # enumerate = indexes the list
# print(list(enumerate(ShoppingCart)))
# print(ShoppingCart[1])


# -----
# While Loops
# -----

# number = 200
# while number >= 25:
#     print(number)
#     number //= 2

# Below = Example 2

# command = ""
# while command.lower() != "quit":
#     command = input(">")
#     if command == "Hey":
#         print("Why hey there")
#     if command != "Hey" or "Jeffrey":
#         print(command)

# Below = If input "0", don't know why it's giving me a return of "Your age is 0" instead of "terminated"...
# age = ""
# while age != 0:
#     if age == 0:
#         print("Terminated")
#     else:
#         age = int(input("Age: "))
#         print(f"Your age is {age}")

# ----
# Infinite Loops = starts off with "while True" and ends with a "break". Don't need to initialize variable
# ----

# while True:
#     command = input(">")
#     print("ECHO", command)
#     if command.lower() == "quit":
#         break

# -----
# Even numbers exercise
# -----

# count = 0
# for number in range(1, 10):
#     if number % 2 == 0:
#         count += 1
#         print(number)

# print(f"We have {count} even numbers")

# -----
# Defining Functions
# -----

# def increment(number, by):
#     return number + by

# print(increment(2, 1))

# # ---------

# def greet(FirstName, LastName):
#     FirstName = input("First Name: ")
#     LastName = input("Last Name: ")
#     print(f"Hey there {FirstName} {LastName} \n Welcome Aboard!")
# greet("", "")

# ------
# For-in + *Args (variable arguments)
# ------

# def ValueList(*numbers):
#     for number in numbers:
#         print(number*numbers)

# ValueList(5, 10, 6, 3, 2)

# ----------------

# def ShoppingList(*__words):
#     for word in __words:
#         print(word)

# ShoppingList("Oranges", "Broccoli", "Grapes", "Beans", "Tortilla wraps")
# ShoppingList("Apple", "Carrots", "Raspberry", "Chickpeas", "Taco shells")
# ShoppingList("Oranges", "Broccoli", "Grapes", "Beans", "Tortilla wraps")

# ------
# **Args (variable arguments, but now also creates dictionary)
# ------

# def userInfo(**Info):
#     print(Info["age"])

# userInfo(accountID=15423, firstName="Nick", lastName="Gotsy", age=23)

# --------

# def GroceryList(**WholeList):
#     print(WholeList)

# GroceryList(Expensive="Computer",
#             notExpensive="basketball",
#             cheap="Paper clips")

# ---------

# def GroceryList(**WholeList):
#     print(WholeList["Expensive"])

# GroceryList(Expensive="Computer",
#             notExpensive="basketball",
#             cheap="Paper clips")

# -----
# Global variables = take precedence over other variables of same name (even if local)
# -----

# # Below: letters = global variable
# letters = "goodbye"

# def greet(name):
#     # Letters here = local variable
#     for letters in name:
#         print(letters)

# greet("Nick")
# print(letters)

# # For-in loop using a number array...

# NumberArray = [0, 2, 4, 6, 8, 10]

# def Listout(items):
#     for eachitem in items:
#         print(eachitem)

# Listout(NumberArray)

# -------
# FizzBuzz Project (If + return statements)
# -------

# # Solution 1

# Number = int(input("Choose a number: "))
# if (Number % 5 == 0) and (Number % 3 == 0):
#     print("Fizz Buzz")
# if Number % 3 == 0:
#     print("Fizz")
# if Number % 5 == 0:
#     print("Buzz")

# Solution 2

# def fizz_buzz(input):
#     if (input % 5 == 0) and (input % 3 == 0):
#         return "FizzBuzz"
#     if input % 3 == 0:
#         return "Fizz"
#     if input % 5 == 0:
#         return "Buzz"

# print(fizz_buzz(15))

# -----
# List + range functions. Range = lists out 0 -> n-1
# -----

# numbers = list(range(20))
# numbers[1] = 69
# print(numbers)

# -----
# Unpacking Lists - to extract certain items, prefix a variable with: *
# -----

# Groceries = ["Apples", "Oranges", "Broccoli",
#              "Macaroni", "Tacos", "Hamburgers"]
# fruit1, fruit2, vegetable, *others = Groceries
# print(*others)

# -----
# Indexing lists (creating topples)
# -----

# ToDoList = ["By some books", "Sell stuff online", "Learn Python"]
# for index, ToDo in enumerate(ToDoList):
#     print(index, ToDo)

# -----
# Adding/removing items from list
# -----

# # Below = Adding item (method = .insert)

# GroceryItems = ["Tacos", "Enchiladas", "Carrots", "Cinammon sticks"]
# GroceryItems.insert(1, "Salsa")
# print(GroceryItems)

# # Below = Removing item (can also use: .remove (insert item, no index here), and to remove whole list, .clear())

# GroceryList = ["Apples", "Bananas", "Bananas", "Bananas", "Broccoli"]
# GroceryList.pop(2)
# print(GroceryList)


# Below = sorting alphabetically using split method

# GroceryItems = ["Tacos", "Enchiladas", "Carrots", "Cinammon sticks"]
# print(sorted("Tacos, Enchiladas, Carrots, Cinammon-sticks".split(), key=str.lower))


# # Downside of split = cannot store in a list variable
# # Below = sorting alphabetically using tuples

# GroceryItems_tuple = [("Tacos", 3), ("Enchiladas", 70),
#                       ("Carrots", 20), ("Cinammon sticks", 5)]
# print(sorted(GroceryItems_tuple, key=lambda GroceryItem: GroceryItem[0]))


# -----
# Sorting Tuples
# -----

# partPrices = [
#     ("muffler", 50),
#     ("hood", 10),
#     ("engine", 80),
#     ("tires", 30)
# ]


# def basedOnPrice(partsAndPrice):
#     return partsAndPrice[1]


# partPrices.sort(key=basedOnPrice)
# print(partPrices)


# -----
# Lambda function = shortens line of code in sorting tuples (from last lesson)
# -----

# items = [
#     ("muffler", 50),
#     ("engine", 20),
#     ("tires", 70),
#     ("windows", 30)
# ]

# items.sort(key=lambda partsAndPrice: partsAndPrice[1])
# print(items)

# -----
# Map function = Extracting a list from larger, tuple list (e.g. list of x in (x,y))
# -----

# Inefficient method (below)

# fruitAndPrices = [
#     ("apples", 20),
#     ("oranges", 10),
#     ("bananas", 30)
# ]

# names = []
# for item in fruitAndPrices:
#     names.append(item[0])

# print(names)

# Cleaner version = map function (below)

# fruitAndPrices = [
#     ("apples", 20),
#     ("oranges", 10),
#     ("bananas", 30)
# ]

# price_list = map(lambda items: items[1], fruitAndPrices)
# for price in price_list:
#     print(price)

# below = same, but uses list function (no for-in loop needed)

# fruitAndPrices = [
#     ("apples", 20),
#     ("oranges", 10),
#     ("bananas", 30)
# ]

# price_list = list(map(lambda fruitPrice: fruitPrice[1], fruitAndPrices))
# print(price_list)

# ----
# Filtering Lists = taking out touples with a certain value
# ----

# ProductAndPrice = [
#     ("Shoes", 10),
#     ("Hoodies", 30),
#     ("Shirts", 13),
#     ("Glasses", 60),
#     ("Socks", 5),
# ]

# filtered_list = list(filter(lambda product: product[1] >= 10, ProductAndPrice))
# print(filtered_list)

# -----
# List Comprehensions = preferred method to filter/map lists (noone uses filter and map functions...)
# -----
# Below = map List

# groceryItems = [
#     ("spinach", 5),
#     ("tomatoes", 6),
#     ("broccoli", 8)
# ]

# groceryPrices = [groceryItem[1] for groceryItem in groceryItems]
# print(groceryPrices)

# Below = filtering List

# groceryItems = [
#     ("spinach", 5),
#     ("tomatoes", 6),
#     ("broccoli", 8)
# ]

# groceryPricesOver6Dollars = [
#     groceryItem for groceryItem in groceryItems if groceryItem[1] > 6]
# print(groceryPricesOver6Dollars)

# -----
# Zip function = used to combine lists (in a way that first items of each lists now become their own list, second items their own, and so on)
# -----

# list1 = [1, 2, 3]
# list2 = "abc"

# print(list(zip([12, 15, 16], "HEY", list1, list2)))

# -----
# Changing variables
# -----

# # Goal = flip the value of the variables
# x = 10
# y = 11

# #Create a Tuple and set them to a flipped version
# x, y = y, x

# print("x =", x)
# print("y =", y)

# # Can do it with strings...

# a = "Nick"
# b = "Hello there,"
# c = "My name is"

# a, b, c = b, c, a

# print(a, b, c)

# -----
# Dictionary (key-value pairs) - looping over dictionaries uses method: .items
# -----

# phoneBook = dict(Norman=440_319_8858, Terry=216_315_3218)

# # for names in phoneBook:
# #     print(names, phoneBook[names])

# for names, numbers in phoneBook.items():
#     print(names,numbers)

# # item name = associates with key, variable[key] = value
# # Version below it = same result (little longer, but makes more sense)

# -----
# Comprehensions = used to clean code (used on lists, sets, and dictionaries)
# -----

# listDivisibleBy3 = []
# for number in range(5):
#     listDivisibleBy3.append(number * 3)
# print(listDivisibleBy3)

# 3 lines of code above = same as below (below = cleaner code)

# listDivisibleBy3 = [number * 3 for number in range(5)]
# print(listDivisibleBy3)

# -----
# Generator objects = helps reduce amount of memory taken from large lists (e.g. random number generator)
# -----

# from sys import getsizeof

# values = (x * 2 for x in range(100000))
# print("gen:", getsizeof(values))

# values = [x * 2 for x in range(100000)]
# pritn("list:", getsizeof(values))

# # Braces = generator
# # Brackets = list
# # Return = number of bytes it takes up

# -----
# Unpacking - To unpack items from list, prefix variable with: *
# -----

# # numbers = [1, 2, 3]
# # print(*numbers)

# # * = used fro both unpacking and unpacking combinations of lists
# # For dictionaries, used: ** - but this can only be used when used to combine lists

# # Notice, below (just unpacking)= will not work

# # numbers = {"hey": 1, "b": 2, "c": 3, "d": 4}
# # print(**numbers)

# # However, below (unpacking combinations, will work - very weird why its limited to that)

# peopleCleveland = {"John": 440_596_9476,
#                    "Terry": 555_555_5555, "Ricky": 314_157_9514}
# peopleCincinnati = {"John": 777_777_7777, "Jerimiah": 222_222_2222}

# combinedBooks = {**peopleCleveland, **peopleCincinnati, "Jacob": 666_666_6666}
# print(combinedBooks)

# -----
# Exercise = develop program that determines most repeated character in a sentence
# -----

# Basically:
# 1. Develop/initialize a dictionary
# 2. Create for loops for each character, increasing value by 1 for each time it appears in dictionary
# 3. Define new variable: sort dictionary (sorted), convert dictionary to tuples (.items; dictionaries can't be sorted), using lambda...
# ... sort based on the value (reverseTrue = descending order)
# 4. Print out the first tuple (highest value)

# sentence = "Hello there, my name is nick"
# char_frequency = {}
# for char in sentence:
#     if char in char_frequency:
#         char_frequency[char] += 1
#     else:
#         char_frequency[char] = 1
# characterList = sorted(char_frequency.items(),
#                        key=lambda kv: kv[1], reverse=True)
# print(characterList[0])

# -----
# Handling Exceptions = "try" clause - creates friendly error messages (prevents crashing)
# -----

# Goal = for an age input system, \if no value is put in, system tells you to try again. If value = 0, terminates system.

# age = ""
# while age != 0:
#     try:
#         age = int(input("age: "))
#     except ValueError:
#         print("You didn't enter an integer value for your age. Try again")
#     else:
#         if age == 0:
#             print("Operation Terminated")
#         else:
#             print(f"Processed! You have updated your age to: {age}!")

# -----
# Raising Exceptions = adding exceptions to default error message (I.e. making it more picky - not commonly used since it slows the system)
# -----

# def how_many_burgers_did_you_have(number):
#     if number < 0:
#         raise ValueError("You cannot have a negative number...")

# try:
#     how_many_burgers_did_you_have(-5)
# except ValueError as you_cant_eat_negative_burgers:
#     print(you_cant_eat_negative_burgers)

# Below = more efficient version

# def how_many_burgers_did_you_have(number):
#     if number < 0:
#         return None

# Burgers = how_many_burgers_did_you_have(-5)
# if Burgers == None:
#     pass

# Main takeaway = avoid raising exceptions. See if it can alternatively be handled by an if-statement first

# -----
# Constructor = sets initial values for an object. Uses magic method called "__init__"
# -----

# First = define the class. Uses constructor magic method
# class PoundsInches:
#     def __init__(self, weight, height):
#         self.weight = weight
#         self.height = height

# # Next = inside class code block, define a method

#     def WeightHeight(self):
#         print(f"Nick is {self.weight} pounds, and {self.height} inches tall")

# # Finally, set a new variable to a class and input parameters (after self). Then, call for method on the newly-defined variable

# Nick = PoundsInches(150, 69)
# Nick.WeightHeight()

# # Below = another example

# class GradeAttendance:
#     def __init__(self, Grade, Attendance):
#         self.Grade = Grade
#         self.Attendance = Attendance

#     def PersonGradeAttendance(self):
#         print(
#             f"Jerry scored {self.Grade}% on average on his exams, while attending class {self.Attendance}% of the time")

# Jerry = GradeAttendance(95, 75)
# Jerry.PersonGradeAttendance()
# print(Jerry.Attendance)

# -----
# Magic methods = used to modify an object(e.g. into a string)
# -----

# class CalSpice:
#     def __init__(self, calories, spicyness):
#         self.calories = calories
#         self.spicyness = spicyness

#     def __str__(self):
#         return f"({self.calories}, {self.spicyness})"

# ChickenTaco = CalSpice(400, 3)
# print(ChickenTaco)

# # If it wasn't for the __str__ magic method, return for Chicken Taco = random number location where "ChickenTaco" variable is stored

# -----
# Comparing Objects (__eq__ = gathered from a magic methods website)
# -----

# class CalSpice:
#     def __init__(self, calories, spicyness):
#         self.calories = calories
#         self.spicyness = spicyness

#     def __eq__(self, other):
#         return self.calories == other.calories and self.spicyness == other.spicyness

# ChickenTaco = CalSpice(400, 3)
# BeefBurrito = CalSpice(600, 7)
# print(ChickenTaco == BeefBurrito)

# class CalSpice:
#     def __init__(self, calories, spicyness):
#         self.calories = calories
#         self.spicyness = spicyness

#     def __gt__(self, other):
#         return self.calories > other.calories and self.spicyness > other.spicyness

# ChickenTaco = CalSpice(400, 3)
# BeefBurrito = CalSpice(600, 7)
# print(BeefBurrito > ChickenTaco)

# # If you don't include __eq__ magic method, return = false (since "CalSpice" object = stored in different addresses by default)

# -----
# Arithmetic between objects (e.g. adding, subtracting)
# -----

# class CalSpice:
#     def __init__(self, calories, spicyness):
#         self.calories = calories
#         self.spicyness = spicyness

#     def __add__(self, other):
#         return CalSpice(self.calories + other.calories, self.spicyness + other.spicyness)

#     def __str__(self):
#         return f"({self.calories}, {self.spicyness})"

# ChickenTaco = CalSpice(400, 3)
# BeefBurrito = CalSpice(600, 7)
# CombinedMeal = ChickenTaco + BeefBurrito
# print(CombinedMeal)
# print(CombinedMeal.calories)

# __str__ magic method = makes the return for "CombinedMeal" possible (otherwise returns random location in memory the variable is stored)

# -----
# Making a custom container (lists, sets, dictionaries = all examples of containers)
# -----

# Objective = find out how many times a variable is "tagged" with "Python"

# First, define class, make constructor, initialize dictionary ("built-in data structure")

# class HowMuchThisWordIsFound:
#     def __init__(self):
#         self.__words = {}

# # setitem = allows to set initial value for "python" tag. See WordSearcher["python"] = 10

#     def __setitem__(self, word, count):
#         self.__words[word.lower()] = count

# # Add function = used to increment the value in the key-value pair. See WordSarcher.add("Python")

#     def add(self, word):
#         # Below: key = left of equal sign, value = right of equal sign
#         self.__words[word.lower()] = self.__words.get(word.lower(), 0) + 1

# # getitem = allows us to get data from: WordSearcher["python"]

#     def __getitem__(self, word):
#         return self.__words.get(word.lower(), 0)

# WordSearcher = HowMuchThisWordIsFound()
# WordSearcher["python"] = 10
# WordSearcher.add("Python")
# WordSearcher.add("python")
# WordSearcher.add("pYtHoN")
# print(WordSearcher.__words)
# print(WordSearcher["python"])

#  -----
#  Private Members = used to access "underlying dictionary" (i.e. words) in which the attribute/method is made private (by underscores)
#  -----

# To make an attribute/method (words) private, prefix with two underscores

# class HowMuchThisWordIsFound:
#     def __init__(self):
#         self.__words = {}

#     def __setitem__(self, word, count):
#         self.__words[word.lower()] = count

#     def add(self, word):
#         self.__words[word.lower()] = self.__words.get(word.lower(), 0) + 1

#     def __getitem__(self, word):
#         return self.__words.get(word.lower(), 0)

# WordSearcher = HowMuchThisWordIsFound()
# WordSearcher.add("Python")
# WordSearcher.add("pYTHoN")
# print(WordSearcher._HowMuchThisWordIsFound__words)

# -----
# Properties = used to limit the values an attribute can take
# -----

# Goal = Don't wan't amazon total cart price to be a negative number
# Not using property yet.. (next part we will)

# class AmazonCartTotalPrice:
#     # Step 1 = in constructor, refer to set method (defined later
#     def __init__(self, totalPrice):
#         self.set_summaryTotal(totalPrice)

#     # Step 2 = define a get method
#     def get_summaryTotal(self):
#         return self.__summaryTotal

#     # Step 3 = method for setting the attribute
#     # Here = raise exception
#     def set_summaryTotal(self, value):
#         if value < 0:
#             raise ValueError("Price cannot be a negative value")
#         self.__summaryTotal = value

# # Test Run...

# CartTotal = AmazonCartTotalPrice(-50)

# # Below = using same code as above, but now, using properties (more "pythonic")
# # Goal = Don't wan't amazon total cart price to be a negative number

# class AmazonCartTotalPrice:
#     # Step 1 = create constructor
#     def __init__(self, totalPrice):
#         self.summaryTotal = totalPrice

#     # Step 2 = "Get" decorator = used to hide get method from appearing after dot operator (not needed to appear there)
#     @property
#     # Step 3 = create method for getting the attribute (We have decorator, so don't need to explicitly write get method)
#     def summaryTotal(self):
#         return self.__summaryTotal

#     # Step 3 = "Set" decorator
#     @summaryTotal.setter
#     # Step 3= method for setting the attribute. Here, raising exception (what if value less than zero)
#     def summaryTotal(self, value):
#         if value < 0:
#             raise ValueError("Price cannot be a negative value")
#     # ... Otherwise, return that value(
#         self.__summaryTotal = value

# # Test Run...

# CartTotal = AmazonCartTotalPrice(10)
# print(CartTotal.summaryTotal)
# CartTotal.summaryTotal = -1
# print(CartTotal.summaryTotal)

# # Below = without comments

# class AmazonCartTotalPrice:
#     def __init__(self, totalPrice):
#         self.summaryTotal = totalPrice

#     @property
#     def summaryTotal(self):
#         return self.__summaryTotal

#     @summaryTotal.setter
#     def summaryTotal(self, value):
#         if value < 0:
#             raise ValueError("Price cannot be a negative value")
#         self.__summaryTotal = value

#  -----
#  Method Overriding: if methods are used to allow for parent method to be inherited to child (e.g. if both initialized to something)
#  -----
# # Below, methods size and weight = initialized
# # To override, use function: super

# class Animal:
#     def __init__(self):
#         print("It's an animal")
#         self.size = "bigger than an insect"

# class Mammal(Animal):
#     def __init__(self):
#         super().__init__()
#         print("Does not lay eggs")
#         self.weight = "weighs more than an insect"

# Zebra = Mammal()
# print(Zebra.size)
# # print(Zebra.weight)

# # Notice the order in which the return is given (flip-flop between the two print statements above)
# # Can change this order by changing the line in which the super function is called

# class Animal:
#     def __init__(self):
#         print("It's an animal")
#         self.size = "bigger than an insect"

# class Mammal(Animal):
#     def __init__(self):
#         print("Does not lay eggs")
#         self.weight = "weighs more than an insect"
#         # Now, super function is on the bottom. The print statement directly above gets called first, then the rest
#         super().__init__()

# Zebra = Mammal()
# print(Zebra.size)
# # print(Zebra.weight)

# -----
# Good example of Inheritance
# -----

# # Want to make it so that if something is opened/closed, can't opened/closed again
# # Raise a "custom exception" (one that's not built-in by Python)...

# from abc import ABC, abstractmethod

# class InvalidOperationError (Exception):
#     pass

# class Stream:
#     # Initialize an "open flag" (telling you when the application is opened)
#     def __init__(self):
#         self.opened = False

#     # Define open method
#     # Refer to  custom exception
#     def open(self):
#         if self.opened:
#             raise InvalidOperationError("Stream is already opened")
#         self.opened = True

#     # Define close method
#     # Refer to custom exception
#     def close(self):
#         if not self.opened:
#             raise InvalidOperationError("Stream is already closed")
#         self.opened = False

# # Creating the parent and child classes

# class FileStream (Stream):
#     def read(self):
#         print("Reading data from a file")

# class NetworkStream (Stream):
#     def read(self):
#         print("Reading data from a network")

# ----
#  Polymorphisms
# ----
# Can be used to "render" the user-interface (UI) of an application
# Objective = Have a form that contains a dropdown list and textbox. Want to pass that to a function called "draw()" that renders both of them at once

# from abc import ABC, abstractmethod

# # Create an abstract base class

# class UIControl(ABC):
#     @abstractmethod
#     def draw(self):
#         pass

# # Create textbox and dropdownlist classes (become children of the abstract class)

# class TextBox(UIControl):
#     def draw(self):
#         print("This is the content of the textbox")

# class DropDownList(UIControl):
#     def draw(self):
#         print("This is the content of the dropdown list")

# # Create draw() function. Make it iterable (so that it extracts textbox + dropdownlist))

# def draw(Everything):
#     for eachthing in Everything:
#         eachthing.draw()

# ddl = DropDownList()
# textbox = TextBox()
# draw([ddl, textbox])

# Called "Polymorphism" since draw() function here takes on many forms (i.e. can take on textbox + dropdown list in this scenario, and...
# ... maybe radio lists, checkboxes, description lists in another)

# ----
# Extending Built-in Types = using inheritance on classes that come Built-in on python
# ----

# # Goal = create a way to log the times you append (i.e. add) something

# class MyNumber(list):
#     def append(self, object):
#         # "Extend" the built-in append method (i.e. does whatever it does normally by default, but add this print statement to it)
#         print("Something was added!")
#         # Call the append method of the base ("super") class
#         super().append(object)

# Mylist = MyNumberList()
# Mylist.append("1")

# -----
# Data Classes - classes that have no functionality, just data. For these, instead of using eq magic method, use "namedtuple"
# -----

# Objective = find a way to equate 2 grocery lists that specify for the same things (e.g. both ask for 1 apple, 2 bananas)

# # Import package
# from collections import namedtuple

# # Create a variable with namedtuple function
# GroceryLists = namedtuple("List", ["apples", "bananas"])
# # For arguments, they need to be in key-word form
# GroceryList_1 = GroceryLists(apples=1, bananas=2)
# # print(GroceryList_1.apples)
# GroceryList_2 = GroceryLists(apples=1, bananas=2)
# print(GroceryList_1 == GroceryList_2)

# # Requires less code than eq magic method. But downside = "immutable" (we cannot alter any of these grocery lists)

# -----
# Package = a "subdirectory" (sub-folder) with multiple files
# -----

# # Here, created subdirectory "ecommerce". Needs to include a file __init__.py
# # After doing so, need to adjust the import statement (i.e. prefix by the subdirectory )

# from ecommerce.sales import calc_shipping

# calc_shipping()

# # Below = importing a script (see sales.py and __init__.py - run the code). Above = also does this function (even though specifically asking for "sales" file, gives you __init__ file info as well)

# from ecommerce import sales

# ----
# Working with paths/directories/files
# ----

# # Inside Path class, can modify/observe a path, directory, or file
# # Below = example of working with a file

# from pathlib import Path

# path = Path("ecommerce/__init__.py")

# # Put exists method in print function
# # path.exists()
# # path.rename()

# #.unlink = deletes the path (i.e. deletes __init__.py in ecommerce directory)
# # path.unlink()
# # path.stat()

# ----
# Copying Files = uses "shell utilities" (shutil)
# ----

# from pathlib import Path
# import shutil

# source = Path("ecommerce/__init__.py")
# target = Path() / "__init__.py"
# shutil.copy(source, target)

# # When you run it, creates another __init__.py file (that's not in a directory - but can always make it one)

# ----
# Zip file (Part 1)
# ----

# # Goal = gather all the files from an ecommerce directory and "write" (store it all into) a zip file

# from pathlib import Path
# from zipfile import ZipFile

# # "w" = writes to zip file (i.e. stores everything into it)
# # In case something goes wrong, "with" statement prevents error (better replacement than a close method (below))

# with ZipFile("ecommerce_files.zip", "w") as zip:
#     # .rglob = used to "recursively"(i.e. repeatedly) find all files and its children
#     # Iterate over it (since default = generator) - create a "zip" variable
#     for each_file_path_inside_ecommerce in Path("ecommerce").rglob("*.*"):
#         zip.write(each_file_path_inside_ecommerce)

# # Keep  line below in a comment (just demonstrates with-as statement = doesn't need a close statement)
# # zip.close()

# -----
# Zip File (Part 2)
# -----

# Goal = Extract the Zip file created (for modifying/reading)

# from pathlib import Path
# from zipfile import ZipFile

# # namelist method = returns all the names of files
# with ZipFile("ecommerce_files.zip") as zip:
#     # namelist = returns list of file names
#     print(zip.namelist())
#     # Extractall function = extracts the content of each file name in zip into a directory created called "Extracted_Zip_File"
#     zip.extractall("Extracted_Zip_File")

# ----
# Working with JSON (part 1)
# ----

# Goal = create an array of dictionaries, and "write it" to a file

# import json
# from pathlib import Path

# # E.g. create an array of dictionaries (each item = key-value pairs)
# movies = [{"id": 1, "title": "Catch Me If You Can", "year": 2003},
#           {"id": 2, "title": "Terminator", "year": 1989}
#           ]

# MoviesList = json.dumps(movies)
# Path("movies.json").write_text(MoviesList)

# # Here, created an array of dictionaries to begin with - so JSON didn't do any conversion. Not always the case (esp if diff language)

# ----
# Working with JSON (part 2)
# ----
# # Goal = read JSON File from an external source (i.e. from a different website)

# import json
# from pathlib import Path

# MoviesList = Path("movies.json"). read_text()
# # loads function = returns an array of dictionaries
# Movies = json.loads(data)
# # Can extract whats needed from the dictionary using square brackets
# print(Movies[0]["title"])

# ----
# Working with SQL Database (Part 1) - Creating a table
# ----

# # Goal = create a table of movies, each containing an ID, Title, and Year created

# import sqlite3
# import json
# from pathlib import Path

# # Assign list of movies to a variable
# # read_text function = loads all content as a string
# MoviesList = json.loads(Path("Movies/movies.json").read_text())
# # Make sure it works
# print(MoviesList)

# # Store movies list to a database
# # Use method connect
# with sqlite3.connect("TheMoviesDatabase.sqlite3") as connection:
#     # Create a command for movies table (for modifying the data)
#     # Question marks = placeholders for the column names (i.e. id, name, year)
#     command = "INSERT INTO Movies VALUES(?, ?, ?)"
#     # Iterate over MoviesList
#     for movie in MoviesList:
#         connection.execute(command, tuple(movie.values()))
#     # Create commit method
#     connection.commit()


# ----
# Working with SQL Database (Part 2) - Reading a table
# ----

# # Goal = read a movie list data from SQL database (i.e. get a return in tuple form)

# import sqlite3
# import json
# from pathlib import Path

# with sqlite3.connect("TheMoviesDatabase.sqlite3") as connection:
#     command = "SELECT * FROM Movies"
#     cursor = connection.execute(command)

#     # fetchall = returns all columns at once
#     movies = cursor.fetchall()
#     print(movies)

# -----
# Timestamps = used to track the time of something
# -----

# # Goal = figure out how long it took to "send" 1,000,000 emails

# import time


# def send_emails():
#     for i in range(1_000_000):
#         pass


# # Mark the time before the action
# start = time.time()
# # Commit the action
# send_emails()
# # Mark the time after the action
# end = time.time()
# duration = end - start
# print(duration)


# -----
# Generating Random Values
# -----

# import random

# # Every run = different floating point value
# print(random.random())

# # Different integer between values
# print(random.randint(1, 10))

# # Randomly picking a number in an array of values
# print(random.choice([1, 2, 3, 4]))

# # Goal = generating a random password
# # Empty string = serves to join the words together (can include anything in it)
# print("".join(random.choices("abcdefghijklmnop", k=6)))

# ----
# Sending Emails
# ----

# # If you experience issues, it comes from the format of the HTML file. So play around with the lines python arises in problem section

# # Allows to send email in both HTML and plain form (if HTML not supported)...
# from email.mime.multipart import MIMEMultipart
# # If there is a header not supported by MIMEMultipart, treat as string...
# from email.mime.text import MIMEText
# # Import image...
# from email.mime.image import MIMEImage
# # Create a path to images...
# from pathlib import Path
# # Create an HTML template...
# from string import Template
# # Send message through an SMTP server...
# import smtplib

# # Create an HTML template. read_text = returns content as a string
# template = Template(Path("mail.html").read_text())

# message = MIMEMultipart()
# # Set headers supported by MIMEMultipart (e.g. from, to, subject)
# message["from"] = "Nick Gotsy"
# message["to"] = "nick.gotsy@gmail.com"
# message["subject"] = "Meth Dealer?"
# # Substitute method = allows for dynamic parameters (in html doc, used $name)
# body = template.substitute({"name": "Niko"})
# # Body section not supported by MIMEMultipart, so need to "attach" it
# message.attach(MIMEText(body, "html"))
# # read_bytes = returns data in binary form (makes image readable)
# message.attach(MIMEImage(Path("Jesse and Walter.jpg").read_bytes()))

# # To connect with SMTP server, call the module with class SMTP
# # Once done with it, need to close it - so use a with statement
# with smtplib.SMTP(host="smtp.gmail.com", port=587) as smtp:
#     # "Hello" message for smtp server
#     smtp.ehlo()
#     # SMTP connection is "transport-layer security" (messages = become encrypted)
#     smtp.starttls()
#     # Input username and password. Password = has to be a generated app pasword (found in security section in Google account)
#     smtp.login("nick.gotsy@gmail.com", "tfjmulhjqswnzzbz")
#     # Pass through the object
#     smtp.send_message(message)
#     # For confirmation things went through...
#     print("Sent...")

# # Below = non-comment version

# from email.mime.multipart import MIMEMultipart
# from email.mime.text import MIMEText
# from email.mime.image import MIMEImage
# from pathlib import Path
# from string import Template
# import smtplib

# template = Template(Path("Mail/mail.html").read_text())
# message = MIMEMultipart()
# message["from"] = "Nick Gotsy"
# message["to"] = "nick.gotsy@gmail.com"
# message["subject"] = "Meth Dealer?"
# body = template.substitute({"name": "Niko"})
# message.attach(MIMEText(body, "html"))
# message.attach(MIMEImage(Path("Jesse and Walter.jpg").read_bytes()))

# with smtplib.SMTP(host="smtp.gmail.com", port=587) as smtp:
#     smtp.ehlo()
#     smtp.starttls()
#     smtp.login("nick.gotsy@gmail.com", "tfjmulhjqswnzzbz")
#     smtp.send_message(message)
#     print("Message Sent!")


#  -----
#  Commmand-line Arguments
#  -----

# # Goal = allowing user to create a password

# import sys
# # print(sys.argv)

# # There's always needs to be at least 1 argument when putting in "app.py"
# if len(sys.argv) == 1:
#     print("USAGE: python3 app.py <password>")
# # In terminal, when app.py is followed by something, that will become the password (e.g. python app.py 1234 = password is now 1234)
# else:
#     password = sys.argv[1]
#     print("Password", password)
# -----
# Running Operating/External Programs
# -----

# Goal = python script that executes another python script

# import sys
# import subprocess

# run = subprocess.Popen([sys.executable, "ecommerce/sales.py"])
# run.communicate()

# -----
# Format method
# ----

# # Goal = Embed John's age into an age sentence

# John_age = 36
# Age_sentence = "My name is John, and I am {}"
# print(Age_sentence.format(John_age))

# -----
# In operator
# -----

# # Goal = check if item is in the grocery list

# Grocery_list = ["apple", "banana", "tacos"]
# if "tacos" in Grocery_list:
#     print("We need tacos!")

# ----
# Continue clause = used to alter an iteration
# ----

# # Goal = instead of printing "i" for 3, say "tres"

# i = 0
# while i < 6:
#     i += 1
#     if i == 3:
#         print("tres")
#         continue
#     print(i)

# -----
# __init__ function = used to define a function in a class
# -----

# # Goal = Nick is an object of the person class. Create a way in which Nick.lastname = gives you his last name


# class Person:
#     def __init__(self, fname, lname, age):
#         self.first_name = fname
#         self.last_name = lname
#         self.age = age


# Nick = Person("Nickolaus", "Gotsiridze", 23)

# print(Nick.last_name)


# ----
# Inheritance
# ----

# # Follow through code to explain to yourself why the return is so (starting from x.printname())

# class Person:
#     def __init__(self, fname):
#         self.firstname = fname

#     def printname(self):
#         print(self.firstname)


# # Below = just to make Student class inherit Person
# class Student(Person):
#     pass


# x = Student("Mike")

# x.printname()


# -----
# JSON = basically a python dictionary (but the whole thing is surrounded by string quotes)
# -----

# # Loads function = converts JSON -> Python dict

# import json

# # x = JSON
# x = '{"name": "John", "age": 30, "city": "NYC"}'
# y = json.loads(x)
# # Below: return = python dictionary
# print(y["age"])


# # Dumps function = converts Python dict -> JSON

# x = {"name": "John", "age": 30, "city": "NYC"}
# y = json.dumps(x)
# # Below: return = JSON string
# print(y)
