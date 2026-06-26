for i in range(3):
    for j in range(2):
        print((i, j))  


#list comprehension#
result = [(i, j) for i in range(3) for j in range(2)]
print(result)  


records = [
    {"id": 1, "name": "Alice"},
    {"id": 2, "name": "Bob"},
    {"id": 1, "name": "Alice"},
    {"id": 3, "name": "Charlie"},
    {"id": 2, "name": "Bob"}
]   

unique_records =[(record) for record in records if tuple(sorted(record.items())) not in [tuple(sorted(r.items())) for r in records[:records.index(record)]] ]

Square of numbers using list comprehension
numbers = [1, 2, 3, 4, 5]
squares=[number**2 for number in numbers]

print(squares)  # Output: [1, 4, 9, 16, 25]


Convert strings to uppercase
strings = ["hello", "world", "python"]
uppercase_strings = [string.upper() for string in strings]

print(uppercase_strings)  # Output: ['HELLO', 'WORLD', 'PYTHON']  

Length of a each word in a list
words = ["apple", "banana", "cherry"]   
word_lengths=[len(word) for word in words]
print(word_lengths)

Remove all empty strings.
strings = ["hello", "", "world", "", "python"]
non_empty_strings = [string for string in strings if string != ""]
print(non_empty_strings)  # Output: ['hello', 'world', 'python']

Keep employees whose salary is greater than 50000.
employees = [
    {"id": 1, "name": "Alice", "salary": 60000},
    {"id": 2, "name": "Bob", "salary": 40000},
    {"id": 3, "name": "Charlie", "salary": 75000},
    {"id": 4, "name": "David", "salary": 45000},
]

high_earners=[employee["name"] for employee in employees if employee["salary"]>50000]
print (high_earners)  # Output: ['Alice', 'Charlie'] 


