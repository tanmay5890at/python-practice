b=10000

i=1
while (i<=4):
    print("""       ATM
    1.Check Balance
    2. Deposit
    3. Withdraw
    4. Exit""")
    a=int(input("enter choice:"))
    if a==1:
        print("balance is:",b)
    elif a==2:
        c=int(input("enter amount to be deposited:"))
        b=b+c
        print("deposit successful")
    elif a==3:
        d=int(input("enter amount to be withdrawl:"))
        if d<=b:
            b=b-d
            print("withdrawl successful")
        else:
            print("withdraw not successful")
    elif a==4:
        print("thank you\nFinal Balance",b)
        i+=1
        break
    else:
        print("invalid choice")