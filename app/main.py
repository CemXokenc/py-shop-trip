from app.initialisation import initialisation


def shop_trip() -> None:
    fuel_price, customers, shops = initialisation("config.json")

    for customer in customers:
        price = customer.choose_shop(shops, fuel_price)

        best_shop = min(price, key=price.get)
        best_price = price[best_shop]

        if customer.enough_money(best_price):
            customer.buy(best_shop, best_price, shops)
        else:
            customer.not_enough_money()


if __name__ == "__main__":
    shop_trip()
