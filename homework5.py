"""
Homework #5 List of tuples.

Task description:
Given list of tuples people data.
1.Need to add new record with similar random'
'data to the beginning of the given list'
2.Then in this modified list swap elements'
'with indexes 1 and 5  (1<->5) and print result'
3.Then check condition that all people in modified'
'list with records indexes 6, 10, 13'
'# have age >=30 and print result'

Steps:
1. Adding new list item by using insert method for'
 'element with 0 index'
2. swapping elements using its indexes
3. use boolean operators AND to verify condition
"""

people_records = [
    ('John', 'Doe', 28, 'Engineer', 'New York'),
    ('Alice', 'Smith', 35, 'Teacher', 'Los Angeles'),
    ('Bob', 'Johnson', 45, 'Doctor', 'Chicago'),
    ('Emily', 'Williams', 30, 'Artist', 'San Francisco'),
    ('Michael', 'Brown', 22, 'Student', 'Seattle'),
    ('Sophia', 'Davis', 40, 'Lawyer', 'Boston'),
    ('David', 'Miller', 33, 'Software Developer', 'Austin'),
    ('Olivia', 'Wilson', 27, 'Marketing Specialist', 'Denver'),
    ('Daniel', 'Taylor', 38, 'Architect', 'Portland'),
    ('Grace', 'Moore', 25, 'Graphic Designer', 'Miami'),
    ('Samuel', 'Jones', 50, 'Business Consultant', 'Atlanta'),
    ('Emma', 'Hall', 31, 'Chef', 'Dallas'),
    ('William', 'Clark', 29, 'Financial Analyst', 'Houston'),
    ('Ava', 'White', 42, 'Journalist', 'San Diego'),
    ('Ethan', 'Anderson', 36, 'Product Manager', 'Phoenix')
]

people_records.insert(0, ('Kobe', 'Bryant', 35, 'Basket player', 'LA'))
print(people_records)

people_records[1] = people_records[5]
print(people_records)

age_bool = (people_records[6][2] and people_records[13][2] and people_records[10][2]) >= 30
print(age_bool)
