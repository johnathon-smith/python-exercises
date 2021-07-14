# Control Structures
# 1a - prompt the user for a day of the week, print out whether the day is Monday or not
users_day_of_the_week = input('Please choose a day of the week: ')

if users_day_of_the_week == 'Monday':
    print("You chose Monday!")
else:
    print("You didn't choose Monday!")
print('\n')
# 1b - prompt the user for a day of the week, print out whether the day is a weekday or a weekend
users_day_of_the_week = input('Please choose a day of the week: ')

if users_day_of_the_week == 'Saturday' or users_day_of_the_week == 'Sunday':
    print("You chose a weekend day!")
else:
    print("You chose a weekday!")

# 1c - create variables and make up values for
# - the number of hours worked in one week
# - the hourly rate
# - how much the week's paycheck will be
# write the python code that calculates the weekly paycheck. You get paid time and a half if you work more than 40 hours
hours_worked = 52
hourly_rate = 25
if hours_worked > 40:
    weekly_pay = hourly_rate * 40 + (hourly_rate * 1.5) * (hours_worked - 40)
else:
    weekly_pay = hourly_rate * hours_worked
print('\n')
print("Hours worked: ", hours_worked)
print("Hourly_pay: ", hourly_rate)
print(f'Your weekly pay is: ${weekly_pay}')

#Loop Basics
# 2a - While
# Create an integer variable i with a value of 5.
# Create a while loop that runs so long as i is less than or equal to 15
# Each loop iteration, output the current value of i, then increment i by one.
print('\n')
i = 5
while i <= 15:
    print(i)
    i += 1
print('\n')
# Create a while loop that will count by 2's starting with 0 and ending at 100. Follow each number with a new line.
i = 0
while i <= 100:
    print(i)
    i += 2
    print('\n')

# Alter your loop to count backwards by 5's from 100 to -10.
i = 100
while i >= -10:
    print(i)
    i -= 5
    print('\n')

# Create a while loop that starts at 2, and displays the number squared on each line while the number is less than 1,000,000
i = 2
while i < 1000000:
    print(i)
    i = pow(i, 2)
print('\n')

# Write a loop that uses print to create the output shown below.
#The output shows printed numbers starting at 100 and decreasing by 5 all the way down to 5
i = 100
while i >= 5:
    print(i)
    i -= 5

print('\n')

#For Loops
#Write some code that prompts the user for a number, then shows a multiplication table up through 10 for that number.
users_number = int(input('Please enter a number: '))

for i in range(1, 11):
    print(f'{users_number} x {i} = {users_number * i}')

print("\n")

# Create a for loop that uses print to create the output shown below.
for i in range(1, 10):
    print(f'{i}' * i)

print("\n")

#break and continue
#Prompt the user for an odd number between 1 and 50. Use a loop and a break statement to continue prompting the user if they enter invalid input.
#(Hint: use the isdigit method on strings to determine this). Use a loop and the continue statement to output all the odd numbers between 1 and 50,
#except for the number the user entered.
users_number = input('Please enter an odd number between 1 and 50: ')

while True:
    if users_number.isdigit() == True and int(users_number) % 2 == 1 and int(users_number) >= 1 and int(users_number) <= 50:
        break
    print('\nInvalid input')
    users_number = input('Please enter an odd number between 1 and 50: ')

print('\n')
print('Number to skip:', users_number)

for i in range(1, 51, 2):
    if i == int(users_number):
        print('This number skipped!')
        continue
    print('Here is an odd number:', i)

print('\n')

#The input function can be used to prompt for input and use that input in your python code. 
#Prompt the user to enter a positive number and write a loop that counts from 0 to that number. 
#(Hints: first make sure that the value the user entered is a valid number, also note that the input function returns a string, 
#so you'll need to convert this to a numeric type.)
users_number = input('Please enter any positive number: ')

while users_number.isdigit() != True or int(users_number) <= 0:
    print('\nInvalid input')
    users_number = input('Please enter any positive number: ')

print('\n')
print('Counting to', users_number)
for i in range(0, int(users_number) + 1):
    print(i)

print('\n')

#Write a program that prompts the user for a positive integer. Next write a loop that prints out the numbers from the number the user entered down to 1.
users_number = input('Please enter any positive number: ')

while users_number.isdigit() != True or int(users_number) <= 0:
    print('\nInvalid input')
    users_number = input('Please enter any positive number: ')

print('\n')
print('Counting down from:', users_number)
i = int(users_number)
while i >= 1:
    print(i)
    i -= 1

print('\n')

#FizzBuzz
#Write a program that prints the numbers from 1 to 100.
#For multiples of three print "Fizz" instead of the number
#For the multiples of five print "Buzz".
#For numbers which are multiples of both three and five print "FizzBuzz".
print('FizzBuzz Test:')
for i in range(1, 101):
    if i % 3 == 0 and i % 5 == 0:
        print('FizzBuzz')
    elif i % 3 == 0:
        print('Fizz')
    elif i % 5 == 0:
        print('Buzz')
    else:
        print(i)

print('\n')

#Display a Table of Powers
#Prompt the user to enter an integer.
#Display a table of squares and cubes from 1 to the value entered.
#Ask if the user wants to continue. I'm assuming this means if the user wants to pick another number and do this again.
#Assume that the user will enter valid data.
#Only continue if the user agrees to.

while True:
    users_number = input('What number would you like to go up to? ')
    print('\n')

    print('Here is your table!')
    print('\n')
    print('Number | Squared | Cubed ')
    print('------ | ------- | -----')

    for i in range(1, int(users_number) + 1):
        print(f'{i: <6} | {pow(i, 2): <7} | {pow(i,3): <}')

    print('\n')

    wants_to_continue = input('Do you want to continue? Y for yes, N for no: ')
    print('\n')

    if wants_to_continue[0].lower() == 'y':
        continue
    else:
        break


#Convert given number grades into letter grades.

"""
Prompt the user for a numerical grade from 0 to 100.
Display the corresponding letter grade.
Prompt the user to continue.
Assume that the user will enter valid integers for the grades.
The application should only continue if the user agrees to.
Grade Ranges:

A : 100 - 88
B : 87 - 80
C : 79 - 67
D : 66 - 60
F : 59 - 0
"""
while True:
    users_grade = int(input('Please enter a numerical grade from 0 to 100: '))
    print('\n')

    if users_grade < 60:
        print('Your letter grade is: F')
    elif users_grade < 67:
        print('Your letter grade is: D')
    elif users_grade < 80:
        print('Your letter grade is: C')
    elif users_grade < 88:
        print('Your letter grade is: B')
    else:
        print('Your letter grade is: A')
    
    print('\n')
    wants_to_continue = input('Would you like to continue? Y for yes, N for no: ')
    print('\n')

    if wants_to_continue[0].lower() == 'y':
        continue
    else:
        break


#Create a list of dictionaries where each dictionary represents a book that you have read. Each dictionary in the list should have the keys title, author,
#and genre. Loop through the list and print out information about each book.

#Prompt the user to enter a genre, then loop through your books list and print out the titles of all the books in that genre.
books = [
    {
        'Title': 'Eragon',
        'Author': 'Christopher Paolini',
        'Genre': 'Fantasy'
    },
    {
        'Title': 'The Outsider',
        'Author': 'Stephen King',
        'Genre': 'Horror'
    },
    {
        'Title': 'Unscripted',
        'Author': 'MJ DeMarco',
        'Genre': 'Business'
    },
    {
        'Title': 'Mr. Mercedes',
        'Author': 'Stephen King',
        'Genre': 'Horror'
    }
]

print("Books I have read:")
for book in books:
    print(f"{book['Title']}, by {book['Author']}. Genre: {book['Genre']}")

print('\n')
chosen_genre = input("Please enter a genre to search for: ")

print('Books in your genre:')
for book in books:
    if book['Genre'] == chosen_genre:
        print(f"{book['Title']}")
