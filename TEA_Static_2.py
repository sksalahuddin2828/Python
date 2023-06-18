eange_start=int(input("Range Start"))
eange_end=int(input("Range end"))
a_input=input("")
x=[]
for i in range(int(a_input)):
    x.append(input("a to n"))


p1=[]
p2=[]
p3=[]
p4=[]
p5=[]

output=[] 

for i in range(eange_start,eange_end+1):
    if i<=3:
        p1.append(input("enter for person 1 :"))
    elif i>3 and i<=6:
        p2.append(input("enter for person 2 :"))
    elif i>6 and i<=9:
        p3.append(input("enter for person 3 :"))
    elif i>9 and i<=12:
        p4.append(input("enter for person 4 :"))
    elif i>12 and i<=15:
        p5.append(input("enter for person 5 :"))    
last_list=p1+p2+p3+p4+p5
print(last_list)
print(x)
for i in range(int(a_input)):
    print(i)
    print(x[i])
    if last_list.count(x[i])>=3:
        output.append(x[i])

print(output)
