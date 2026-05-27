# Workshop: Build a Report Card Printer
def calculate_grade(score):
    if score >= 90:
        return "A"
    elif score >= 80:
        return "B"
    elif score >= 70:
        return "C"
    elif score >= 60:
        return "D"
    else:
        return "F"

def print_report_card(name, scores):
    print(f"Student: {name}")
    print(f"Average: {sum(scores) / len(scores):.1f}")
    print(f"Grade: {calculate_grade(sum(scores) / len(scores))}")

print_report_card("Alice", [85, 92, 78, 95])
