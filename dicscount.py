from abc import ABC, abstractmethod

class Product:
    
    def __init__(self, name, price, category):
        self.name = name
        self.price = price
        self.category = category

class Cart:
    
    def __init__(self):
        self.products = []

    def add_product(self, product: Product):
        self.products.append(product)

    def subtotal(self) -> float:
        return sum(p.price for p in self.products)
    
class Discount:
    @abstractmethod
    def apply(self):
        pass

class CategoryDiscount(Discount):
    def __init__(self, category, persent):
        self.category = category
        self.persent = persent

    def apply(self, cart: Cart, current_total):
        total = current_total
        products = cart.products
        for i in products:
            if i.category == self.category:
                total -= i.price
                total += (1.0 - self.persent/100) * i.price
        return total
    
class FixedDiscount(Discount):
    def __init__(self, amount, min_amount):
        self.amount = amount
        self.min_amount = min_amount

    def apply(self, cart: Cart, current_total):
        
        if current_total >= self.min_amount:
            return current_total - self.amount
        else:
            return current_total
    
class DiscountEngine:
    def __init__(self, discounts):
        self.discounts = discounts

    def count(self, cart: Cart):
        total = cart.subtotal()
        for i in self.discounts:
            total = i.apply(cart, total)
        
        return total


mouse = Product("Мышь", 3000, "Электроника")
keyboard = Product("Клавиатура", 2000, "Электроника")

cart1 = Cart()
cart1.add_product(mouse)
cart1.add_product(keyboard)

discounts = [CategoryDiscount("Электроника", 10), FixedDiscount(500, 3000)]

engine = DiscountEngine(discounts)
print(engine.count(cart1))

    
