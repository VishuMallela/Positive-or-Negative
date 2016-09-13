# In this python program, user enters a number and checked if the number is positive or negative or zero

num = float(input("Enter a number: "))
if num > 0:
   print("The number is positive!")
elif num == 0:
   print("Zero is not classified as positive or negative")
elif num < 0:
   print("The number is negative!")
else:
   print("Illegal Input!")

