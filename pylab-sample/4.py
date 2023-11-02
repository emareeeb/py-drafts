#Solve a trianles area, given 2 sides and an angle.
a=int(input("enter  the first  side a of triangle"))
b=int(input("enter the second side a of triangle"))
c=int(input("enter the angle including sides"))
import math
c=(c*math.pi)/180
area=0.5*a*b*math.sin(c)
print("The area is",area)
