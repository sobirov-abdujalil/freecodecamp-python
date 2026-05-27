# Workshop: Build a Movie Ticket Booking Calculator
def calculate_ticket_price(age, is_3d, is_member):
    base = 12.00
    if age < 12:
        base = 8.00
    elif age >= 65:
        base = 10.00
    if is_3d:
        base += 3.00
    if is_member:
        base *= 0.85
    return base

price = calculate_ticket_price(25, True, False)
print(f"Ticket price: ${price:.2f}")
