records = [
    {"id": 1, "name": "Alice"},
    {"id": 2, "name": "Bob"},
    {"id": 1, "name": "Alice"},
    {"id": 3, "name": "Charlie"},
    {"id": 2, "name": "Bob"}
]

unique_records = []
seen = set()

for record in records:
    record_tuple = tuple(sorted(record.items()))
    if record_tuple not in seen:
        seen.add(record_tuple)
        unique_records.append(record)
print(unique_records)


#Remove duplicates based on ID 
unique_records_by_id = []
seen_ids = set()

for record in records:
    if record["id"] not in seen_ids:
        seen_ids.add(record["id"])
        unique_records_by_id.append(record)

print(unique_records_by_id)


#Generators

def even_numbers(n):
    for i in range(n):
        if i % 2 == 0:
            yield i

for num in even_numbers(10):
    print(num)
