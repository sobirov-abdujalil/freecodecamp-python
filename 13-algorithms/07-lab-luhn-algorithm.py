# Lab: Implement the Luhn Algorithm
def luhn_algorithm(card_number):
    digits = [int(d) for d in str(card_number) if d.isdigit()]
    digits.reverse()

    for i in range(1, len(digits), 2):
        digits[i] *= 2
        if digits[i] > 9:
            digits[i] -= 9

    total = sum(digits)
    return total % 10 == 0

def validate_card(card_number):
    card_str = str(card_number).replace(" ", "").replace("-", "")
    if luhn_algorithm(card_str):
        return "Valid card number"
    return "Invalid card number"

cards = ["4532015112830366", "4532015112830367"]
for card in cards:
    print(f"{card}: {validate_card(card)}")
