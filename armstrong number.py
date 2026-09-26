n=int(input("enter number"))
a=n
b=0
c=0
f=0
s=0
while(a>0):
    b=a%10
    c=b**3
    a=a//10
    s+=c
print(s)
if n==s:
    print("it is a armstrong number")
else:
    print("not armstrong number")