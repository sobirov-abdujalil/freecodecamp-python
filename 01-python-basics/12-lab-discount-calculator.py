# Lab: Build an Apply Discount Function
def apply_discount(price, discount_percent):
    return price * (1 - discount_percent / 100)

def format_price(amount):
    return f"${amount:.2f}"

original = 49.99
discounted = apply_discount(original, 20)
print(f"Original: {format_price(original)}")
print(f"After 20% off: {format_price(discounted)}")
