#Define a function named is_two. It should accept one input and return True if the passed input is either the number or the string 2, False otherwise.
def is_two(num):
    if num == '2' or num == 2:
        return True
    
    return False

print('\n1)')
print('Testing function "is_two":')
print(f'Result when input is "2": {is_two("2")}')
print(f'Result when input is 2: {is_two(2)}')
print(f'Result when input is "two": {is_two("two")}')

#Define a function named is_vowel. It should return True if the passed string is a vowel, False otherwise.
def is_vowel(string):
    if string == 'a' or string == 'e' or string == 'i' or string == 'o' or string == 'u':
        return True
    
    return False

print('\n2)')
print('Testing function "is_vowel":')
print(f'Result when input is "e": {is_vowel("e")}')
print(f'Result when input is "b": {is_vowel("b")}')

#Define a function named is_consonant. It should return True if the passed string is a consonant, False otherwise. 
#Use your is_vowel function to accomplish this.
def is_consonant(string):
    if is_vowel(string) == False:
        return True

    return False

print('\n3)')
print('Testing function "is_consonant":')
print(f'Result when input is "e": {is_consonant("e")}')
print(f'Result when input is "b": {is_consonant("b")}')

#Define a function that accepts a string that is a word. The function should capitalize the first letter of the word if the word starts with a consonant.
def capitalize_consonant(string):
    if is_consonant(string[0]) == True:
        return string.capitalize()
    
    return string

print('\n4)')
print('Testing function "capitalize_consonant":')
print(f'Result when input is "bridge": {capitalize_consonant("bridge")}')
print(f'Result when input is "apple": {capitalize_consonant("apple")}')

#Define a function named calculate_tip. It should accept a tip percentage (a number between 0 and 1) and the bill total, and return the amount to tip.
def calculate_tip(percent, bill_total):
    return bill_total * percent

print('\n5)')
print('Testing function "calculate_tip":')
print(f'Result when input is .15, 10: {calculate_tip(.15, 10)}')
print(f'Result when input is .25, 60: {calculate_tip(.25, 60)}')

#Define a function named apply_discount. It should accept a original price, and a discount percentage, and return the price after the discount is applied.
def apply_discount(price, discount):
    discounted_price = price - (price * discount)
    return discounted_price

print('\n6)')
print('Testing function "apply_discount":')
print(f'Result when input is 100, .10: {apply_discount(100, .10)}')
print(f'Result when input is 50, .30: {apply_discount(50, .30)}')

#Define a function named handle_commas. It should accept a string that is a number that contains commas in it as input, and return a number as output.
def handle_commas(num_with_commas):
    return int(num_with_commas.replace(",",""))

#Define a function named get_letter_grade. It should accept a number and return the letter grade associated with that number (A-F).
def get_letter_grade(number_grade):
    if number_grade < 70:
        return 'F'
    elif number_grade < 75:
        return 'D'
    elif number_grade < 80:
        return 'C'
    elif number_grade < 90:
        return 'B'
    else:
        return 'A'

#Define a function named remove_vowels that accepts a string and returns a string with all the vowels removed.
def remove_vowels(string):
    string.replace('a','')
    string.replace('e','')
    string.replace('i','')
    string.replace('o','')
    string.replace('u','')

    return string

#Define a function named normalize_name. It should accept a string and return a valid python identifier, that is:
#anything that is not a valid python identifier should be removed
#leading and trailing whitespace should be removed
#everything should be lowercase
#spaces should be replaced with underscores
#for example:
#Name will become name
#First Name will become first_name
#% Completed will become completed
def normalize_name(string):
    string.strip()
    string.replace(' ', '_')
    string.lower()

    return string

#Write a function named cumulative_sum that accepts a list of numbers and returns a list that is the cumulative sum of the numbers in the list.
#cumulative_sum([1, 1, 1]) returns [1, 2, 3]
#cumulative_sum([1, 2, 3, 4]) returns [1, 3, 6, 10]
def cumulative_sum(numbers):
    new_list = []
    num_sum = 0

    for number in numbers:
        num_sum += number
        new_list.append(num_sum)
    
    return new_list

