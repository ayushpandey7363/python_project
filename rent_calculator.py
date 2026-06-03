# rent calculator in python - @codeingwithayush

# # we need from user inputs
# total rent
# total food order
# electricity spend
# charge per unit 
# persons living in room/flat

# output
# total amount you've to pay is 

r=int(input("Enter your room/flat rent = "))
f=int(input("Enter your order food = "))
e=int(input("Enter your electricity spend = "))
c=int(input("Enter the charge per unit = "))
p=int (input("Enter the person living in room/flat = "))

total_bill = e*c

output = (f+r+total_bill)//p

print("Each person will pay = ", output)

