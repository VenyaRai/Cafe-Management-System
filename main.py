from datetime import datetime
import random

menu={
    "Pizza": 140,
    "Paneer Burger": 160,
    "Dynamites": 130,
    "Paneer Wrap": 110,
    "Pizza Sandwich": 80
}
orders=[]
total=0
def display_menu():
    print("="*45)
    print("       WELCOME TO OUR CAFE!")
    print("="*45)
    print("\nMENU")
    print("-"*45)
    for item,price in menu.items():
        print(f"{item:<25} Rs.{price}")
    print("-"*45)
def take_orders():
    global total
    while True:
        order= input("\nEnter item name: ").title()
        if order in menu:
            while True:
                try:
                    quantity=int(input("Enter quantity: "))

                    if quantity>0:
                        break
                    else:
                        print("Quantity should be greater than 0.")
                except ValueError:
                    print("Please enter a valid number.")
            price=menu[order]*quantity
            total+=price
            orders.append([order,quantity,price])
            print(f"\n{order} added successfully!")
            print(f"Current Total: Rs.{total}")
        else:
            print("Sory! Item is unavailable.")
            continue
        choice=input("\nDo you want to order more? (Yes/No): ").lower()
        if choice!="yes":
            break
def print_bill():
    bill_no = random.randint(1000, 9999)
    now = datetime.now()
    print("\n")
    print("=" * 55)
    print("               FINAL BILL")
    print("=" * 55)
    print(f"Bill No : {bill_no}")
    print(f"Date    : {now.strftime('%d-%m-%Y')}")
    print(f"Time    : {now.strftime('%I:%M %p')}")
    print("-" * 55)
    print(f"{'Item':<22}{'Qty':<10}{'Price'}")
    print("-" * 55)
    for item, qty, price in orders:
        print(f"{item:<22}{qty:<10}Rs.{price}")
    print("-" * 55)
    print(f"{'TOTAL AMOUNT':<32}Rs.{total}")
    print("=" * 55)
    print("      Thank You! Visit Again ")
    print("=" * 55)
display_menu()
take_orders()
print_bill()


