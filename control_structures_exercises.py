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
