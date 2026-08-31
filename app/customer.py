import datetime

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

    def enough_money(self, amount: int) -> bool:
        return self.money >= amount

    def not_enough_money(self):
        print(f"{self.name} doesn't have enough "
              f"money to make a purchase in any shop")

    def choose_shop(self, shops, fuel_price):
        print(f"{self.name} has {self.money} dollars")
        price = {}

        for shop in shops:
            cost_transport = self.car.calculate_fuel_cost(
                [
                    self.location,
                    shop.location
                ],
                fuel_price
            )
            cost_products = shop.cost_products(self)

            price[shop.name] = round(cost_transport + cost_products, 2)
            print(f"{self.name}'s trip to the "
                  f"{shop.name} costs {price[shop.name]}")

        return price

    def buy(self, best_shop, best_price, shops) -> None:
        print(f"{self.name} rides to {best_shop}\n")
        print(f"Date: "
              f"{datetime.datetime.now().strftime('%d/%m/%Y %H:%M:%S')}")
        print(f"Thanks, {self.name}, for your purchase!")
        print("You have bought:")

        self.pay(best_price)
        total_products_cost = 0
        selected_shop = next(
            shop
            for shop in shops
            if shop.name == best_shop
        )

        for product, amount in self.product_cart.items():
            item_cost = amount * selected_shop.products[product]
            total_products_cost += item_cost
            item_cost_formatted = (
                int(item_cost)
                if item_cost.is_integer()
                else item_cost
            )
            print(f"{amount} {product}s for {item_cost_formatted} dollars")

        print(f"Total cost is {total_products_cost} dollars")
        print("See you again!\n")
        print(f"{self.name} rides home")
        print(f"{self.name} now has {self.money} dollars\n")
