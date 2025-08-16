class Item:
    def __init__(self, name: str, price: int, quantity: int):
        self.name = name
        self.price = price
        self.quantity = quantity

    def __del__(self):
        print(f"clear object: {self}: {self.name}, {self.price}, {self.quantity}")

    def calculate_sum(self):
        total_sum = self.price * self.quantity
        return total_sum


class Fruit(Item):
    def __init__(self, name: str, price: int, quantity: int):
        super().__init__(name, price, quantity)


class Vegtable(Item):
    def __init__(self, name: str, price: int, quantity: int):
        super().__init__(name, price, quantity)


apple = Fruit('Apple', 10, 7)
banana = Fruit('banana', 10, 8)
broccoli = Vegtable('broccoli', 60, 12)
lettuce = Vegtable('lettuce', 50, 10)
jennas_grocery_list = [apple, banana, broccoli, lettuce]

def TotalSum(item_list: list[Item]):
    total_sum = 0

    for item in item_list:
        if isinstance(item, Item):
            total_sum += item.calculate_sum()
            del item
    print('Total Sum:', total_sum)

TotalSum(jennas_grocery_list)
