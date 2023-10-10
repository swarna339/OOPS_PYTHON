class Product:
    def __init__(self, product_id, name, price, quantity, category):
        self.product_id = product_id
        self.name = name
        self.price = price
        self.quantity = quantity
        self.category = category

    def display_product_details(self):
        print(f"Product ID: {self.product_id}")
        print(f"Name: {self.name}")
        print(f"Price: ${self.price:.2f}")
        print(f"Quantity in Stock: {self.quantity}")
        print(f"Category: {self.category}")
        print("\n")

class ShoppingCart:
    def __init__(self):
        self.cart = []

    def add_to_cart(self, product, quantity):
        if quantity <= product.quantity:
            self.cart.append({"product": product, "quantity": quantity})
            product.quantity -= quantity
            print(f"{quantity} {product.name}(s) added to the cart.")
        else:
            print(f"Insufficient stock of {product.name}.")

    def remove_from_cart(self, product, quantity):
        for item in self.cart:
            if item["product"] == product:
                if item["quantity"] > quantity:
                    item["quantity"] -= quantity
                    product.quantity += quantity
                else:
                    self.cart.remove(item)
                    product.quantity += item["quantity"]
                print(f"{quantity} {product.name}(s) removed from the cart.")
                return
        print(f"{product.name} not found in the cart.")

    def calculate_total_price(self):
        total_price = sum(item["product"].price * item["quantity"] for item in self.cart)
        return total_price

    def checkout(self):
        total_price = self.calculate_total_price()
        order_summary = f"Order Summary\nTotal Price: ${total_price:.2f}\n\nItems:\n"
        for item in self.cart:
            product = item["product"]
            quantity = item["quantity"]
            order_summary += f"{product.name} ({quantity} units): ${product.price * quantity:.2f}\n"
        return order_summary

class Customer:
    def __init__(self, customer_id, name, email):
        self.customer_id = customer_id
        self.name = name
        self.email = email
        self.shopping_cart = ShoppingCart()

    def add_to_cart(self, product, quantity):
        self.shopping_cart.add_to_cart(product, quantity)

    def remove_from_cart(self, product, quantity):
        self.shopping_cart.remove_from_cart(product, quantity)

    def view_cart_contents(self):
        return self.shopping_cart.cart

    def proceed_to_checkout(self):
        return self.shopping_cart.checkout()

class OnlineShop:
    def __init__(self):
        self.catalog = {}
        self.customers = {}

    def add_product(self, product):
        self.catalog[product.product_id] = product

    def register_customer(self, customer):
        self.customers[customer.customer_id] = customer

    def login_customer(self, customer_id):
        return self.customers.get(customer_id, None)

    def display_available_products(self):
        return self.catalog

# Usage Example:

# Create an OnlineShop instance
online_shop = OnlineShop()

# Add products to the catalog
product1 = Product(1, "Laptop", 800, 10, "Electronics")
product2 = Product(2, "Smartphone", 400, 20, "Electronics")
online_shop.add_product(product1)
online_shop.add_product(product2)

# Register a customer
customer1 = Customer(101, "Alice", "alice@example.com")
online_shop.register_customer(customer1)

# Login a customer
logged_in_customer = online_shop.login_customer(101)

# Add products to the customer's cart
logged_in_customer.add_to_cart(product1, 2)
logged_in_customer.add_to_cart(product2, 1)

# Display cart contents
print("Cart Contents:", logged_in_customer.view_cart_contents())

# Proceed to checkout and generate order summary
order_summary = logged_in_customer.proceed_to_checkout()
print(order_summary)
