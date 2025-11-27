print("Welcome to Ayesha Supermarket")
menu = {
    "Rice": 50,
    "Sugar": 20,
    "Milk": 40,
    "Bread": 30,
    "Eggs": 60,
    "Oil": 120,
    "Butter": 90,
    "Cheese": 150,
    "Apple": 100,
    "Banana": 40,
    "Juice": 80,
    "Soap": 35,
    "Shampoo": 130,
    "Toothpaste": 70,
    "Biscuits": 25
}
for item,price in menu.items():
    print(f"{item:10} - ₹{price}/kg")

print("Type 'Done' when you finish!")

cart={}
total=0

#taking user input for items
while True:
    item_name=input("Enter item name: ").capitalize()
    if item_name=="Done":
        break
    elif item_name in menu:
        qty=int(input(f"Enter quantity of {item_name}: "))
        cart[item_name]=cart.get(item_name,0)+qty
    else:
        print("Item not found choose from the list")

#print(cart)


print(f"{'='*15}BILL{'='*15}")
print(f"{'Items':10} {"Qty":>5}{"Price":>10}{"Total":>10}")
print(f"{'-'*35}")
#Bill generator
for item,price in cart.items():
    price=menu[item]
    item_total=price*qty
    total+=item_total
    print(f"{item:10}{qty:>5}{price:>10}{item_total:>10}")

print(f"{'-'*35}")
print(f"{"Grand Total":>25} = ₹{total}")


print(f"{'='*35}")
print("Thank you for shopping! visit again!")
