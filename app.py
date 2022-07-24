# PrimitiveType = 'Numbers' or 'Booleans' or 'Strings'
# print(bool(PrimitiveType == "Strings"))
# ???
# --------------------------------------------------

# -----
# Methods
# -----

# MyName = "      Nick Gotsy"
# MyNameStripped = MyName.strip()
# print(MyNameStripped.find("Nick"))

# -----
# String Slicing
# -----

# Nick = 'Knows english and georgian '
# print(f"Nick knows {Nick[6:13]}/\"{Nick[-9:-1]}\"... \nHe's Bilingual")

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
# Input function = used for when user puts in the value (lines 49-51 = concatinating input values)
# -----

# CountryName = input("Country Name: ")
# YearFounding = input(f"\"{CountryName}\" was founded in the year: ")
# Statement = f"The country of {CountryName} was founded in {int(YearFounding)}"
# print(Statement)


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

# # Instead of lines 81-84...
# EligibilityMessage = "Eligible" if age >= 18 else "Not eligible"
# # Known as "chaining comparison operators"


# -----
# For Loop
# -----

# for number in range(1, 3, 1):
#     print("Attempting", number * ".")
# for number in range(3, 0, -1):
#     print("Attempting", number * ".")


# -----
# Break statement
# -----

# successful = False
# for number in range(3):
#     print("Attempt")
#     if successful:
#         print("Successful")
#         break
#     else:
#         print("Attempted 3 times and failed")

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

# for x in range(2, 5, 1):
#     print(x)

# ShoppingCart = ["Tacos", "Beans", "Ravioli", "Chicken", "Chickpeas"]
# print(list(enumerate(ShoppingCart)))


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

# letters = "goodbye"


# def greet(name):
#     for letters in name:
#         print(letters)


# greet("Nick")
# print(letters)


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
# print(items)

# PartPrices = [
#     ("muffler", 50),
#     ("hood", 10),
#     ("engine", 80),
#     ("tires", 30)
# ]


# def SortingBasedOnPrice(items):
#     return items[1]


# PartPrices.sort(key=SortingBasedOnPrice)
# print(PartPrices)


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
# Flipping variables = create tuples with them and set that equal to a flipepd tuple (line 501)
# -----

# x = 10
# y = 11

# x, y = y, x

# print("x =", x)
# print("y =", y)

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

# age = ""
# while age != 0:
#     try:
#         age = int(input("age: "))
#     except ValueError:
#         print("You didn't enter an integer value for your age. Try again")
#     else:
#         if age == 0:
#             print("Terminated")
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

# class AmazonCartTotalPrice:
#     # Step 1 = create constructor

#     def __init__(self, totalPrice):
#         self.summaryTotal = totalPrice

#     # Step 2 = "Get" decorator = used to hide get method from appearing after dot operator (not needed to appear there)
#     @property
#     # Step 3 = create method for getting the attribute (We have decorator, so don't need to explicitly write get method)
#     def summaryTotal(self):
#         return self.__summaryTotal

#     # Step 3 = "Set" Decorator

#     @summaryTotal.setter
#     # Step 3= method for setting the attribute. Here, raising exception (if value less than zero)
#     def summaryTotal(self, value):
#         if value < 0:
#             raise ValueError("Price cannot be a negative value")
#     # ... Otherwise, return that value
#         self.__summaryTotal = value


# # Test Run...


# CartTotal = AmazonCartTotalPrice(10)
# print(CartTotal.summaryTotal)
# CartTotal.summaryTotal = -1
# print(CartTotal.summaryTotal)


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
#     def clse(self):
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
