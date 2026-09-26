n=int(input("enter number"))
count=0
for i in range (1,n+1):
    if n%i==0:
        print(i,"is a factor")
        count+=1
print("count is:",count)

is_prime = True

for i in range(2, n):
    if n % i == 0:
        is_prime = False
        break

if is_prime:
    print("Prime")
else:
    print("Not prime")