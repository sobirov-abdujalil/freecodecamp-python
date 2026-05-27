print("Hello! Welcome to the tip calculator.")

total = float(input("What is the total bill? $"))

people = int(input("How many people are splitting the bill? "))

tip_percent = float(input("What percentage tip would you like to leave? "))

tip = total * (tip_percent / 100)

grand_total = total + tip

per_person = grand_total / people

print(f"Each person pays: ${per_person:.2f}")
