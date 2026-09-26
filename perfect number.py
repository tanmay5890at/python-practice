n=int(input("enter number"))
a=0
s=0
while(n>a):
    a+=1
    if n%a==0:
        print(a)
        s=(s+a)
s-=n
print("sum of digits is",s)
if s==n:
    print("perfect number")
else:
    print("not a perfect number")

