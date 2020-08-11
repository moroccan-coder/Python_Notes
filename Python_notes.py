# ------ Variables Type -------- #


print(type(100))
print(type(9.44))
print(type("hello"))
print(type(2 == 4))
print(type([2, 3, 4, 200]))
print(type((21, 44, 3, 5)))
print(type({'one': 1, 'two': 2, 'three': 3}))

# ------------------------- #
# Source Code : Original Code You Write it in Computer
# Translation : Converting Source Code Into Machine Language
# Compilation : Translate Code Before Run Time
# Run-Time : Period App Take To Executing Commands
# Interpreted : Code Translated On The Fly During Execution

# Reserved Words
help("keywords")

# unpack values ------
a, b, c = 1, 20, 33
print(a)
print(b)
print(c)

# ------------------------------------- Escape Sequences Characters ------------------------------------
# \b => Back Space
# \newline => Escape new line + \
# \\ => Escape Back Slash
# \' => Escape Single Quotes
# \" => Escape Double Quotes
# \n => Line Feed
# \r => Carriage Return
# \t => Horizontal Tab
# \xhh => Character Hex Value

# Back Space
print("hello\bworld!")  # will remove o

# Escape new Line + Back Slash
print("hello\
 all\
 the\
 world")

# Escape Back Slash
print("I Love back Slash \\")

# Escape Single Quote
print('I love Single Quote \'TEST\' ')

# Line Feed
print('Hello\nWorld')

# Carriage Return
print("123456\rAbcd")

# Horizontal Tab
print("hello\tPython")

# Character Hex Value
print("\x4E\x76")

# -----------------------------------------End Escape Sequences Characters -----------------------


mystring = "I Love Python"
# Slice
print(mystring[0:3])  # note integrate the end 3
print(mystring[:3])
print(mystring[2:])
print(mystring[:])
# Steps
print(mystring[0::2])
print(mystring[1::2])
print(mystring[::2])
print(mystring[0::])

# ------------------------------------------- String Methods -----------------------------
print("\n#------------------------------------------- String Methods -----------------------------")

# Strip (Remove space or character)
a = '   I Love Python  '
print(a.strip())  # Remove right & left Space
print(a.rstrip())  # Remove Right Space
print(a.lstrip())  # Remove Left Space

a = '####I Love Python#####'
print(a.strip("#"))  # Remove right & left #
print(a.rstrip("#"))  # Remove Right #
print(a.lstrip("#"))  # Remove Left #

a = '###@I Love Python#@####'
print(a.strip("#@"))  # Remove right & left #@
print(a.rstrip("#@"))  # Remove Right #@
print(a.lstrip("#@"))  # Remove Left #@

# title()
a = 'I love 2d graphic and 5g technology'
print(a.title())  # Capitalize First char of words and character after number

# zfill()
a, b, c = "1", "11", "11"
print(a.zfill(3))  # adding Zeros in first of number
print(b.zfill(3))
print(c.zfill(3))

# upper() / lower()
a = "yassine"
b = "Yassine"
print(a.upper())
print(b.lower())

# Splite()
a = "I love python"
print(a.split())
a = "I-love-python and java for android"
print(a.split("-"))
print(a.split("-", 2))

d = "hi-my-name-is-kamal"
print(d.rsplit("-", 2))
print(d.split("-", 2))

# center()
a = "yassine"
print(a.center(11))  # spaces
print(a.center(11, "#"))  # Hashes

# Count()
b = "hi i love Python and php, because python is easy to learn than php"
print(b.count("python"))
print(b.count("php", 0, 30))

# swapcase() : if contain small character change to capitalize and so one
dd = "I love PYthOn"
hh = "I lOve pythOn"
print(dd.swapcase())
print(hh.swapcase())

# startswith()
i = "I love Python"
print(i.startswith("I"))
print(i.startswith("I", 7, 10))  # from index 7 to 10

# endswith()
i = "I love Python"
print(i.endswith("n"))
print(i.endswith("e", 2, 6))  # from index 7 to 10

# index()
a = 'This is python'
print(a.index('n'))
print(a.index('n', 8, 14))
# print(a.index('n', 0, 5)) #show error if not exist

# find()
b = 'we love python'
print(b.find('p'))  # index 8
print(b.find('p', 0, 9))  # index 8
print(b.find('q'))  # index -1

# rjust(width,fill char)   /    ljust(width,fill char)
c = "yassine"
print(c.rjust(20))
print(c.rjust(20, '&'))

print(c.ljust(20))
print(c.ljust(20, '$'))

# splitlines()

d = """hi yassine
this is the
python course"""

print(d.split())
print(type(d.split()))

dd = "how ho\n this is\n python course"
print(dd.splitlines())

# expandtabs()
g = "hello\tworld\tfrom\tpisinj"
print(g.expandtabs())
print(g.expandtabs(20))

# is
worlds = "this is a test"
print(worlds.istitle())
print(worlds.isspace())
print(worlds.islower())
print(worlds.isidentifier())

x = "AaaaaaBbbbb"
y = "AaaaaBbbbb11"
print(x.isalpha())
print(y.isalpha())
print(y.isalnum())

# replace(Old Value,New Value,Count)

axa = "hello man, are you oky man"
print(axa.replace("man", "woman"))
print(axa.replace("man", "woman", 1))

# join(Iterable)
myList = ["yassine", "hassan", "otman", "kamal", "leila", "bhjaouiat"]
print("-".join(myList))
print(" ".join(myList))
print("\n".join(myList))
print(type(", ".join(myList)))

# ---------------------------- String Formatting --------------------------------

# using Placeholder to concatinate strings
name = "yassine"
age = 30
rank = 1

# Old way
print("My Name is : %s" % name)
# new way
print("My Name is : {}".format(name))

# Old way
print("My Name is : %s and my age : %d" % (name, age))
# new way
print("My Name is : {} and my age : {}".format(name, age))

# Old way
print("My Name is : %s and my age : %d and my rank : %f" % (name, age, rank))
# new way
print("My Name is :{:s} and my age : {:d} and my rank : {:f}".format(name, age, rank))

# --> Control Floating Point Number
myNumber = 10
# Old way
print("My Number is: %d" % myNumber)
print("My Number is: %f" % myNumber)
print("My Number is: %.2f" % myNumber)
# new way
print("My Number is: {:d}".format(myNumber))
print("My Number is: {:f}".format(myNumber))
print("My Number is: {:.2f}".format(myNumber))

# --> Truncate String (Slice String)

myLongString = "Hello Coders of Moroccan Coder School I Love you All"
# Old way
print("Message is : %s" % myLongString)
print("Message is : %.12s" % myLongString)  # Only 12 Char
# new way
print("Message is : {:s}".format(myLongString))
print("Message is : {:.12s}".format(myLongString))  # Only 12 Char

# --> Format Money
myMoney = 500000000000  # $
print("My money in Bank is : {:d}$".format(myMoney))
print("My money in Bank is : {:_d}$".format(myMoney))
print("My money in Bank is : {:,d}$".format(myMoney))

# --> Rearrange Items
a, b, c = "One", "Two", "Three"
print("Hello {} {} {}".format(a, b, c))  # Hello One Two Three
print("Hello {1} {0} {2}".format(a, b, c))  # Hello Two One Three

x, y, z = 20, 40, 60
print("Hello {} {} {}".format(x, y, z))
print("Hello {1:d} {0:d} {2:d}".format(x, y, z))  # with variable type
print("Hello {1:.2f} {0:.3f} {2:.20f}".format(x, y, z))  # with variable type

# Format in Version 3.6 +
myName = "yassine"
myAge = 36

print("my name is {myName} and my age is {myAge}")
print(f"my name is {myName} and my age is {myAge}")  # with f formation

# -------------------------------------------- Lists -------------------------------------
myList = ["one", "two", True, 1]

# myList[0] = 1  # Edit the index value to 1
# myList[0:3] = [1, 2, False]   # edit index from 0:3 to 1 2 False
print(myList)

# --> append()
myFriends = ["Kamal", "Hassan", "Issam", "Redwan", "Sadik", "Zakaria"]
myOldFriends = ["mohamed", "brahim", "khalid", "Nourdine"]

myFriends.append("Ms3oud")
myFriends.append(myOldFriends)
print(myFriends)
print(myFriends[7][0])  # first item inside second list inside the first list
# in index 0 of Second list that exist in index 7 of first list

# --> extend()
a = [1, 2, 3, 4]
b = ["A", "B", "C"]
c = ["One", "Two", "Three"]

a.extend(b)
a.extend(c)
print(a)

# --> remove()

x = [1, 2, 5, "yassine", "test", 10, 12]
x.remove("yassine")
print(x)

# --> sort()
numbers = [1, 12, 4, 8, -6, 555]
charcters = ["Z", "A", "X"]
numbers.sort()
charcters.sort()
numbers.sort(reverse=True)
print(numbers)
print(charcters)

# --> reverse()

numbers2 = [1, 12, 4, 8, -6, 555]
numbers2.reverse()  # the last item in list will be in the first an so on
print(numbers2)

# --> clear()
a = [1, 2, 3, 4]
a.clear()
print(a)

# ---------------> copy()
b = [1, 2, 3, 4]
c = b.copy()
print(b)  # Main List
print(c)  # Copied List

# ---------------> count()
d = [1, 2, 3, 4, 1, 10, 11, 23, 1]
print(d.count(1))

# ----------------> index()
e = ["mohamed", "brahim", "khalid", "Nourdine"]
print(e.index("khalid"))

# ----------------> insert()
f = [1, 2, 3, 9, "A", "Z"]
# f.insert(0, "Mourad")
f.insert(-1, "Mourad")
print(f)

# ----------------------------------------------- Tuples --------------------------
tuple1 = ("yassine", "said", "ahmed")
tuple2 = "testt", "saaad"  # we can use tuple without perenteses
print(tuple1)
print(tuple2)
print(type(tuple2))

# ----------------> Tuple Indexing
mytuple = (1, 2, 3, 4, 5)
print(mytuple[0])
print(mytuple[-1])

# ----------> Tuple Assign Value  (imputable)
mytuple = (1, 2, 3, 4, 5)
# mytuple[0] = 1 # Tuple object does not support item assignment
# print(mytuple)

# ----------> Tuple Items
mytuplee = (1, 2, 3, 4, "Test", True, 100.2)
print(mytuplee[-2])

# ----------> Tuple with One element
mytuple1 = ("yassine",)  # add , to indicate that is tuple
mytuple2 = "yassine",  # add , to indicate that is tuple
print(type(mytuple1))
print(type(mytuple2))

# --------> Tuple Concatenation
a = (1, 2, 3, 4)
b = (5, 6)
c = a + b
d = a + ("A", "B", True) + b
print(d)

# -----------> Tuple, List, String Repeat (*)
myString = "yassine "
myList = [1, 2]
myTuple = ("A", "B")

print(myString * 6)
print(myList * 6)
print(myTuple * 6)

# -------> count()
a = (1, 2, 3, 5, 2, 10, 2)
print(a.count(2))

# -------> index()
b = (1, 2, 3, 5, 2, 10, 2)
print(b.index(5))
print("the index of 5 is :{:d}".format(b.index(5)))
print(f"the index of 5 is :{b.index(5)}")

# -------> Destruct
a = ('A', 'B', 'C')
b = ('A', 'B', 4, 'C')
x, y, z = a
xx, yy, _, zz = b  # _ ignored item inside tuple
print(x)
print(y)
print(z)
print(xx)
print(yy)
print(zz)

# ------------------------------------- Set ------------------------------------
# [1] Set Items Are Enclosed in Curly Braces
# [2] Set Items Are Not Ordered And Not Indexed
# [3] Set Indexing and Slicing Cant Be Done
# [4] Set Has Only Immutable Data Type (Numbers, Strings, Tuples) List and Dict Are Not
# [5] Set Items Is Unique

# ------> clear()
a = {1, 2, 3, 4}
a.clear()
print(a)

# ------> union()
b = {"One", "Two", "Three"}
c = {"1", "2", "3"}
x = {"Zero", "Six"}

print(c | b)
print(b.union(c, x))

# -----> add()
d = {1, 2, 3, 4}
d.add(5)
d.add(6)
print(d)

# -------> copy()
e = {1, 2, 3, 4}
f = e.copy()

print(e)
print(f)

e.add(5)

print(f)
print(e)

# -------> remove()
g = {1, 2, 3, 4}
g.remove(1)
# g.remove(9) # show error if item not exist into the set()
print(g)

# --------> discard()
gg = {1, 2, 3, 4}
gg.discard(1)
gg.discard(9)  # don't show any error if the item not exist into the set()
print(gg)

# -------> pop()
i = {"A", "B", 1, 2, 3, 4, 5}
print(i.pop())

# --------> update()
j = {1, 2, 3}
k = {1, "A", "B", 2}
j.update(k)  # add k into j and remove repetitive element
print(j)
j.update(['python', 'javascript'])
print(j)

# ---------> difference()
a = {1, 2, 3, 4}
b = {1, 2, 3, "Osama", "Ahmed"}
print(a)
print(a.difference(b))  # a-b show elements that does not exist in b

# -------> difference_update()
aa = {1, 2, 3, 4}
bb = {1, 2, "Osama", "Ahmed"}  # delete element from aa that exist in bb
print(aa)
aa.difference_update(bb)
print(aa)

# ------> intersection()
aaa = {1, 2, 3, 4, "X"}
bbb = {1, "X", 6}
print(aaa)
print(aaa.intersection(bbb))  # show element that exist in tuple aaa & bbb
print(bbb)

# ------> intersection_update()
aa = {1, 2, 3, 4}
bb = {1, 2, "Osama", "Ahmed"}
print(aaa)
aa.intersection_update(bb)  # update the original tuple aa with the element that exist in two tuples
print(aa)

# ------> symmetric_difference()
aa = {1, 2, 3, 4}
bb = {1, 2, "Osama", "Ahmed"}

print(aa)
print(aa.symmetric_difference(bb))  # show elements that not exist in two tuples
print(aa)

# ------> symmetric_difference_update()
aaa = {1, 2, 3, 4}
bbb = {1, 2, "Osama", "Ahmed"}

print(aaa)
aaa.symmetric_difference_update(bbb)  # update original tuple aa with the elements that not exist in two tuples
print(aaa)

# ------> ussuperset()

a = {1, 2, 3, 4}
b = {1, 2, 3}
c = {1, 2, 3, 4, 5}
print(a.issuperset(b))  # is all items in b exist in a :True
print(a.issuperset(c))  # is all items in c exist in a :False

# -------> issubset()
a = {1, 2, 3, 4}
c = {1, 2, 3}

print(a.issubset(c))  # is all items in a exist in c :False

# ------> isdisjoint()
a = {1, 2, 3, 4}
b = {1, 2, 3}
c = {10, 20, 30}
print(a.isdisjoint(b))  # is any items in b exist in a
print(a.isdisjoint(c))

# ------------------------------------------ Dictionary -------------------------------------
# [1] Dict Items Are Enclosed in Curly Braces
# [2] Dict Items Are Contains Key : Value
# [3] Dict Key Need To Be Immutable (Number, String, Tuple) List Not Allowed
# [4] Dict Value Can Have Any Data Type
# [5] Dict Key Need To Be Unique
# [6] Dict Is Not Ordered You Access Its Element With Key

user = {
    "name": "yassine",
    "age": 30,
    "country": "Morocco",
    "Skills": ["python", "Android", "js"],
    "rating": 9.9,
}
print(user["name"])
print(user.get("age"))
print(user.keys())
print(user.values())

# ------> Two-Dimensional Dictionary (nested Dictionary)

languages = {
    "one": {
        "name": "Python",
        "progress": "99%",
    },
    "two": {
        "name": "Android",
        "progress": "100%",
    },
}

print(languages)
print(languages["one"])
print(languages["one"]["name"])
# dictionary length
print(len(languages))
print(len(languages["one"]))

# ------> Dictionary from Variables
frameworkOne = {
    "name": "Android",
    "progress": "100%",
}

frameworkTwo = {
    "name": "Python",
    "progress": "99%",
}

allFrameWork = {
    "one": frameworkOne,
    "tow": frameworkTwo,
}

print(allFrameWork)

# ---------> clear()
user = {
    "name": "yassine"
}

print(user)
user.clear()
print(user)

# -------------> update()
member = {
    "name": "yassine",
}

print(member)
member["age"] = 30
print(member)
member.update({"country": "Morocco"})
print(member)

# --------> copy()
main = {
    "name": "yassine"
}
b = main.copy()
print(b)
main.update({"skills": "Thinking"})
print(main)
print(b)

# -------> keys() \ values()
print(main.keys())
print(main.values())

# -------> setdefault()
user = {
    "name": "yassine"
}

print(user)
user.setdefault("age", 30)
print(user)

# -------> popitem()

number = {
    "name": "yassine",
    "skill": "thinking",
}

print(number)
member.update({"age": 30})
print(member.popitem())  # print last item added into Dictionary

# ------> items()
view = {
    "name": "Yassine",
    "skill": "Thinking",
}

allitems = view.items()  # keep every item in dictionary and also the next items that added to dictionary
print(view)
view["age"] = 30
print(allitems)  # allitems show us all items inside dictionary and also the items that added after

# ---------> fromkeys()
a = ('keyOne', 'KeyTwo', 'KeyThree')
b = "X"
print(dict.fromkeys(a, b))  # create Dictionary using keys and values above

# ------------------------------------------- Boolean ---------------------------------
print(100 > 200)

# ------> True Values
print(bool("yassine"))
print(bool(100))
print(bool(100.90))
print(bool(True))
print(bool([1, 2, 3, 4, 5]))

# ------> False Values
print(bool(0))
print(bool(""))
print(bool(''))
print(bool([]))
print(bool(()))
print(bool({}))
print(bool(False))
print(bool(None))

# ------> Operators
age = 30
country = "morocco"
rank = 9.99

print(age > 20 and country == "morocco")  # and
print(age < 30 or country == "morocco")  # or
print(not age > 20)  # not

# --------------------------------- Type Conversion ----------------------

a = 10
print(str(a))

# -----> Tuple() Conversion
c = "yassine"  # String
d = [1, 2, 3, 4, 5, 6]  # List
e = {"A", "B", "C"}  # Set
f = {"a": 1, "b": 2}  # Dictionary

print(tuple(c))
print(tuple(d))
print(tuple(e))
print(tuple(f))

# -----> List() Conversion
c = "yassine"  # String
d = [1, 2, 3, 4, 5, 6]  # Tuple
e = {"A", "B", "C"}  # Set
f = {"a": 1, "b": 2}  # Dictionary

print(list(c))
print(list(d))
print(list(e))
print(list(f))

# -----> Set() Conversion
c = "yassine"  # String
d = [1, 2, 3, 4, 5, 6]  # List
e = ("A", "B", "C")  # Tuple
f = {"a": 1, "b": 2}  # Dictionary

print(set(c))
print(set(d))
print(set(e))
print(set(f))

# ------------> Dict() Conversion (Need keys and values (not allow Strings & Set(inhashuble) ))
d = (("A", 1), ("B", 2), ("C", 3), ("D", 4))  # Tuple (to convert tuple to dict we need nested tuples inside tuple)
e = [["One", 1], ["Two", 2], ["Three", 3]]  # List (to convert List to dict we need nested Lists inside List)

print(dict(d))
print(dict(e))

# ----------------------------------------------- User Input --------------------------

# fName = input("First Name:")
# mName = input("Middle Name:")
# lName = input("Last Name:")
# # Chained Methods (method after method)
# fName = fName.strip().capitalize()  # (remove space start/end + Capitalize First Char
# mName = mName.strip().capitalize()
# lName = lName.strip().capitalize()
#
# print(f"Welcome {fName} {mName:.1s} {lName} Happy to see you!")

# ----------------------------------------- Practical Slice Email --------------------

# theName = input('what\'s your name :').strip().capitalize()
# theEmail = input('what\'s your email :').strip()
#
# theUsername = theEmail[0:theEmail.index("@")]
# theWebsite = theEmail[theEmail.index("@") + 1:]
#
# print(f"Hello {theName} your username is {theUsername} \nAnd your Domain is {theWebsite} ")

# --------------------------------------- Practical your age full Details --------------
# age = int(input('What \'s your age ?').strip())
#
# months = age * 12
# weeks = months * 4
# days = age * 365
# hours = days * 24
# minutes = hours * 60
# seconds = minutes * 60
#
# print("You Lived For :")
# print(f"{months} Months.")
# print(f"{weeks:,} Weeks.")
# print(f"{days:,} days.")
# print(f"{hours:,} hours.")
# print(f"{minutes:,} minutes.")
# print(f"{seconds:,} seconds.")


# -------------------------------------------- If Condition ------------------------
country = "B"

if country == "A":
    print(f"welcome from country {country}")
elif country == "B":
    print(f"Welcome from Country {country}")

# ------------------> short condition
movieRate = 18
age = 18
print("Movie is not good for you" if age < movieRate else "Movie is Good for you")

# ------------------------------------- MemberShip Operators ---------------

# ------> String
name = "yassine"
print("s" in name)
print("Y" in name)
print("e" in name)

# --------> List
friends = ["zakaria", "kamal", "hassan"]
print("zakaria" in friends)
print("abdellah" not in friends)
print("kamal" not in friends)

# --------> Using "in" and "not in" With Condition

countrys = ["morocco", "Algeria", "saudi arabia", "bahrain", "dubai"]
myCountry = "morocco"
if myCountry in countrys:
    print(f"Hello {myCountry} Welcome Home")

# --------------> Practical Membership Control
# admins = ["Yassine", "Zakaria", "Hassan", "Kamal"]
# name = input("Please type your name ").strip().capitalize()
#
# if name in admins:
#     admin_option = input(f"Welcome {name}, Choose Update or Delete:").strip().capitalize()
#     if admin_option == "Update" or admin_option == "U":
#         admin_update = input("Please type new name : ").strip().capitalize()
#         admins[admins.index(name)] = admin_update
#         print(admins)
#
#     elif admin_option == "Delete" or admin_option == "D":
#         admins.remove(name)
#         print(admins)
#
#     else:
#         print("Command not exist!")
#
# else:
#     print("you are not admin")
#     yes_no = input("do you want to add you as admin? Yes or No").strip().capitalize()
#     if yes_no == "Yes":
#         admins.append(name)
#         print(admins)
#     elif yes_no == "No":
#         print("No Action Saved")
#     else:
#         print("Command not Exist!")


# -------------------------------------------- Loop --------------------------
# -------> while loop
# mainPassword = "htr"
# inputPassword = input("Write Your password:")
# tries = 5
# while inputPassword != mainPassword:
#     tries -= 1
#     print(f"Wrong Password,{'Last' if tries == 0 else tries} Chance Left")
#     inputPassword = input("Write Your password:")
#     if tries == 0:
#         print("All Tries Is Finished")
#         break
# else:  # this else related to while, execute when while is False (inputPassword == mainPassword)
#     print("Correct Password")

# --------------> For Loop
# Ex1
myNumbers = [1, 2, 3, 4, 6, 70, 5, 90, 66, 435]

for number in myNumbers:
    if number % 2 == 0:
        print(f"The Number {number} Is Even.")
    else:
        print(f"The Number {number} Is Odd.")
else:
    print("The Loop Is Finished")

# Ex2
myName = "yassine"
for letter in myName:
    print(f"[{letter.upper()}]")

# Ex3
myRange = range(1, 100)
for number in myRange:
    print(number)

# ---------> Loop Using Dictionary

mySkills = {
    "Html": "90%",
    "Css": "69%",
    "Php": "70%",
    "Js": "80%",
    "Python": "99%"
}

for skill in mySkills:
    print(f"My Progress in {skill} is : {mySkills[skill]}")

# ----------> Nested For Loop

peoples = {
    "yassine": {
        "html": "80%",
        "Js": "70%",
        "Python": "99%",
    },
    "Hassan": {
        "html": "40%",
        "Js": "30%",
        "Python": "50%",
    },
    "Otman": {
        "html": "10%",
        "Js": "40%",
        "Python": "30%",
    },
}

for developer in peoples:
    print(f"Skills For {developer} is :")
    for skill in peoples[developer]:
        print(f"{skill} ==> {peoples[developer][skill]}")

# --------> Continue
myNumbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 19, 11, 12]
for number in myNumbers:
    if number == 6:
        continue
    print(number)

# --------> Break
print("#" * 50)
for numb in myNumbers:
    if numb == 5:
        break
    print(numb)

#  Pass :  (We using pass if condition or block is empty)

# --------> Loop Advanced Dictionary
# Simple Dict
mySkills = {
    "Python": "99%",
    "Html": "80%",
    "Js": "54%",
}

for skill_key, skill_value in mySkills.items():
    print(f'{skill_key} ==> {skill_value}')

# Nested Dict
myUltimateSkills = {
    "Html": {
        "Main": "90%",
        "PugJs": "10%",
    },
    "Css": {
        "Main": "23%",
        "Saas": "20%",
    }
}

for Main_key, Main_value in myUltimateSkills.items():
    print(f"{Main_key} Progress Is :")
    for skill_key, skill_value in Main_value.items():
        print(f"{skill_key.upper()} ==> {skill_value}")


# ------------------------------------------- Function ---------------------------
def myFunct():
    print("Welcome Function!")


myFunct()

# -------> Function Parameters & Arguments
print("yess", "yeyye", "uuue")


# ----------> Function Packing,Unpacking Arguments

# myList = [1, 2, 3, 4, 5, 6]
# print(*myList) #Unpacking List

# ----> Function Packing / unpacking Arguments

def say_hello(*peoples):  # We use function Packing when we don't know the numbers of argument that we want to passe
    for name in peoples:
        print(f"Hello {name}")


say_hello("said", "ahmed", "brahim", "khalid")


# Ex2
def user_skills(name, *skills):
    print(f"Hello {name} your Skills is : ")
    for skill in skills:
        print(f"{skill}")


user_skills("yassine", "Python", "Js", "Css", "Php")


# -------> Function Default Parameters

def say_hi(name, age, country="unkozn"):
    print(f"Hello {name} Your Age is {age} and your country is : {country}")


say_hi("yassine", 30, "morocco")
say_hi("rebica", 28)


# ----> Packing unpacking keyword Arguments

def show_skills(**skills):
    print(type(skills))

    for skill, value in skills.items():
        print(f"{skill} ==> {value}")


show_skills(html="80%", Css="90%", Python="99%")  # unpacked Dict (key value)

# Ex2 send dict az argument

countrys_users = {
    "yassine": "morocco",
    "saaous": "Arabia Saudi",
    "Jaklin": "Uk",
    "Souzanz": "Usa"
}


def show_country(**users):
    for user, country in users.items():
        print(f"{user.capitalize()} From {country}")


show_country(**countrys_users)  # unpacked our dic country_users

# Ex3
myTuple = ("HTML", "CSS", "JS")
mySkilss = {
    "NodJs": "50%",
    "Python": "45%",
    "MySql": "33%"
}


def show_Skills(name, *skills, **SkillsWithProgress):
    print(f"Hello {name} your Skills is :")
    for skill in skills:
        print(f"- {skill}")

    print("Your Skills With Progress Is :")
    for skill_key, skill_value in SkillsWithProgress.items():
        print(f"[{skill_key}] : {skill_value}")


show_Skills("yassine", *myTuple, **mySkills)

# --------------> Function Scope (global Scope)

x = 1  # Global Scope


def one():
    global x  # Add x to global scope and use it from any place into the class
    x = 10  # Ovrride the global scope x value


one()
print(x)

# --------> Lambda Function (Anonymous Function)
# [1] It Has no name
# [2] you can call it inline without Defining it
# [3] you can use it in return data frim another function
# [4] lambda used for simple functions
# [5] lambda is one single expression not block of code
# [6] lambda type is function

holla = lambda name, age: f"Hi {name} your age is {age}"

print(holla("yassine", 30))

print(holla.__name__)
print(type(holla))

# ------------------------------------------ File Handling ------------------------------------

# "a" Append = Open File For Appending Values, Create File If Not Exists
# "r" Read = [Default Value] Open File For Read And Give Error if File is Not Exists
# "w" Write = Open File For Writing, Create File If Not Exists
# "x" Create = Create File, Give Error If File Exists

# import os

# print(os.getcwd())  # Current Working Directory
# print(os.path.abspath(__file__))  # Return the Absolute File(Working File) Path
# print(os.path.dirname(os.path.abspath(__file__)))  # return the Directory Name of Current File
# file = open("yassine.txt")
# file = open(r"C:\Users\hssn\PycharmProjects\nfile\yassine.txt") # Adding "r" (row String) in the begain of our
# link string path To avoid  Escape "\nfile"


# ---------------------------> Read File

# myFile = open("yassine.txt", "r")
# print(myFile)  # File Data Object
# print(myFile.name)
# print(myFile.mode)
# print(myFile.encoding)

# ---------------

# print(myFile.read(5))
# print(myFile.readline())
# print(myFile.readline(5))

# --------------

# print(myFile.readlines(10))
# print(myFile.readlines())
# print(type(myFile.readlines()))

# ---------------

# for line in myFile:
#     print(line)
#     if line.startswith("Mas"):
#         break
#
# # Close the File
# myFile.close()

# -----------------------------> Write and Append In File

# myFile = open("yassine2.txt","w") # if the file not exist , create file
# myFile.write("Hello\n")
# myFile.write("yassine")

# ------------

# myFile = open("yassine3.txt", "w")
# myFile.write("Morrocan Coders\n" * 200)

# ------------

# myList = ["yassine\n", "Saad\n", "Khalid"]
# myFile = open("file1.txt", "w")
# myFile.writelines(myList)

# ------------ Append "a"

# myFile = open("file1.txt", "a")
# myFile.write("this is test of append Line\n")

# ------------

# myFile = open("file1.txt", "a")
# myFile.truncate(7) # Cut 5 Char From all the file and delete Other

# ------------

# myfile = open("file1.txt", "a")
# print(myfile.tell()) # tell us the position of the cursor

# -----------
# myfile = open("file1.txt", "r")
# myfile.seek(4)  # move cursor to the position 4 and read
# print(myfile.read())

# ---------
# import os
# os.remove("test.txt") # Remove File

# ---------------------------------------- Built in Functions-------------------------------------------

# -----> bin() - show number in binary
print(bin(30))

# ------> id() - id of variable in memory
a = "yassinee"
print(id(a))

# --------> sum()
a = [1, 2, 34, 10]
print(sum(a))  # call sum of all number in list
print(sum(a, 53))  # start sum from 53 and add all list number to 53

# ---------> round(number,numofdigits)
print(round(50.510))
print(round(10.176, 2))

# --------- > range(start,end,step)
print(list(range(0)))
print(list(range(10)))
print(list(range(0, 10, 2)))

# ----------> print()
print("hello yassine from usa")
print("hello", "yassine", "from", "Uk", sep="|")

# -------
print("First Line", end="|")  # the end of print by default end with "\n" , we can change it
print("Second Line")

# ----------> abs() - Return positive number
print(abs(100))
print(abs(-100))
print(abs(-10.9))

# ----------> pow(base,exp,mod)
print(pow(2, 5))  # 2*2*2*2*2
print(pow(2, 5, 10))  # (2*2*2*2*2) % 10

# ----------> min(item,item,or iterator) / max(item,item,or iterator)
myNumb = (10, 1, -6, 35, 9)
print(min(1, 10, 23, 44, -3))
print(max(1, 10, 23, 44, -3))
print(min("A", "Saad", "yassine", "nour"))
print(max(myNumb))

# --------> slice(start,end,step)
a = ["A", "B", "C", "E", "CC"]
print(a[:4])
print(a[slice(3)])
print(a[slice(1, 5, 2)])


# -----------> map
# [1] Map Take a Function + Iterator
# [2] Map Called Map Because It Map The Function On Every Element
# [3] The Function Can Be Pre-Defined Function Or Lambda Function

# Use Map With Predefined Function
def formattext(textt):
    return f"- {textt} -"


myTexts = ["Yassine", "Ahmed", "Said"]
myFormateData = map(formattext, myTexts)

for name in myFormateData:
    print(name)

# Use Map With Lambda Function

myTexts = ["Yassine", "Ahmed", "Said"]
myFormateData = map(lambda text: f"- {text} -", myTexts)

for name in myFormateData:
    print(name)


# -------------> Filters
# Use Map With Predefined Function
def checkNumber(num):
    return num > 10


myNumbers = [1, 22, 90, 32, 5]
myResults = filter(checkNumber, myNumbers)

for numbr in myResults:
    print(numbr)


# EX2
def chekName(name):
    return name.startswith("y")


myTexts = ["yassine", "Saud", "youness", "ahmed", "yasmin"]
myReturnedData = filter(chekName, myTexts)
for name in myReturnedData:
    print(name)

# Use Map With Lambda Function

myTexts = ["yassine", "Saud", "youness", "ahmed", "yasmin"]
myReturnedData = filter(lambda name: name.startswith("a"), myTexts)
for name in myReturnedData:
    print(name)


# ----------> reduce()
def sumAll(num1, num2):
    return num1 + num2


from functools import reduce

numbrs = [1, 8, 99, 10]
result = reduce(sumAll, numbrs)  # (((1+8)+99)+10)
print(result)

# ------> enumerate(iterable,start=0)
mySkills = ["Html", "Css", "Js", "Php"]
mySkilsWithCounter = enumerate(mySkills, 5)  # add counter from 5 to my list item
print(type(mySkilsWithCounter))

# for skil in mySkilsWithCounter:
#     print(skil)

for count, skil in mySkilsWithCounter:  # Custom counter enumarate
    print(f"{count} - {skil}")

# ----------> help()
print(help(sum))

# -------> reversed(iterable)
myString = "yassine"

for leter in reversed(myString):
    print(leter)

# Ex2

skool = ["html", "css", "javs"]

for skkil in reversed(skool):
    print(skkil)

# ------------------------------------ Built in Module ----------------------------
# [1] Module is A File Contain a Set of Functions
# [3] You Can Import Module in Your App To Help You
# [4] you can Import multiple module
# [5] you can create your own modules
# [6] modules saves your time


# import random
#
# print(random)
# print(f"random float number {random.random()}")

# -------> Show all functions inside module
# import random
# print(dir(random))

# ------->Import one or two functions from module
# from random import randint, random
#
# print(f"Print Random Float {random()}")
# print(f"Print Random Integer {randint(1, 9)}")


# -----------> Create my own Module
# import codingHelp
#
# codingHelp.sayMyname("yassine")
# codingHelp.fromCountry()

# alias module name
# import codingHelp as cod  # "as alias_name"
#
# cod.sayMyname("yassine")
# cod.fromCountry()

# import function from module
# from codingHelp import sayMyname as nm
# nm("yassine")


# ----------------------------> Install External Package ------------------------
# [1] Module : is single file contains functions - Package : contain many modules
# [2] External Packages Download From Internet
# [3] you can install package with python package manager PIP
# [4] PIP install the package and it Dependencies (related files)
# [5] Modules List "https://docs.python.org/3/py-modinedex.html"
# [6] package and Modules Directory "https://pypi.org"
# [7] PIP install manual "https://pip.pypa.io/en/stable/reference/pip_install/"
# -------------------------------------------------------------------------------

# ----> update package or module
# pip install pip __update

# -------> print my name with figlet format (need to install pyfiglet module)
# import pyfiglet
# print(pyfiglet.figlet_format("CODING HELP"))

# ------------------------------------------------- Date and Time -----------------------------------
import datetime

# -------> Current Date and time
print(datetime.datetime.now())

# Current Year
print(datetime.datetime.now().year)

# Current Month
print(datetime.datetime.now().month)

# Current Day
print(datetime.datetime.now().day)

# --------> Current time
print(datetime.datetime.now().time())

# Current Hour
print(datetime.datetime.now().time().hour)

# Current Minute
print(datetime.datetime.now().time().minute)

# Current Second
print(datetime.datetime.now().time().second)

# ---------------> Print Specific Date
print(datetime.datetime(1990, 8, 9))
print(datetime.datetime(1990, 8, 9, 4, 45, 19))

# ---------------> difference between two date
myBirthDay = datetime.datetime(1990, 8, 9)
dateNow = datetime.datetime.now()
print(f"My Birth Day is :{myBirthDay} and ", end="")
print(f"Date now is {dateNow}")

print(f"I lived for : {dateNow - myBirthDay}")
print(f"I lived for : {(dateNow - myBirthDay).days} Days.")

# ---------------> Format Date "https://strftime.org/"

myBirthDay = datetime.datetime(1990, 8, 9)
print(myBirthDay.strftime("%a"))
print(myBirthDay.strftime("%A"))
print(myBirthDay.strftime("%b"))
print(myBirthDay.strftime("%B"))

print(myBirthDay.strftime("%d %B %Y"))
print(myBirthDay.strftime("%d/%B/%Y"))
