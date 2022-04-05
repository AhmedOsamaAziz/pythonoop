import csv

class Item:
    # Clas Attribute >> can be changed
    pay_rate = 0.8
    all = []

    def __init__(self, name: str, price: float, quantity=0.0):
        # Validations
        assert name and not str.isspace(name), f'Name {name} can\'t be null or whitespace'
        assert price >= 0, f'Price {price} should be greater than or equal to 0'
        assert quantity >= 0, f'quantity {quantity} should be greater than or equal to 0'

        # Assign Values
        self.name = name
        self.price = price
        self.quantity = quantity

        # Actions
        Item.all.append(self)

    def calculate_total_price(self):
        return f'{self.name} coast is {self.quantity * self.price}'

    def apply_discount(self):
        self.price *= self.pay_rate

    # Class method send a reference to the class in the definition
    # Do something that has a relationship with the class, but not something that must be unique per instance
    # To instantiate all objects from DB
    @classmethod
    def get_all_from_csv(cls):
        with open('items.csv', 'r') as f:
            reader = csv.DictReader(f)
            items = list(reader)

        for item in items:
            Item(
                name=item.get('name'),
                price=float(item.get('price')),
                quantity=float(item.get('quantity'))
            )

    # Does not send a reference to class in the function definition
    # Use static when you don't need an instance to work with
    # This should do something that has a relationship with the class
    # but not something that must be unique per instance
    @staticmethod
    def is_integer(num):
        if isinstance(num, float):
            return num.is_integer()
        elif isinstance(num, int):
            return True
        else:
            return False

    def __repr__(self):
        return f"Item('{self.name}', {self.price}, {self.quantity})"


Item.get_all_from_csv()
print(Item.all)
