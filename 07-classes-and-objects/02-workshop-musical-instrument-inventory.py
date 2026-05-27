# Workshop: Build a Musical Instrument Inventory
class Instrument:
    def __init__(self, name, instrument_type, price):
        self.name = name
        self.type = instrument_type
        self.price = price

class Inventory:
    def __init__(self):
        self.instruments = []

    def add(self, instrument):
        self.instruments.append(instrument)

    def total_value(self):
        return sum(i.price for i in self.instruments)

    def by_type(self, instrument_type):
        return [i for i in self.instruments if i.type == instrument_type]

inv = Inventory()
inv.add(Instrument("Guitar", "String", 500))
inv.add(Instrument("Piano", "Keyboard", 2000))
print(f"Total value: ${inv.total_value()}")
