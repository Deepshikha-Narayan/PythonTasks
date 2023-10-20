#Create a function that checks if a given string is a palindrome
#For negative indexing, to display the 1st element to last element in steps of 1 in reverse order,
# we use the [::-1]. The [::-1] reverses the order

name=str(input("Enter name"))
print(name)

if (name==name[::-1]):
   print("Palindrome string")
else:
   print("Not palindrome string")


