# Lab: Build a Travel Weather Planner
def travel_advice(temp_celsius, is_rainy):
    if temp_celsius > 30:
        print("Pack light clothes and stay hydrated.")
    elif temp_celsius > 20:
        print("Mild weather. A light jacket is fine.")
    else:
        print("Pack warm clothes.")
    if is_rainy:
        print("Don't forget an umbrella!")

travel_advice(28, True)
