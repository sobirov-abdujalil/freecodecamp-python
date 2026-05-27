# Workshop: Build a Pin Extractor
def extract_pins(text):
    pins = []
    words = text.split()
    for word in words:
        if word.isdigit() and len(word) == 4:
            pins.append(word)
    return pins

def validate_pin(pin):
    return len(pin) == 4 and pin.isdigit()

text = "My pins are 1234, 5678, and abc1"
found = extract_pins(text)
print(f"Found pins: {found}")
print(f"Validate 1234: {validate_pin('1234')}")
