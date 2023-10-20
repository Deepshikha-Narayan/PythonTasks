#Create a function that checks if a given string is a palindrome

name=str(input("Enter name"))
print(name)

if (name==name[::-1]):
   print("Palindrome string")
else:
   print("Not palindrome string")


