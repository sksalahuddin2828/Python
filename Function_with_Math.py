def area_of_circle(pai,r):
      return pai*pow(r,2)
def area_of_rectangle(lenth,width):
     return lenth*width
def area_of_triangle(base,height):
     return 0.5*base*height
def area_of_square(a,b):
     return pow(a,2)
Print_list=["area_of_circle","area_of_rectangle","area_of_triangle","area_of_square"]
print(Print_list)
output=int(input("Enter Index Number : "))
A=float(input())
B=float(input())
l=[area_of_circle(A,B),area_of_rectangle(A,B),area_of_triangle(A,B),area_of_square(A,B)][output]
print(l)
