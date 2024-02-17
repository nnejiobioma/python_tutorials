a = 50
b = 20

# if b > a:
#     print("b is greater than a")
# else:
#     print("a is greater than b")

# if a == b:
#     print("both are equle")
# elif a < b:
#     print(" a is greater than b")
# else:
#     print("both equations are wrong")

# a = int(input("what number do I have in mind : "))

# if a == 100:
#     print("The number is not above 100")
# elif a == 50:
#     print("you are close to the number please try again")
# elif a > 50:
#     print("just a little above the number, Please keep trying")
# elif a == 40:
#     print("you are close to the number, raising your expection a little hight will help")
# elif a == 45:
#     print("You have made it. The number is 45")
# else:
#     print("Please keep trying.....")

while True:
   a = int(input("What number do I have in mind: "))

   if a == 100:
       print("The number is not above 100")
   elif a == 50:
       print("You are close to the number, please try again")
   elif a > 50:
       print("Just a little above the number, please keep trying")
   elif a == 40:
       print("You are close to the number, raising your expectation a little higher will help")
   elif a == 45:
       print("You have made it! The number is 45")
       break  # Exit the loop if guessed correctly
   else:
       print("Please keep trying...")