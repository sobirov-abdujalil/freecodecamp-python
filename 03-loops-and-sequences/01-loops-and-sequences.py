# Working with Loops and Sequences
fruits = ["apple", "banana", "cherry"]
for fruit in fruits:
    print(fruit)

for i in range(5):
    print(i, end=" ")
print()

count = 0
while count < 3:
    print(f"Count: {count}")
    count += 1

nums = [x * 2 for x in range(1, 6)]
print(nums)
