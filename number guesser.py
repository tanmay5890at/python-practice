import random as r
s=r.randint(1,100)
count=1
i=0
while (i<s):
    n=int(input("enter number:"))
    if s==n:
        print("correct")
        break
    elif s>n:
        print("low")
    else:
        print("high")
    i+=1
    count+=1
print("guessed in:",count,"times")