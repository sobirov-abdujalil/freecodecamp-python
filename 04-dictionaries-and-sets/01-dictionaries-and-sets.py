# Working with Dictionaries and Sets
student = {"name": "Alice", "age": 22, "grade": "A"}
print(student["name"])
student["city"] = "New York"
print(student.keys())
print(student.values())

unique_ids = {101, 102, 103, 101, 104}
print(unique_ids)
print(101 in unique_ids)

nums1 = {1, 2, 3, 4}
nums2 = {3, 4, 5, 6}
print(nums1 & nums2)
print(nums1 | nums2)
