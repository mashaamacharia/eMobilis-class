#maths functionality
import math
x=99
square_root=math.sqrt(x)
print("The square root is",square_root)
rounded=round(square_root,3)
print("Rounded to 3 decimal places",rounded)
#functions(args)
print("----------------------------")

name="Victor Macharia"
print(len(name))
print(name.lower())
print(name.upper())
print(name.title())
print(name.capitalize())
print("-------------------------------")
post="This thing is fluent"
new_post=post.replace("fluent","flowing")
print(new_post)