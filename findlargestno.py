a,b,c = (input("Enter first number: "))
# = (input("Enter second number: "))
#c = (input("Enter third number: "))
if (a > b) and (a > c):
  largest = a
elif (b > a) and (b > c):
  largest = b
else:
  largest = c
print("The largest number is",largest)
