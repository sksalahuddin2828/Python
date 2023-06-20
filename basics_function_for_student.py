def sum(a=10,b=21):
    print(a+b)

sum()
u = int(input("Enter 1st: "))
o = int(input("Enter 2nd: "))
sum(u,o)

x = 20
y = 30
sum(x,y)

p = 100
_ = 20
sum(p,_)

# with return keyword____

def square(x):
    return x*x

s=square(10)
print(s)

def square(x):
    return x*x,x+12

s=square(5)
print(s)
