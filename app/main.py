from app import customer
from app.car import Car

from app.initialisation import initialisation


def shop_trip() -> None:
    fuel_price, customers, shops = initialisation("config.json")

    for customer in customers:
        print(f"{customer.name} has {customer.money} dollars")
        price = {}

        for shop in shops:
            cost_transport = customer.car.calculate_fuel_cost(
                [
                    customer.location,
                    shop.location
                ],
                fuel_price
            )
            cost_products = sum(
                amount
                * shop.products[product]
                for product, amount in customer.product_cart.items()
            )

            price[shop.name] = round(cost_transport + cost_products, 2)
            print(f"{customer.name}'s trip to the "
                  f"{shop.name} costs {price[shop.name]}")

        best_shop = min(price, key=price.get)
        best_price = price[best_shop]

        if customer.enough_money(best_price):
            customer.buy(best_shop, best_price, shops)
        else:
            customer.not_enough_money()


if __name__ == "__main__":
    shop_trip()
