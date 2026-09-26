n=list(map(int,input("enter numbers seperated by spaces:").split()))
print(n)
l=n[0]
s=n[0]
for i in n: 
    if i>l:
        l=i
    if i<s:
        s=i
        
print("largest",l)
print("smallest",s)
avg=sum(n)/len(n)
print("avg is:",avg)