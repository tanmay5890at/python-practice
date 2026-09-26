import random as r
u=input("rock, paper or scissor:")
comp=r.choice(["rock","paper","scissor"])
print(comp)
if u==comp:
    print("draw")
elif u=="rock" and comp=="paper" or u=="paper" and comp=="scissor" or u=="scissor" and comp=="rock":
    print("comp wins")
else:
    print("user wins")