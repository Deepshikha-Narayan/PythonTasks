#Write a program that classifies a triangle based on its side lengths.
#Given three input values representing the lengths of the sides, determine if the triangle is equilateral
# (all sides are equal), isosceles (exactly two sides are equal), or scalene (no sides are equal).

l=int(input("Enter lenght"))
b=int(input("Enter breadth"))
h=int(input("Enter height"))

if l==b and l==h:
    print("Its a triangle")
elif l==b or l==h:
    print("Its a isosceles")
else:
    print("Its a scalene")