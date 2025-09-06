#Write a program to create a billing system at supermarket.
while True:
    Name=input("Enter the Nmae of Customer: ")
    Total=0
    while True:
        print("Enter the Amount and Quantity:")
        Amount=float(input("Amount:"))
        Quantity=float(input("Quantity:"))
        Total+=Amount*Quantity
        Repeat=input("Do you want to add more items? (Yes/No) ")
        if Repeat=="no" or Repeat=="NO" or Repeat=="No":
            break
    print("-"*40)
    print("Customer Name: ",Name)
    print("Total Amount: ",Total)
    print("-"*40)
    print("*****************Happy Shopping************")
    Repeat1=input("do you want to add more Customers? (Yes/No)")
    if Repeat1=="no" or Repeat=="NO" or Repeat=="No":
     break