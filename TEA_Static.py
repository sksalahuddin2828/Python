# Way No1: Static
# a=["a","b","c","d","e"]
# f1=["a","b","c"]#it can be input 
# f2=["c","b","e"]#it can be input 
# f3=["d","a","c"]#it can be input 
# f4=["a","d","c"]#it can be input 
# f5=["a","e","d"]#it can be input 
# last_list=f1+f2+f3+f4+f5
# output=[]

# for i in len(a):
#     if last_list.count(a[i])>=3:
#         output.append(a[i])
# print(output)
#===============================================================
# Way No2: dynamic
import math
x=["a","b","c","d","e"]
f1=[] 
f2=[]
f3=[] 
f4=[] 
f5=[]
for i in range(1,16):
    if i<=3:
        a=input("Enter for friend No#1 : ")
        b=a.replace(" ","")
        if b in x:
            f1.append(b)
        else:
            continue
    elif i>3 and i<=6:
        a=input("Enter for friend No#2 : ")
        b=a.replace(" ","")
        f2.append(b)
    elif i>6 and i<=9:
        a=input("Enter for friend No#3 : ")
        b=a.replace(" ","")
        f3.append(b)
    elif i>9 and i<=12:
        a=input("Enter for friend No#4 : ")
        b=a.replace(" ","")
        f4.append(b)
    elif i>12 and i<=15:
        a=input("Enter for friend No#5 : ")
        b=a.replace(" ","")
        f5.append(b)

last_list=f1+f2+f3+f4+f5
output=[]
print(len(last_list)/3)

for i in range(math.floor(len(last_list)/3)):
    print(i)
    print(x[i])
    if last_list.count(x[i])>=3:
        output.append(x[i])
print(output)
