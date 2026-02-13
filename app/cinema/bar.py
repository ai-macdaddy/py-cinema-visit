class CinemaBar:


    bar_sells = {}

    @staticmethod
    def sell_product(customer: Customer, product: str) -> str:
        CinemaBar.bar_sells[customer] = product
        return f"Cinema bar sold {product} to {customer}."
