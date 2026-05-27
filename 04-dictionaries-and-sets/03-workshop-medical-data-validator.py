# Workshop: Build a Medical Data Validator
def validate_patient_record(record):
    required = {"patient_id", "name", "age", "diagnosis"}
    if not required.issubset(record.keys()):
        missing = required - record.keys()
        return False, f"Missing: {missing}"
    if not isinstance(record["age"], int) or record["age"] < 0:
        return False, "Invalid age"
    return True, "Valid record"

record = {"patient_id": "P123", "name": "John", "age": 45, "diagnosis": "Flu"}
valid, msg = validate_patient_record(record)
print(f"{valid}: {msg}")
