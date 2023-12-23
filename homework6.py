"""
Homework #6 List sorting.

Task description:
1. Need to sort list by age and sex fields
2. Need to get new list as old list without'
 'first two elements and last two elements. Print this new list'
3. In the new list need to calculate total numbers of'
 '"female"  and "male" and print it as small table.'

Flow:
 1. Sorting list using sort method and lambda build in function
 2. using pop method by indexes for removing extra list elements'
  'from the list. printing new list'
 3. importing itertools to format list as flatlist
 4. then counting each 'female' and 'male' from flatlist
 5. creating table using loop and display count results

"""
import itertools

people = [
    ('Alice', 32, 100, 'Johnson', 'female'),
    ('Bob', 41, 200, 'Smith', 'male'),
    ('Charlie', 27, 150, 'Jones', 'male'),
    ('David', 52, 75, 'Williams', 'male'),
    ('Eve', 18, 300, 'Davis', 'female'),
    ('Frank', 33, 50, 'Taylor', 'male'),
    ('Grace', 42, 125, 'Clark', 'female'),
    ('Henry', 26, 225, 'Lewis', 'male'),
    ('Ivy', 38, 175, 'Moore', 'female'),
    ('Jack', 20, 140, 'Harris', 'male'),
    ('Kate', 37, 110, 'Miller', 'female'),
    ('Leo', 44, 90, 'Wilson', 'male'),
    ('Mae', 29, 180, 'Brown', 'female'),
    ('Nick', 51, 70, 'Davies', 'male'),
    ('Oliver', 18, 250, 'Collins', 'male'),
    ('Pete', 36, 160, 'Green', 'male'),
    ('Quinn', 20, 230, 'Bell', 'female'),
    ('Remy', 30, 120, 'Foster', 'male'),
    ('Sara', 28, 140, 'Baker', 'female'),
    ('Tom', 47, 80, 'Scott', 'male'),
    ('Ursula', 39, 135, 'Adams', 'female'),
    ('Vivian', 25, 190, 'Ross', 'female'),
    ('Wendy', 46, 90, 'Wright', 'female'),
    ('Xavier', 31, 105, 'Reed', 'male'),
    ('Yuliana', 22, 200, 'Lopez', 'female'),
    ('Zack', 48, 60, 'Mitchell', 'male'),
    ('Adam', 35, 75, 'Davis', 'male'),
    ('Bella', 27, 125, 'Smith', 'female'),
    ('Charlie', 44, 115, 'Johnson', 'male'),
    ('Daisy', 20, 215, 'Miller', 'female'),
    ('Ethan', 33, 100, 'Taylor', 'male'),
    ('Fiona', 40, 150, 'Jones', 'female'),
    ('George', 24, 180, 'Lewis', 'male'),
    ('Hannah', 22, 200, 'Williams', 'female'),
    ('Ivan', 29, 160, 'Brown', 'male'),
    ('Julie', 55, 90, 'Clark', 'female'),
    ('Kenny', 38, 140, 'Harris', 'male'),
    ('Luna', 55, 170, 'Smith', 'female'),
    ('Mike', 55, 55, 'Johnson', 'male')
]

people.sort(key=lambda x: (x[1], x[4]))
print(people)

people_new = people.copy()
people_new.pop(0)
people_new.pop(0)
people_new.pop()
people_new.pop()
print(people_new)

flat_people = list(itertools.chain.from_iterable(people_new))
count_fem = flat_people.count('female')
count_male = flat_people.count('male')

print(count_fem)
print(count_male)

sep_num = 21

print("-" * sep_num)
print(f"| {'vowel':^7} | {'count':^7} |")
print("-" * sep_num)
sex_count = {
    "female": count_fem,
    "male": count_male,
}

for sex, count in sex_count.items():
    print(f"| {sex:^8}| {count:^7} |")

print("-" * sep_num)
