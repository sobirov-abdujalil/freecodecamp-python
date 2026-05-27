# Lab: Debug an ISBN Validator
def validate_isbn10(isbn):
    isbn = isbn.replace("-", "").replace(" ", "")
    if len(isbn) != 10:
        return False
    total = 0
    for i, char in enumerate(isbn):
        if char == "X" and i == 9:
            total += 10
        elif char.isdigit():
            total += int(char) * (10 - i)
        else:
            return False
    return total % 11 == 0

isbns = ["0-306-40615-2", "123456789X", "abcdefghij"]
for isbn in isbns:
    print(f"{isbn}: {validate_isbn10(isbn)}")
