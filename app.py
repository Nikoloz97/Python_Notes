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

# -----------------------

# command = ""
# while command.lower() != "quit":
#     command = input(">")
#     if command == "Hey":
#         print("Why hey there")
#     if command != "Hey" or "Jeffrey":
#         print(command)


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

# def ShoppingList(*words):
#     for word in words:
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

# numbers = [1, 2, 3, 4, 5, 6, 7, 8]
# first, second, *others = numbers
# print(first)
# print(others)


# -----
# Indexing lists (creating topples)
# -----

# letters = ["a", "b", "c"]

# for index, letter in enumerate(letters):
#     print(index, letter)

# letters = ["a", "b", "b", "b", "c"]
# letters.remove("b")
# print(letters)


# -----
# Sorting Tuples
# -----

# items = [
#     ("muffler", 50),
#     ("hood", 10),
#     ("engine", 80),
#     ("tires", 30)
# ]


# def basedOnPrice(partsAndPrice):
#     return partsAndPrice[1]


# items.sort(key=basedOnPrice)
# print(items)

# -----
# Lambda function
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
# Map function = Used to extract certain aspects from a tuple list
# -----


# fruitAndPrices = [
#     ("apples", 20),
#     ("oranges", 10),
#     ("bananas", 30)
# ]

# price_list = map(lambda fruitPrice: fruitPrice[1], fruitAndPrices)
# for price in price_list:
#     print(price)

# ---> below = same, but uses list function (notice no for-in loop needed anymore)


# fruitAndPrices = [
#     ("apples", 20),
#     ("oranges", 10),
#     ("bananas", 30)
# ]

# price_list = list(map(lambda fruitPrice: fruitPrice[1], fruitAndPrices))
# print(price_list)


# -----
# List Comprehensions = preferred method to filter/map lists
# -----

# groceryItems = [
#     ("spinach", 5),
#     ("tomatoes", 6),
#     ("broccoli", 8)
# ]

# groceryPrices = [
#     groceryItem for groceryItem in groceryItems if groceryItem[1] > 6]
# print(groceryPrices)


# -----
# Zip function = used to combine multiple lists
# -----

# list1 = [1, 2, 3]
# list2 = "abc"

# print(list(zip([12, 15, 16], "HEY", list1, list2)))


# -----
# Switching variables
# -----

# x = 10
# y = 11

# x, y = y, x

# print("x", x)
# print("y", y)


# -----
# Dictionary = used to "map" a key -> value
# -----

# phoneBook = {"Norman": 440_596_9476, "Terry": 330_990_3495}
# phoneBook = dict(Norman=440_319_8858, Terry=216_315_3218)
# print(phoneBook)

# # for names in phoneBook:
# #     print(names, phoneBook[names])

# for names, numbers in phoneBook.items():
#     print(names, numbers)

# 1st line = used for initialization
# 2nd line = contains "keyword arguments" (e.g. x=10)
# Lines 252-253 = same effect as the lines below it

# -----
# Comprehensions = used to clean code
# -----

# listDivisibleBy3 = []
# for number in range(5):
#     listDivisibleBy3.append(number * 3)

# 3 lines of code above = same as below (below = cleaner code)

# listDivisibleBy3 = [number * 3 for number in range(5)]
# print(listDivisibleBy3)

# -----
# Unpacking dictionaries = used to take out braces away from each key-item value
# -----


# peopleCleveland = {"John": 440_596_9476,
#                    "Terry": 555_555_5555, "Ricky": 314_157_9514}
# peopleCincinnati = {"John": 777_777_7777, "Jerimiah": 222_222_2222}
# combinedBooks = {**peopleCleveland, **peopleCincinnati, "Jacob": 666_666_6666}
# print(combinedBooks)


# -----
# Exercise = develop program that determines most repeated character in a sentence
# -----

# from pprint import pprint
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
# Handling Exceptions = used to create friendly error messages (prevents crashing)
# -----

# try:
#     age = int(input("age: "))
# except ValueError:
#     print("You didn't enter an integer value for your age")
# except ZeroDivisionError:
#     print ("The value cannot be 0.")
# else:
#     print(f"Thanks for saying you are {age} years old!")

# -----
# Constructors = method used when defining a new object
# -----
# class PoundsInches:
#     def __init__(self, weightPounds, heightInches):
#         self.weightPounds = weightPounds
#         self.heightInches = heightInches

#     def WeightHeightStatement(self):
#         print(
#             f"Nick is {self.weightPounds} pounds, and {self.heightInches} inches")


# Nick = PoundsInches(150, 69)
# Nick.WeightHeightStatement()


# -----
# Magic methods = used to modify an object(e.g. into a string)
# -----


# class CalSpice:
#     def __init__(self, calories, spicyness):
#         self.calories = calories
#         self.spicyness = spicyness

#     def __str__(self):
#         return f"({self.calories}, {self.spicyness})"

#     def results(self):
#         print(
#             f"This taco is {self.calories} calories, and rated {self.spicyness} on spicyness scale of 1-10")


# ChickenTaco = CalSpice(400, 3)
# print(str(ChickenTaco))


# -----
# Comparing Objects (def __eq__ = gathered from a magic methods database)
# -----

# class CalSpice:
#     def __init__(self, calories, spicyness):
#         self.calories = calories
#         self.spicyness = spicyness

#     def __eq__(self, other):
#         return self.calories == other.calories and self.spicyness == other.spicyness

# # If you don't include lines 366-367, return = false by default


# ChickenTaco = CalSpice(400, 3)
# BeefBurrito = CalSpice(600, 7)
# print(ChickenTaco == BeefBurrito)

# -----
# Doing arithmetic between objects (e.g. adding, subtracting, etc.)
# -----


# class CalSpice:
#     def __init__(self, calories, spicyness):
#         self.calories = calories
#         self.spicyness = spicyness

#     def __add__(self, other):
#         return CalSpice(self.calories + other.calories, self.spicyness + other.spicyness)


# ChickenTaco = CalSpice(400, 3)
# BeefBurrito = CalSpice(600, 7)
# CombinedCalSpice = ChickenTaco + BeefBurrito
# print(CombinedCalSpice)


# -----
# Making a custom container
# -----

# class HowMuchThisWordIsFound:
#     def __init__(self):
#         self.words = {}

#     # def add(self, word):
#     #     self.words[word.lower] = self.words.get(word.lower, 0) + 1

#     def __setitem__(self, word, count):
#         self.words[word.lower()] = count


# WordSearcher = HowMuchThisWordIsFound()
# WordSearcher["python"] = 10
# # WordSearcher.add("python")
# # WordSearcher.add("Python")
# # WordSearcher.add("python")
# print(WordSearcher.words)


# -----
#
# -----

# class HowMuchThisWordIsFound:
#     def __init__(self):
#         self.words = {}

#     def add(self, word):
#         self.words[word.lower] = self.words.get(word.lower, 0) + 1

#     def __getitem__(self, word):
#         return self.words.get(word.lower(), 0)


# WordSearcher = HowMuchThisWordIsFound()
# WordSearcher.add("Python")
# WordSearcher.add("Python")
# WordSearcher.add("Python")
# print(WordSearcher["python"])
