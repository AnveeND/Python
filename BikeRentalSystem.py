# Bike Rental system using OOPs concepts :-

"""
- Show total stock how many bikes available
- User can rent bikes
- Accordingly you have to show price for this renting
- per bike 100Rs
"""


class bike:
    def __init__(self, stock):
        self.s = stock

    def show(self):
        print("\nStock Available is : ", self.s, " Bikes")

    def rent(self, qty):
        print('\nkindly pay the rent = Rs. ', qty * 100)
        self.s = self.s - qty

    def condition(self, qty):
        if qty > self.s:
            print("\nStock not available upto ", qty, " Bikes")
            self.show()

        elif qty < self.s:
            self.rent(qty)

        else:
            print("\nEnter a valid number!! ")


obj = bike(1000)
while True:

    print("\n```````````````````` BIKE RENTAL SHOP ``````````````````````\n")
    print("1)Rent Bike\n2)Total stock available\n3)Exit")
    ch = int(input('\nEnter your choice : '))
    if ch == 1:
        n = int(input("\nHow many bikes do you want to rent ? --> "))
        obj.condition(n)

    elif ch == 2:
        obj.show()

    elif ch == 3:
        print("\nThank you !! Visit again .")
        break

    else:
        print("\nEnter a valid choice ")
