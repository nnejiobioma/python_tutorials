#Arithemetic Operators
#1. Addition operators (+)
x = 10
y = 20

c = x + y
print("Answer is : ",c)
# output will be Answer is : 30 when you run the file operators_Example using (python operators_Example.py)

#--------------------------------------------------

#2. Subrtraction operators (-)
x = 20
y = 10

c = x - y
print("Answer is : ",c)
# output is Answer 1s : 10

#---------------------------------------------------

#3. Multiplication Operators (x)
x = 10
y = 20

c = x * y
print("Answer is : ",c)
# output is Answer 1s : 200

#---------------------------------------------------

#4. Divition Operators (/)
x = 20
y = 10

c = x / y
print("Answer is : ",c)
# output is Answer 1s : 2.0

#---------------------------------------------------

#5. Floor divition without remainder (//)
x = 200
y = 23

c = x // y
print("Answer is : ",c)
# output is Answer 1s : 2.0

#----------------------------------------------------
#6. Modulo - remmainder after division (%)
x = 200
y = 23

c = x % y
print("Answer is : ",c)
# output is Answer 1s : 16

#-----------------------------------------------------
#7. Exponentiation (**)
x = 200
y = 23

c = x ** y
print("Answer is : ",c)
# output is Answer 1s : 83886080000000000000000000000000000000000000000000000

#-----------------------------------------------------

# COMPARISON OPERATORS:
#1. Equalto (==)
x = 200
y = 23

print(x == y)

# Answer will be False

x = 23
y = 23

print(x == y)

#Answer will be True

#------------------------------------------------------

#2. Not equal to (!=)
x = 23
y = 23

print(x != y)
# Answer will be False because x == y

x = 40
y = 40

print(x == y)
#Answer will be True because x is equal to y
#-----------------------------------------------------
#3. Less than (<)
x = 23
y = 23

print(x < y)
#Answer will be False because x is not less than y, they are equal

x = 22
y = 23

print(x < y)
#Answer will be True because x is less than y.

#------------------------------------------------------
#4. Greater than (>)
x = 24
y = 23

print(x > y)
#Answer will be True because x is greater than y

x = 20
y = 23

print(x == y)
#Answer will be False because x is less than y

#------------------------------------------------------
#5. Less Than or equal to (<=)
x = 23
y = 23

print(x <= y)
#Answer True because is not less than or equal to y

x = 20
y = 23

print(x == y)
#Answer is False

#------------------------------------------------------

#6. Greater than or equal to (>=)

x = 20
y = 23

print(x >= y)
#Answer is False

x = 25
y = 23

print(x >= y)
#Answer True

#-------------------------------------------------------

#LOGICAL OPERATORS
#1. And operators (and)

x = 23
y = 23

print(x>y and x<y)
#Answer False

#-------------------------------------------------------

#2. Not (not)
# Example 1
x = True
print(not x)  # Output: False

# Example 2
y = False
print(not y)  # Output: True

# Example 3
z = 10 > 5
print(not z)  # Output: False, because 10 > 5 is True, so negating it makes it False

#-------------------------------------------------------


#Membership Operators:
# Example 1: Using the 'in' operator
my_list = [1, 2, 3, 4, 5]
print(3 in my_list)  # Output: True, because 3 exists in the list
print(6 in my_list)  # Output: False, because 6 does not exist in the list

# Example 2: Using the 'not in' operator
my_string = "Hello, World!"
print('e' not in my_string)  # Output: False, because 'e' exists in the string
print('z' not in my_string)  # Output: True, because 'z' does not exist in the string

#-------------------------------------------------------

# Identity Operators:
# Example 1: Using the 'is' operator
x = [1, 2, 3]
y = [1, 2, 3]
z = x

print(x is y)  # Output: False, because x and y refer to different objects
print(x is z)  # Output: True, because x and z refer to the same object

# Example 2: Using the 'is not' operator
a = 5
b = 5.0

print(a is not b)  # Output: True, because a and b refer to different objects

