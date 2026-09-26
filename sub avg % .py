n=int(input("enter number of subjects"))
a=0
t=0
for i in range (1,n+1):
    a +=int(input(f"enter marks for subject {i}:"))
    max_marks=int(input("enter maximum marks for the subject"))
    t+=max_marks
percentage=(a/t)*100
print ("percentage is:",percentage)

