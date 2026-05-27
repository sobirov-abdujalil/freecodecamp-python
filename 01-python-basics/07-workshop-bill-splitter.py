# Workshop: Build a Bill Splitter
def split_bill(total, people, tip_percent=15):
    tip = total * (tip_percent / 100)
    grand_total = total + tip
    return grand_total / people

total = 120.00
people = 4
tip = 18
per_person = split_bill(total, people, tip)
print(f"Each person pays: ${per_person:.2f}")
