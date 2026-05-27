# Workshop: Build an Employee Profile Generator
def create_profile(first, last, role, years):
    email = f"{first.lower()}.{last.lower()}@company.com"
    return f"""Employee Profile
Name: {first} {last}
Role: {role}
Years: {years}
Email: {email}"""

profile = create_profile("Jane", "Doe", "Developer", 3)
print(profile)
