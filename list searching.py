a=list(map(int,input("enter numbers seperated by space:").split()))
b=int(input("enter number to be searched for:"))
c=0
f=False
for i in a:
    if i==b:
        f=True
    print(i,"exists in list")
    c+=1
print("it occurs",c,"times")
if f==True:
    pass
else:
    print("doesnt exist")
