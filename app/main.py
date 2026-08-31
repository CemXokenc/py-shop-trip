import datetime

from app.car import Car

from app.initialisation import initialisation


def shop_trip() -> None:
    fuel_price, customers, shops = initialisation("config.json")

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

            customer.pay(best_price)
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
            print(customer.not_enough_money())


if __name__ == "__main__":
    shop_trip()
