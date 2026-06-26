#Create a dictionary mapping employee names to salaries.

employees = [
    {"id": 1, "name": "Alice", "salary": 60000},
    {"id": 2, "name": "Bob", "salary": 40000},
    {"id": 3, "name": "Charlie", "salary": 75000},
    {"id": 4, "name": "David", "salary": 45000}
]

name_to_salary = {employee["name"]: employee["salary"] for employee in employees}
print(name_to_salary)  # Output: {'Alice': 60000, 'Bob': 40000, 'Charlie': 75000, 'David': 45000}


#Keep only employees earning more than 50,000.
high_earners = {employee["name"]: employee["salary"] for employee in employees if employee["salary"] > 50000}
print(high_earners)  # Output: {'Alice': 60000, 'Charlie': 75000}  

words = [
    "python",
    "ai",
    "python",
    "llm",
    "ai",
    "rag",
    "mcp"
]

#Create a dictionary containing each word and its length.
word_lengths = {word: len(word) for word in words}
print(word_lengths)  # Output: {'python': 6, 'ai': 2, 'llm': 3, 'rag': 3, 'mcp': 3}


#Keep only words longer than 3 characters
long_words = {word: len(word) for word in words if len(word) > 3}
print(long_words)  # Output: {'python': 6, 'llm': 3, 'rag': 3}  

responses = [
    {"question": "Hi", "tokens": 10, "cost": 0.001},
    {"question": "Explain AI", "tokens": 250, "cost": 0.02},
    {"question": "Python", "tokens": 100, "cost": 0.005},
] 

strings = [word["question"] for word in responses]
print(strings)  # Output: ['Hi', 'Explain AI', 'Python'] 

#Keep only responses where tokens > 100
filtered_responses = [response for response in responses if response["tokens"] > 100]
print(filtered_responses)  # Output: [{'question': 'Explain AI', 'tokens': 250, 'cost': 0.02}]

#Create a dictionary mapping questions to token count.
question_to_tokens = {response["question"]: response["tokens"] for response in responses}
print(question_to_tokens)  # Output: {'Hi': 10, 'Explain AI': 250, 'Python': 100}