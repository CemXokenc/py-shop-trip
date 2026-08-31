from app.car import Car


class Customer:
    def __init__(
            self,
            name: str,
            product_cart: dict[str, int],
            location: list[int],
            money: int,
            car: Car
    ) -> None:
        self.name = name
        self.product_cart = product_cart
        self.location = location
        self.money = money
        self.car = car

    def pay(self, amount: int) -> None:
        self.money -= amount

    def enough_money(self):
        pass

    def not_enough_money(self):
        return (f"{self.name} doesn't have enough "
                f"money to make a purchase in any shop")
