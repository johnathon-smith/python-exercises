#Use from to import the calculate_tip function directly. Call this function with values you choose and print the result.
from function_exercises import calculate_tip

tip = calculate_tip(0.15, 10)
print('Your calculated tip is:', tip)

#Using itertools module, How many different ways can you combine the letters from "abc" with the numbers 1, 2, and 3?
import itertools as it 

combos = it.permutations(["a","b","c",1,2,3], 2)

print('\n2a')
for item in combos:
    print(item)

#How many different combinations are there of 2 letters from "abcd"?
combos = it.combinations('abcd',2)
print('\n2b)')
for item in combos:
    print(item)

#How many different permutations are there of 2 letters from "abcd"?
combos = it.permutations('abcd',2)
print('\n2c')
for item in combos:
    print(item)


#import json for question 3
import json
users = json.load(open('profiles.json'))

print('\n3)')
#Your code should produce a list of dictionaries. Using this data, write some code that calculates and outputs the following information:
#Total number of users
print(f'The total number of users is {len(users)}')

#Number of active users
active_users = []
for user in users:
    if user["isActive"] == True:
        active_users.append(user)

print(f'The total number of active users is {len(active_users)}')

#Number of inactive users
print(f'The total number of inactive users is {len(users) - len(active_users)}')

#Grand total of balances for all users
balance_total = 0
user_balances = []

for user in users:
    user_balance = user["balance"].replace('$','').replace(',','')
    user_balances.append(user_balance)
    balance_total += float(user_balance)

print(f'The grand total of all user\'s balances is {balance_total}')

#Average balance per user
print(f'The average balance per user is {balance_total / len(users):.2f}')

#User with the lowest balance
lowest_balance_user_index = user_balances.index(min(user_balances))
lowest_balance_user = users[lowest_balance_user_index]
lowest_balance = min(user_balances)
print(f'The user with the lowest balance is {lowest_balance_user["name"]} with a balance of {lowest_balance_user["balance"]}')

#User with the highest balance
highest_balance = max(user_balances)
highest_balance_user_index = user_balances.index(max(user_balances))
highest_balance_user = users[highest_balance_user_index]
print(f'The user with the highest balance is {highest_balance_user["name"]} with a balance of {highest_balance_user["balance"]}')

#Most common favorite fruit
fav_fruit_types = []
fav_fruit_list = []

for user in users:
    fav_fruit_list.append(user["favoriteFruit"])
    if fav_fruit_types.count(user["favoriteFruit"]) == 0:
        fav_fruit_types.append(user["favoriteFruit"])

fav_fruit_counts = []

for fruit in fav_fruit_types:
    fav_fruit_counts.append(fav_fruit_list.count(fruit))

most_fav_fruit_index = fav_fruit_counts.index(max(fav_fruit_counts))
most_fav_fruit = fav_fruit_types[most_fav_fruit_index]

print(f'The most common favorite fruiit among users is the {most_fav_fruit} with a count of {max(fav_fruit_counts)}')

#Least most common favorite fruit
least_fav_fruit_index = fav_fruit_counts.index(min(fav_fruit_counts))
least_fav_fruit = fav_fruit_types[least_fav_fruit_index]

print(f'The least common favorite fruit among users is the {least_fav_fruit} with a count of {min(fav_fruit_counts)}')

#Total number of unread messages for all users
user_unread_message_counts = []

for user in users:
    user_messages = ''

    for char in user["greeting"]:

        if char.isdigit() == True:
            user_messages = user_messages + char
    
    num_messages = int(user_messages)
    user_unread_message_counts.append(num_messages)

total_unread_messages = sum(user_unread_message_counts)

print(f'The total number of unread messages is {total_unread_messages}.')