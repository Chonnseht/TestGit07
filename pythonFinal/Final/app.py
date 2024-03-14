###Functions and arguments

def FA02(username, amount, due_date):
    print(f"Hello, {username}")
    print(f"Your bill of ${amount: .2f} is due: {due_date}")

def FA03(fname):
    print(fname + " Refsnes")

FA03("Emil")
FA03("Tobias")
FA03("Linus")

def FA04(fname, lname):
  print(fname + " " + lname)

FA04("Emil", "Refsnes")

def FA05(*kids):
  print("The youngest child is " + kids[2]) #*before parameter to receive a tuple of arguments

FA05("Emil", "Tobias", "Linus")

def FA06(child3, child2, child1):
  print("The youngest child is " + child3)

FA06(child1 = "Emil", child2 = "Tobias", child3 = "Linus")

def FA07(**kid):
  print("His last name is " + kid["lname"]) #**before parameter to receive a dictionary of arguments

FA07(fname = "Tobias", lname = "Refsnes")

def FA08(country = "Norway"): #default parameter value
  print("I am from " + country)

FA08("Sweden")
FA08("India")
FA08()
FA08("Brazil")

def FA09(food): #passing a list as argument
  for x in food:
    print(x)

fruits = ["apple", "banana", "cherry"]


FA09(fruits)

###Return
def RT01(x, y):
    z = x + y
    return z
print(RT01(1,2))

def RT02(x,y):
    z = x - y
    return z
print(RT02(1,2))

def RT03(x,y):
    z = x * y
    return z
print(RT03(1,2))

def RT04(x,y):
    z = x / y
    return z
print(RT04(1,2))

def RT05(first, last):
    first = first.capitalize()
    last = last.capitalize()
    return first + " " + last

    full_name = RT05("john", "smith")

    print(full_name)

def RT06(x):
  return 5 * x

print(RT06(3))
print(RT06(5))
print(RT06(9))


###Variables
x = str(3)
y = int(3)
z = float (3)

x = 5
y = "John"
print(type(x)) #Run to   <class 'int'>
print(type(y)) #Run to   <class 'str'>

x, y, z = "Orange", "Banana", "Cherry"
print(x)
print(y)
print(z)

x = y = z = "Orange"
print(x)
print(y)
print(z)

fruits = ["apple", "banana", "cherry"]
x, y, z = fruits
print(x)
print(y)
print(z)

x = "Python"
y = "is"
z = "awesome"
print(x, y, z)

x = "Python "
y = "is "
z = "awesome"
print(x + y + z)
#Global Variable is outside of function
x = "awesome"

def myfunc():
  x = "fantastic"
  print("Python is " + x)

myfunc()

print("Python is " + x) #shows Python is fantasic than Pythan is awesome

x = "awesome"

def myfunc():
  global x
  x = "fantastic" #change global variable from awesome to fantastic

myfunc()

print("Python is " + x)


###Numbers
import random

print(random.randrange(1, 10))


###Casting
x = int(1)   # x will be 1
y = int(2.8) # y will be 2
z = int("3") # z will be 3


###Strings
a = """Lorem ipsum dolor sit amet,
consectetur adipiscing elit,
sed do eiusmod tempor incididunt
ut labore et dolore magna aliqua."""
print(a)

a = "Hello, World!"
print(a[1]) #print e

for x in "banana":
  print(x) #print b a n a n a each line

a = "Hello, World!"
print(len(a))

txt = "The best things in life are free!"
print("free" in txt) #print True
#or
txt = "The best things in life are free!"
if "free" in txt:
  print("Yes, 'free' is present.")

txt = "The best things in life are free!"
if "expensive" not in txt:
  print("No, 'expensive' is NOT present.")

#Slicing
b = "Hello, World!"
print(b[2:5]) #print llo

b = "Hello, World!"
print(b[:5]) #print Hello

b = "Hello, World!"
print(b[2:]) #print llo, World!
#negative indexing
b = "Hello, World!"
print(b[-5:-2]) #print orl

#uppercase and lowercase
a = "Hello, World!"
print(a.upper())

a = "Hello, World!"
print(a.lower())

#remove whitespace
a = " Hello, World! "
print(a.strip()) # returns "Hello, World!"

#Replace string
a = "Hello, World!"
print(a.replace("H", "J"))

a = "Hello, World!"
print(a.split(",")) # returns ['Hello', ' World!']

#string contatenation
a = "Hello"
b = "World"
c = a + " " + b
print(c)

quantity = 3
itemno = 567
price = 49.95
myorder = "I want {} pieces of item {} for {} dollars."
print(myorder.format(quantity, itemno, price))

txt = "We are the so-called \"Vikings\" from the north." # \" is "


###Booleans
#Return True
bool("abc")
bool(123)
bool(["apple", "cherry", "banana"])
#Return False
bool(False)
bool(None)
bool(0)
bool("")
bool(())
bool([])
bool({})

class myclass():
  def __len__(self):
    return 0

myobj = myclass()
print(bool(myobj)) #Return False

def myFunction() :
  return True

if myFunction():
  print("YES!")
else:
  print("NO!") #Return YES!

x = 200
print(isinstance(x, int)) #Return True

###Lists
thislist = ["apple", "banana", "cherry"]
print(len(thislist))

thislist = list(("apple", "banana", "cherry")) # note the double round-brackets
print(thislist)


thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(thislist[:4]) #beginning to orange

thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(thislist[2:]) #cherry to the end

thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(thislist[-4:-1]) #orange kiwi melon

thislist = ["apple", "banana", "cherry"]
if "apple" in thislist:
  print("Yes, 'apple' is in the fruits list")

thislist = ["apple", "banana", "cherry", "orange", "kiwi", "mango"]
thislist[1:3] = ["blackcurrant", "watermelon"]
print(thislist) #Change the values "banana" and "cherry" with the values "blackcurrant" and "watermelon"

thislist = ["apple", "banana", "cherry"]
thislist[1:2] = ["blackcurrant", "watermelon"]
print(thislist) #['apple', 'blackcurrant', 'watermelon', 'cherry']

thislist = ["apple", "banana", "cherry"]
thislist.insert(2, "watermelon")
print(thislist)

thislist = ["apple", "banana", "cherry"]
thislist.append("orange")
print(thislist)

thislist = ["apple", "banana", "cherry"]
thistuple = ("kiwi", "orange")
thislist.extend(thistuple)
print(thislist)

thislist = ["apple", "banana", "cherry", "banana", "kiwi"]
thislist.remove("banana") #only remove the first banana
print(thislist)

thislist = ["apple", "banana", "cherry"]
thislist.pop()
print(thislist) #remove the last item cherry

thislist = ["apple", "banana", "cherry"]
for x in thislist:
  print(x)
#or
thislist = ["apple", "banana", "cherry"]
for i in range(len(thislist)):
  print(thislist[i])

#Condition
newlist = [x for x in fruits if x != "apple"]
#Iterable
newlist = [x for x in range(10)]

newlist = [x for x in range(10) if x < 5]
#Expression
newlist = [x.upper() for x in fruits]

newlist = [x if x != "banana" else "orange" for x in fruits] #Return "orange" instead of "banana"
#Asc
thislist = [100, 50, 65, 82, 23]
thislist.sort() #Sorting will start with capital letters before lower case letters
print(thislist)
#Desc
thislist = [100, 50, 65, 82, 23]
thislist.sort(reverse = True)
print(thislist)

#Sort the list based on how close the number is to 50
def myfunc(n):
  return abs(n - 50) #absolute

thislist = [100, 50, 65, 82, 23]
thislist.sort(key = myfunc)
print(thislist)
#lower capital letter (case-insensitive sort)
thislist = ["banana", "Orange", "Kiwi", "cherry"]
thislist.sort(key = str.lower)
print(thislist)

thislist = ["banana", "Orange", "Kiwi", "cherry"]
thislist.reverse()
print(thislist)

thislist = ["apple", "banana", "cherry"]
mylist = thislist.copy()
print(mylist)

###Tuples
thistuple = ("apple", "banana", "cherry")
if "apple" in thistuple:
  print("Yes, 'apple' is in the fruits tuple")
#change tuple values
x = ("apple", "banana", "cherry")
y = list(x)
y[1] = "kiwi"
x = tuple(y)

print(x)
#Add items do not have append() method there are 2 ways
#Method 1. Convert into a list
thistuple = ("apple", "banana", "cherry")
y = list(thistuple)
y.append("orange")
thistuple = tuple(y)

#Method 2. Add tuple to a tuple
thistuple = ("apple", "banana", "cherry")
y = ("orange",)
thistuple += y

print(thistuple)
#unpacking
fruits = ("apple", "banana", "cherry")

(green, yellow, red) = fruits

print(green)
print(yellow)
print(red)

#Assign the rest of the values as a list called "red" by *
fruits = ("apple", "banana", "cherry", "strawberry", "raspberry")

(green, yellow, *red) = fruits

print(green) #apple
print(yellow) #banana
print(red) #['cherry', 'strawberry', 'raspberry']

fruits = ("apple", "mango", "papaya", "pineapple", "cherry")

(green, *tropic, red) = fruits

print(green) #apple
print(tropic) #['mango', 'papaya', 'pineapple']
print(red) #cherry
#loop through a tuple
thistuple = ("apple", "banana", "cherry")
for x in thistuple:
  print(x)
#loop through the index numbers
thistuple = ("apple", "banana", "cherry")
for i in range(len(thistuple)):
  print(thistuple[i])
#while loop
thistuple = ("apple", "banana", "cherry")
i = 0
while i < len(thistuple):
  print(thistuple[i])
  i = i + 1
#join two tuples #can also multiply by *2 like mytuple = fruits * 2
tuple1 = ("a", "b" , "c")
tuple2 = (1, 2, 3)

tuple3 = tuple1 + tuple2
print(tuple3)

###Sets
thisset = {"apple", "banana", "cherry"}

for x in thisset:
  print(x) #to loop

thisset = {"apple", "banana", "cherry"}

print("banana" in thisset) #True
#add sets
thisset = {"apple", "banana", "cherry"}
tropical = {"pineapple", "mango", "papaya"}

thisset.update(tropical) #can also use .union, both will exclude any duplicate items
# where .itnersection will keep only deplicates
print(thisset)

x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}

x.intersection_update(y) #keep duplicates in current set x

print (x)
#where
x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}

z = x.intersection(y)

print(z) #create a new intersection set z
#oppose (keep all except duplicates) ****True and 1 considered the same value
x = {"apple", "banana", "cherry", True}
y = {"google", 1, "apple", 2}

z = x.symmetric_difference(y)

print(z)

# .add to add item #.remove and .discard is for remove item
#.clear is to empty. .del is to delete set

#***** .pop will remove random item *****

###Dictionaries
x = thisdict.keys() #dict_keys(['brand', 'model', 'year'])

thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
x = thisdict["model"]
#or
x = thisdict.get("model")
#Add new keys
car = {
"brand": "Ford",
"model": "Mustang",
"year": 1964
}

x = car.keys()

print(x) #before the change

car["color"] = "white"

print(x) #after the change

thisdict["year"] = 2018
thisdict.update({"year": 2020})
thisdict.pop("model")
del thisdict["model"]
thisdict.clear()
#Print all key names in the dictionary, one by one
for x in thisdict.keys():
  print(x)
#Print all values in the dictionary, one by one

for x in thisdict.values():
      print(x)
#Loop through both keys and values
for x, y in thisdict.items():
  print(x, y)
#copy
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
mydict = dict(thisdict)
print(mydict)
#Nested Dict
myfamily = {
  "child1" : {
    "name" : "Emil",
    "year" : 2004
  },
  "child2" : {
    "name" : "Tobias",
    "year" : 2007
  },
  "child3" : {
    "name" : "Linus",
    "year" : 2011
  }
}
#------------------------------
child1 = {
  "name" : "Emil",
  "year" : 2004
}
child2 = {
  "name" : "Tobias",
  "year" : 2007
}
child3 = {
  "name" : "Linus",
  "year" : 2011
}

myfamily = {
  "child1" : child1,
  "child2" : child2,
  "child3" : child3
}

print(myfamily)

print(myfamily["child2"]["name"])

###If Else
def IE01():
    a = 200
    b = 33
    if b > a:
        print("b is greater than a")
    elif a == b:
        print("a and b are equal")
    else:
        print("a is greater than b")

    a = 200
    b = 33
    c = 500
    if a > b and c > a:
        print("Both conditions are True")

    a = 200
    b = 33
    c = 500
    if a > b or a > c:
        print("At least one of the conditions is True")

    d = 33
    e = 200
    if not d > e:
        print("a is NOT greater than b")

#Nested If
    x = 41

    if x > 10:
        print("Above ten,")
        if x > 20:
             print("and also above 20!")
        else:
             print("but not above 20.")


###While Loops
def WL01():
    i = 1
    while i < 6:
      #print(i)
      if i == 3:
        break
      i += 1

    i = 0
    while i < 6:
      i += 1
      if i == 3:  #3 is missing in the result
        continue
      #print(i)

    i = 1
    while i < 6:
      #print(i)
      i += 1
    else:
      print("i is no longer less than 6")

thislist = ["apple", "banana", "cherry"]
i = 0
while i < len(thislist):
  print(thislist[i])
  i = i + 1
#or Looping Using List Comprehension
#thislist = ["apple", "banana", "cherry"]
#[print(x) for x in thislist]

#fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
#newlist = []

#for x in fruits:
  #if "a" in x:
    #newlist.append(x)

print(newlist)
#shorten to
fruits = ["apple", "banana", "cherry", "kiwi", "mango"]

newlist = [x for x in fruits if "a" in x]

print(newlist)


###For Loops
def FL01():
    fruits = ["apple", "banana", "cherry"]
    for x in fruits:
      print(x)

    fruits = ["apple", "banana", "cherry"]
    for x in fruits:
        if x == "banana":
            break
        print(x)

    fruits = ["apple", "banana", "cherry"]
    for x in fruits:
        if x == "banana": #do not print banana
            continue
        print(x)

    for x in "banana":
      print(x)

    for x in range(6): #0,1,2,3,4,5
        print(x)
    else:
        print("Finally finished!")

    for x in range(6):
        if x == 3: break
        print(x)
    else:
        print("Finally finished!") ##If the loop breaks, the else block is not executed.

    for x in range(2, 6): #2,3,4,5
        print(x)

    for x in range(2, 30, 3): #+3 from 2 to 30
        print(x)
#Nested Loops
    adj = ["red", "big", "tasty"]
    fruits = ["apple", "banana", "cherry"]

    for x in adj:
      for y in fruits:
        print(x, y)


###Classes/Objects
class MyClass:
  x = 5
p1 = MyClass()
print(p1.x)
#Example with __init__() function
class Person:
  def __init__(self, name, age):
    self.name = name
    self.age = age

p1 = Person("John", 36)
#Example with __str__() function
class Person:
  def __init__(self, name, age):
    self.name = name
    self.age = age

  def __str__(self):
    return f"{self.name}({self.age})"

p1 = Person("John", 36)

print(p1)
#Object methods are functions that belong to the object
class Person:
  def __init__(self, name, age):
    self.name = name
    self.age = age

  def myfunc(self):
    print("Hello my name is " + self.name)

p1 = Person("John", 36)
p1.myfunc()

#The self parameter
class Person:
  def __init__(mysillyobject, name, age):
    mysillyobject.name = name
    mysillyobject.age = age

  def myfunc(abc):
    print("Hello my name is " + abc.name)

p1 = Person("John", 36)
p1.myfunc()

#Modify Object Properties
p1.age = 40
#Delete Object Properties
del p1.age
#Delete Objects
del p1

###Algorithm analysis
import random
from time import time

def find_max1():
    num = 2000000
    i = 0
    my_list = []

    while i < num:
        my_list.append(random.randint(0, 10))
        i += 1

    print(my_list)

    # FIND_MAX1
    max1 = 0
    for x in my_list:
        if x > max1:
            max1 = x

    print('Max is ', max1)

def find_max2():
    num = 2000000
    i = 0
    my_list = []

    while i < num:
        my_list.append(random.randint(0, 10))
        i += 1

    print(my_list)
    max2 = 0
    score_list = [10,9,8,7,6,5,4,3,2,1,0]
    for s in score_list:
        if my_list.count(s) > 0: # s is in the my_list or not
            max2 = s
            break
    print("(2)Max is ", max2)


def run():

    start_time = time()  # record the starting time
    find_max1()
    end_time = time()  # record the ending time
    elapsed_time = end_time - start_time
    print(elapsed_time)

    start_time2 = time()  # record the starting time
    find_max2()
    end_time2 = time()  # record the ending time
    elapsed_time2 = end_time2 - start_time2
    print(elapsed_time2)

###Recursive programming

# range (6) --> [0,1,2,3,4,5]

#range (1,6) --> [1,2,3,4,5]
def Evennums(num):
    print(num)
    if num % 2 != 0:
        print("please enter an even number")
    elif num == 2:
        return num
    else:
        return Evennums(num - 2)

Evennums(8)

def sum1(num): # 1 + 2 + 3 + ... + num
   sum = 0
   # [1, 2 , 3, 4, 5]
   for x in range(1, num+1):
       sum += x
   return sum


def sum2(num):
   if num == 0:
       return 0
   elif num == 1:
       return 1
   else:
       return num + sum2(num - 1)
   # 5 + 4 + 3 + 2 + 1


def factorial(num):
   if num == 0:
       return 1
   elif num == 1:
       return 1
   else:
       return num * factorial(num - 1)
   # 5 * 4 * 3 * 2 * 1
   # A and B
   # A B
   # B A --> 2
   # A B C --> A B C , A C B, B A C, B C A, C A B , C B A --> 6


def run():
   #print(sum1(5)) # 1 + 2 + 3 + 4 + 5 = 15
    #print(sum2(6))
   print(factorial(7))

   str = 'Hello'
   # 0 -> H, 1 -> e, 2 -> l, 3 -> l, 4->o, 5 --> Error

   print(str[5])

class Account:
    def __init__(self,account_name,opening_balance):
        self.account_name = account_name
        self.balance = opening_balance

    def display(self):
        # Balance Inquiry
        return self.account_name + ' ' + f"{self.balance:,.2f}"

    def setAccountName(self, new_name):
        self.account_name = new_name



def run():
    my_list = [10, 20, 30, 'Gun', 'Musket', 40, 11.0, 'Cannon']

    #print (len(my_list))
    size = len(my_list)

    print (my_list[size-1])

    my_num = 1
    my_num = 2

    bank01 = Account('Dhirachat Ch', 5000.00)
    print(bank01.display())
    bank02 = Account('Hello World', 1500.00)
    print(bank02.display())

def tri_recursion(k):
  if(k > 0):
    result = k + tri_recursion(k - 1)
    print(result)
  else:
    result = 0
  return result

print("\n\nRecursion Example Results")
tri_recursion(6)

def get_recursive_factorial(n):
    if n < 0:
        return -1
    elif n < 2:
        return 1
    else:
        return n* get_recursive_factorial(n-1)

print(get_recursive_factorial(6))

#recursive vs iterative
def get_iterative_factorial(n):
    if n < 0:
        return -1
    else:
        fact = 1
        for i in range(1, n+1):
            fact *= i
        return fact

print(get_iterative_factorial(6))



###Exercise
#Count number of vowels

def number_of_vowels(str):
    vowels = ['a','e','i','o','u']
    count = 0

    for x in str:
        if x.lower() in vowels:
            count += 1

    return count

def run03():
    print(number_of_vowels('HELLO WORLD'))

def run04():
    my_date = '4 Jan 2024'
    my_list = my_date.split()

    print(my_list[0])
    print(my_list[1])
    print(my_list[2])

def sum_odds(n):
    my_list = range(1,n+1)
    result = 0
    for x in my_list:
        if (x % 2) == 1:
            result += x
    return result

def run05():
    print(sum_odds(10)) # 1 + 3 + 5 + 7 + 9

# '2 Jan 2024'

def isPrime(n):
   if (n % 1) == 0:
       if n <= 1:
           return False
       else:
           # count number of dividend 1..n that make the remainder = 0
           # prime number has count--> 2
           count = 0
           #rint(n)
           list = range(1, n+1)
           for x in list:
               if ((n % x) == 0):
                   count += 1
           #print(count)
           if count == 2:
               return True
           else:
               return False
   else:
       return False

def run06():
    my_list = [11,12,13,14,15,16,17,18,19,20]
    # sum() excludes prime number
    result = 0

    for x in my_list:
        if isPrime(x):
            print('')
            #Do nothing
        else:
            result += x
    print("Sum() excludes prime is " + str(result))