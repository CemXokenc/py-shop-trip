import json
import math
import os
import datetime

from app.car import Car
from app.customer import Customer
from app.shop import Shop


def shop_trip() -> None:
    config_path = os.path.join(os.path.dirname(__file__), "config.json")
    with open(config_path) as f:
        data = json.load(f)

    fuel_price = data["FUEL_PRICE"]
    customers = [
        Customer(
            customer["name"],
            customer["product_cart"],
            customer["location"],
            customer["money"],
            Car(customer["car"]["brand"], customer["car"]["fuel_consumption"])
        )
        for customer in data["customers"]
    ]
    shops = [
        Shop(
            shop["name"],
            shop["location"],
            shop["products"]
        )
        for shop in data["shops"]
    ]

    for customer in customers:
        print(f"{customer.name} has {customer.money} dollars")
        price = {}

        for shop in shops:
            cost_transport = Car.calculate_fuel_cost(
                [
                    customer.location,
                    shop.location
                ],
                customer.car.fuel_consumption,
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

        if customer.money >= best_price:
            print(f"{customer.name} rides to {best_shop}\n")
            print(f"Date: "
                  f"{datetime.datetime.now().strftime('%d/%m/%Y %H:%M:%S')}")
            print(f"Thanks, {customer.name}, for your purchase!")
            print("You have bought:")

            customer.money -= best_price
            total_products_cost = 0
            selected_shop = next(
                shop
                for shop in shops
                if shop.name == best_shop
            )

            for product, amount in customer.product_cart.items():
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
            print(f"{customer.name} rides home")
            print(f"{customer.name} now has {customer.money} dollars\n")
        else:
            print(f"{customer.name} doesn't have enough "
                  f"money to make a purchase in any shop")


if __name__ == "__main__":
    shop_trip()
