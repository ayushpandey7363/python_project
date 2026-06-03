
import random
data=["r","p","s"]
# ch=random.choice(data)
attempt=0
while True:
    ch=random.choice(data)
    attempt+=1
    x=input("Enter your choice(rock:r,paper:p,scissors:s):")
    if (ch=="r" and x=="p") or \
       (ch=="p" and x=="s") or \
       (ch=="s" and x=="r"):
        print("computer:",ch)
        print("you win by ",attempt,"attempts(s)")
        break
    elif ch==x:
        print("computr:",ch)
        print("match draw")
    else:
        print("computer:",ch)
        print("you lost")
