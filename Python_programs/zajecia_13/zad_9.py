class ShoppingCart():
    def __init__(self):
        self.products = {}

    def add_product(self, name, price):
        self.products[name] = price
        print(f"Dodano do koszyka: {name} - {price} zł")

    def remove_product(self, name):
        if name in self.products:
            del self.products[name] #usuwam coś pod podanym kluczem
            print(f"Usunięto z koszyka: {name}")
        else:
            print(f"Produkt '{name}' nie znajduje się w koszyku.")

    def calculate_total(self):
        return sum(self.products.values())

    def apply_discount(self, percent):
        print(f"Rabat {percent}%")
        factor = 1 - (percent / 100)

        for name in self.products:
            self.products[name] = self.products[name] * factor

    def show_cart(self):
        print("Zawartość koszyka:")
        for name, price in self.products.items():
            print(f"{name}: {price:.2f} zł")

koszyk = ShoppingCart()

koszyk.add_product("Mleko", 4.50)
koszyk.add_product("Chleb", 5.00)
koszyk.add_product("Masło", 8.00)
print(f"Łączna cena: {koszyk.calculate_total():.2f} zł")
koszyk.show_cart()
print()
koszyk.remove_product("Chleb")
print(f"Cena po usunięciu chleba: {koszyk.calculate_total():.2f} zł")
print()
koszyk.apply_discount(20)
koszyk.show_cart()
print(f"Cena po rabacie: {koszyk.calculate_total():.2f} zł")