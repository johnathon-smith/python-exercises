# 20 Python Data Structure Manipulation Exercises

#The following questions reference the `students` data structure below. Write
#the python code to answer the following questions:
students = [
    {
        "id": "100001",
        "student": "Ada Lovelace",
        "coffee_preference": "light",
        "course": "web development",
        "grades": [70, 91, 82, 71],
        "pets": [{"species": "horse", "age": 8}],
    },
    {
        "id": "100002",
        "student": "Thomas Bayes",
        "coffee_preference": "medium",
        "course": "data science",
        "grades": [75, 73, 86, 100],
        "pets": [],
    },
    {
        "id": "100003",
        "student": "Marie Curie",
        "coffee_preference": "light",
        "course": "web development",
        "grades": [70, 89, 69, 65],
        "pets": [{"species": "cat", "age": 0}],
    },
    {
        "id": "100004",
        "student": "Grace Hopper",
        "coffee_preference": "dark",
        "course": "data science",
        "grades": [73, 66, 83, 92],
        "pets": [{"species": "dog", "age": 4}, {"species": "cat", "age": 4}],
    },
    {
        "id": "100005",
        "student": "Alan Turing",
        "coffee_preference": "dark",
        "course": "web development",
        "grades": [78, 98, 85, 65],
        "pets": [
            {"species": "horse", "age": 6},
            {"species": "horse", "age": 7},
            {"species": "dog", "age": 5},
        ],
    },
    {
        "id": "100006",
        "student": "Rosalind Franklin",
        "coffee_preference": "dark",
        "course": "data science",
        "grades": [76, 70, 96, 81],
        "pets": [],
    },
    {
        "id": "100007",
        "student": "Elizabeth Blackwell",
        "coffee_preference": "dark",
        "course": "web development",
        "grades": [69, 94, 89, 86],
        "pets": [{"species": "cat", "age": 10}],
    },
    {
        "id": "100008",
        "student": "Rene Descartes",
        "coffee_preference": "medium",
        "course": "data science",
        "grades": [87, 79, 90, 99],
        "pets": [{"species": "cat", "age": 10}, {"species": "cat", "age": 8}],
    },
    {
        "id": "100009",
        "student": "Ahmed Zewail",
        "coffee_preference": "medium",
        "course": "data science",
        "grades": [74, 99, 93, 89],
        "pets": [{"species": "cat", "age": 0}, {"species": "cat", "age": 0}],
    },
    {
        "id": "100010",
        "student": "Chien-Shiung Wu",
        "coffee_preference": "medium",
        "course": "web development",
        "grades": [82, 92, 91, 65],
        "pets": [{"species": "cat", "age": 8}],
    },
    {
        "id": "100011",
        "student": "William Sanford Nye",
        "coffee_preference": "dark",
        "course": "data science",
        "grades": [70, 92, 65, 99],
        "pets": [{"species": "cat", "age": 8}, {"species": "cat", "age": 5}],
    },
    {
        "id": "100012",
        "student": "Carl Sagan",
        "coffee_preference": "medium",
        "course": "data science",
        "grades": [100, 86, 91, 87],
        "pets": [{"species": "cat", "age": 10}],
    },
    {
        "id": "100013",
        "student": "Jane Goodall",
        "coffee_preference": "light",
        "course": "web development",
        "grades": [80, 70, 68, 98],
        "pets": [{"species": "horse", "age": 4}],
    },
    {
        "id": "100014",
        "student": "Richard Feynman",
        "coffee_preference": "medium",
        "course": "web development",
        "grades": [73, 99, 86, 98],
        "pets": [{"species": "dog", "age": 6}],
    },
]
#1. How many students are there?
num_students = len(students)
print('\n1)')
print(f'There are {num_students} students.')

#2. How many students prefer light coffee? For each type of coffee roast?
light_coffee_count = 0
medium_coffee_count = 0
dark_coffee_count = 0

for student in students:
    if student["coffee_preference"] == "light":
        light_coffee_count += 1
    elif student["coffee_preference"] == "medium":
        medium_coffee_count += 1
    else: 
        dark_coffee_count += 1

print('\n2)')
print('Number of students that prefer light coffee:', light_coffee_count)
print('Number of students that prefer medium coffee:', medium_coffee_count)
print('Number of students that prefer dark coffee:', dark_coffee_count)
#3. How many types of each pet are there?

#4. How many grades does each student have? Do they all have the same number of grades?
previous_student_num_grades = len(students[0]["grades"])
same_num_grades = True

print('\n4)')
for student in students:
    if previous_student_num_grades != len(student["grades"]):
        same_num_grades = False

    print(f'{student["student"]} has {len(student["grades"])} grades.')

    previous_student_num_grades = len(student["grades"])

if same_num_grades == True:
    print('All the students have the same number of grades.')
else:
    print('All the students do not have the same number of grades.')

#5. What is each student's grade average?
print('\n5)')
for student in students:
    print(f'{student["student"]} has a grade average of {sum(student["grades"]) / len(student["grades"])}.')

#6. How many pets does each student have?
print('\n6)')
for student in students:
    print(f'{student["student"]} has {len(student["pets"])} pet(s).')

#7. How many students are in web development? data science?
print('\n7)')
web_dev_count = 0
data_science_count = 0
other_course_count = 0

for student in students:
    if student["course"] == 'web development':
        web_dev_count += 1
    elif student["course"] == 'data science':
        data_science_count += 1
    else:
        other_course_count += 1

print(f'There are {web_dev_count} students in web development.')
print(f'There are {data_science_count} students in data science.')

if other_course_count > 0:
    print(f'There are {other_course_count} students in some other course.')

#8. What is the average number of pets for students in web development?
print('\n8)')

num_web_dev_pets = 0
for student in students:
    if student["course"] == 'web development':
        num_web_dev_pets += len(student["pets"])

print(f'The average number of pets for students in web development is {num_web_dev_pets / web_dev_count: .2f}.')

#9. What is the average pet age for students in data science?
print('\n9)')

num_data_science_pets = 0
total_data_science_pet_age = 0

for student in students:
    if student["course"] == 'data science' and len(student["pets"]) > 0:
        for pet in student["pets"]:
            num_data_science_pets += 1
            total_data_science_pet_age += pet["age"]

print(f'The average pet age for data science students is {total_data_science_pet_age / num_data_science_pets: .2f} years.')

#10. What is most frequent coffee preference for data science students?
print('\n10)')

data_sci_light_count = 0
data_sci_medium_count = 0
data_sci_dark_count = 0

for student in students:
    if student["course"] == 'data science':
        if student["coffee_preference"] == 'light':
            data_sci_light_count += 1
        elif student["coffee_preference"] == 'medium':
            data_sci_medium_count += 1
        else:
            data_sci_dark_count += 1

if data_sci_light_count > data_sci_medium_count and data_sci_light_count > data_sci_dark_count:

    print(f'Most data science students prefer light coffee with a count of {data_sci_light_count}.')

elif data_sci_medium_count > data_sci_light_count and data_sci_medium_count > data_sci_dark_count:

    print(f'Most data science students prefer medium coffee with a count of {data_sci_medium_count}.')

else:
    print(f'Most data science students prefer dark coffee with a count of {data_sci_dark_count}.')

#11. What is the least frequent coffee preference for web development students?
print('\n11)')

web_dev_light_count = 0
web_dev_med_count = 0
web_dev_dark_count = 0

for student in students:
    if student["course"] == 'web development':
        if student["coffee_preference"] == 'light':
            data_sci_light_count += 1
        elif student["coffee_preference"] == 'medium':
            data_sci_medium_count += 1
        else:
            data_sci_dark_count += 1

if web_dev_light_count > web_dev_med_count and web_dev_light_count > web_dev_dark_count:

    print(f'Light coffee is the lease preferred among web developers with a count of {web_dev_light_count}.')

elif web_dev_med_count > web_dev_light_count and web_dev_med_count > web_dev_dark_count:

    print(f'Medium coffee is the lease preferred among web developers with a count of {web_dev_med_count}.')

else:
    print(f'Dark coffee is the lease preferred among web developers with a count of {web_dev_dark_count}.')
#12. What is the average grade for students with at least 2 pets?
print('\n12)')

num_multi_pet_students = 0
total_grades_multi_pet_students = 0
grade_count_multi_pet_students = 0

for student in students:
    if len(student["pets"]) >= 2:
        num_multi_pet_students += 1
        total_grades_multi_pet_students += sum(student["grades"])
        grade_count_multi_pet_students += len(student["grades"])

print(f'The average grade for students with at least 2 pets is {total_grades_multi_pet_students / grade_count_multi_pet_students}.')

#13. How many students have 3 pets?
print('\n13)')

num_students_with_three_pets = 0

for student in students:
    if len(student["pets"]) == 3:
        num_students_with_three_pets += 1

print(f'The number of students with 3 pets is {num_students_with_three_pets}.')

#14. What is the average grade for students with 0 pets?
print('\n14)')

num_zero_pet_students = 0
total_grades_zero_pet_students = 0
grade_count_zero_pet_students = 0

for student in students:
    if len(student["pets"]) == 0:
        num_zero_pet_students += 1
        total_grades_zero_pet_students += sum(student["grades"])
        grade_count_zero_pet_students += len(student["grades"])

print(f'The average grade for students with zero pets is {total_grades_zero_pet_students / grade_count_zero_pet_students}')

#15. What is the average grade for web development students? data science students?
print('\n15)')

grade_total_web_dev = 0
grade_total_data_sci = 0
grade_count_web_dev = 0
grade_count_data_sci = 0

for student in students:
    if student["course"] == "data science":
        grade_total_data_sci += sum(student["grades"])
        grade_count_data_sci += len(student["grades"])
    else:
        grade_total_web_dev += sum(student["grades"])
        grade_count_web_dev += len(student["grades"])

print(f'The average grade for data science students is {grade_total_data_sci / grade_count_data_sci: .2f}')
print(f'The average grade for web development students is {grade_total_web_dev / grade_count_web_dev: .2f}')

#16. What is the average grade range (i.e. highest grade - lowest grade) for dark coffee drinkers?
print('\n16)')

dark_coffee_total_grade_range = 0
total_dark_coffee_count = 0

for student in students:
    if student["coffee_preference"] == 'dark':
        dark_coffee_total_grade_range += (max(student["grades"]) - min(student["grades"]))
        total_dark_coffee_count += 1

print(f'The average grade range for dark coffee drinkers is {dark_coffee_total_grade_range / total_dark_coffee_count: .2f}.')

#17. What is the average number of pets for medium coffee drinkers?  
print('\n17)')

num_med_coffee_pets = 0
total_med_coffee_count = 0

for student in students:
    if student["coffee_preference"] == 'medium':
        num_med_coffee_pets += len(student["pets"])
        total_med_coffee_count += 1

print(f'The average number of pets for medium coffee drinkers is {num_med_coffee_pets / total_med_coffee_count: .2f}')

#18. What is the most common type of pet for web development students?
print('\n18)')


#19. What is the average name length?
#20. What is the highest pet age for light coffee drinkers?
