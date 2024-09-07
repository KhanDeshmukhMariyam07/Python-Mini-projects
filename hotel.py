menu={
    'Pizza':100,
    'Burger':60,
    'Pasta':70,
    'Fries':40,
    'Coffee':80,
    'Momos':80,
    'Soft_Drinks':80,
}
print("*********WELCOME TO PYTHON HOTEL*****************")
print("""-----------Menu------------\n
     NAMES                 PRICES
     Pizza:                Rs-100\n
     Burger:               Rs-60\n
     Pasta:                Rs-70\n
     Fries:                Rs-40\n
     Coffee:               Rs-80\n
     Momos:                Rs-80\n
     Soft_Drinks:          Rs-80
    """)


order_total=0

item_1=input("Enter the name of the item: ")

if item_1 in menu:
    order_total +=menu[item_1]
    print(f"Your item {item_1} has been added to your order")

else:
    print(f"Ordered item {item_1} is not available")

another_order=input("Do you want to add another item(YES/NO): ")

if another_order == "YES":
 item_2=input("Enter the name of second item: ")
 if item_2 in menu:
    order_total +=menu[item_2]
    print(f"Your item {item_2} has been added to your order")
 else:
    print(f"Ordered item {item_2} is not available")

print(f"The total amount of item to pay is {order_total}")


