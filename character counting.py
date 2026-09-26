#take input of a sentence and count vowels consonants and total characters
a=input("enter sentence:")
v=0
s=0
c=0
for i in a:
    if i in "aeiou":
        v+=1
    elif i in " ":
        s+=1
    else:
        c+=1
print("vowels are:",v)
print("spaces are:",s)
print("consonants are:",c)
t=v+s+c
print("total character count is:",t)
