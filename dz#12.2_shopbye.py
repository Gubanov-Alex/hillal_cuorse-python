class Item:
    """Product Class"""

    def __init__(self, name, price, description, dimensions):
        self.price = price
        self.description = description
        self.dimensions = dimensions
        self.name = name

    def __str__(self):
        """Information about product"""
        return f"{self.name}, price: {self.price}"

class User:

    def __init__(self, name, surname, numberphone):
        self.name = name
        self.surname = surname
        self.numberphone = numberphone

    def __str__(self):
        """Information about user"""
        return f"{self.name} {self.surname}"

class Purchase:
    """Purchase Class"""
    def __init__(self, user):
        self.products = {}
        self.user = user
        self.total = 0

    def add_item(self, item, cnt=1):
        """Add item to cart"""
        if cnt <= 0:
            raise ValueError("Украл,выпил,в тюрьму")
        if item in self.products:
            self.products[item] += cnt
        else:
            self.products[item] = cnt


    def remove_item(self, item, cnt=1):
        """Delete item from cart"""
        if item in self.products:
            if self.products[item] > cnt:
                self.products[item] -= cnt
            else:
                del self.products[item]
        else:
            raise ValueError(f"Нету {item} тута).")

    def __str__(self):
        """Information about cart"""
        products_str = "\n".join(f"{item.name}: {cnt} pcs." for item, cnt in self.products.items())
        return f"User: {self.user}\nItems:\n{products_str}"

    def get_total(self):
        """Price for all products in cart"""
        return sum(item.price * cnt for item, cnt in self.products.items())

lemon = Item(
             'lemon',
             5,
             "yellow",
             "small",
)
apple = Item(
            'apple',
            2,
            "red",
            "middle",
)
print(lemon)  # lemon, price: 5

buyer = User(
            "Ivan",
            "Ivanov",
            "02628162"
)
print(buyer)  # Ivan Ivanov

cart = Purchase(buyer)
cart.add_item(lemon, 4)
cart.add_item(apple, 20)
print(cart)
"""
User: Ivan Ivanov
Items:
lemon: 4 pcs.
apple: 20 pcs.
"""
assert isinstance(cart.user, User) is True, 'Екземпляр класу User'
assert cart.get_total() == 60, "Всього 60"
assert cart.get_total() == 60, 'Повинно залишатися 60!'
cart.add_item(apple, 20)
print(cart)

cart.remove_item(lemon, 2)
print(cart)
"""
User: Ivan Ivanov
Items:
lemon: 2 pcs.
apple: 40 pcs.
"""

print (cart.get_total())
assert cart.get_total() == 90

