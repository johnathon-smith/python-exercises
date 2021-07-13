#Define a function named is_two. It should accept one input and return True if the passed input is either the number or the string 2, False otherwise.
def is_two(num):
    if num == '2' or num == 2:
        return True
    
    return False



#Define a function named is_vowel. It should return True if the passed string is a vowel, False otherwise.
def is_vowel(string):
    if string in 'aeiou':
        return True
    
    return False



#Define a function named is_consonant. It should return True if the passed string is a consonant, False otherwise. 
#Use your is_vowel function to accomplish this.
def is_consonant(string):
    if is_vowel(string) == False: #Used is_vowel function to determine that it is not a vowel, therefore, must be a consonant
        return True

    return False



#Define a function that accepts a string that is a word. The function should capitalize the first letter of the word if the word starts with a consonant.
def capitalize_consonant(string):
    if is_consonant(string[0]) == True: #Check if the first letter of the string argument starts with a consonant
        return string.capitalize() #return the string with the first letter capitalized
    
    return string #otherwise, return the original string



#Define a function named calculate_tip. It should accept a tip percentage (a number between 0 and 1) and the bill total, and return the amount to tip.
#This function has the parameters percent(float), and bill_total(int) and returns a float.
def calculate_tip(percent, bill_total):
    return bill_total * percent



#Define a function named apply_discount. It should accept a original price, and a discount percentage, and return the price after the discount is applied.
#This function has the parameters price(float or int) and discount(float) and returns a float value
def apply_discount(price, discount):
    discounted_price = price - (price * discount)
    return discounted_price



#Define a function named handle_commas. It should accept a string that is a number that contains commas in it as input, and return a number as output.
def handle_commas(num_with_commas):
    return int(num_with_commas.replace(",","")) #replace all the commas with empty strings and return


#Define a function named get_letter_grade. It should accept a number and return the letter grade associated with that number (A-F).
def get_letter_grade(number_grade):
    if number_grade < 70: #(0-69 = F)
        return 'F'
    elif number_grade < 75: #(70-74 = D)
        return 'D'
    elif number_grade < 80: #(75-79 = C)
        return 'C'
    elif number_grade < 90: #(80-89 = B)
        return 'B'
    else:
        return 'A' #(90 and above = A)



#Define a function named remove_vowels that accepts a string and returns a string with all the vowels removed.
def remove_vowels(string):
    return string.replace('a','').replace('e','').replace('i','').replace('o','').replace('u','') #replace all the vowels with empty strings and return



#Define a function named normalize_name. It should accept a string and return a valid python identifier, that is:
#anything that is not a valid python identifier should be removed
#leading and trailing whitespace should be removed
#everything should be lowercase
#spaces should be replaced with underscores

import keyword #This is needed to check for reserved keywords in the following function
def normalize_name(string):
    for character in string:
        if character == ' ': #since I don't want to remove all of the spaces, I chose to skip those here
            continue
        if character.isidentifier() == False: #This will check each character. If it is not a valid identifier, it will replace it with an empty string 
            string = string.replace(character, '')

    while string[0].isdigit() == True: #looks for leading digits and removes them 
        string = string.replace(string[0], '')
    
    string = string.strip() #removes leading and trailing whitespace
    string = string.replace(' ', '_') #replaces internal whitespaces with underscores
    string = string.lower() #puts everything in lower case

    if keyword.iskeyword(string) == True:
        print("The new string is a keyword in Python and connot be used as a valid identifier.")
        return "Invalid"
    else:
        return string


#Write a function named cumulative_sum that accepts a list of numbers and returns a list that is the cumulative sum of the numbers in the list.
#cumulative_sum([1, 1, 1]) returns [1, 2, 3]
#cumulative_sum([1, 2, 3, 4]) returns [1, 3, 6, 10]
def cumulative_sum(numbers):
    new_list = [] #This list will contain the new numbers and will be returned at the end
    num_sum = 0 #This keeps track of the cumulative sum

    for number in numbers: #For each number in the numbers list
        num_sum += number #calculate the new cumulative sum
        new_list.append(num_sum) #add the new cumulative sum to the new_list
    
    return new_list



#Bonus
#Create a function named twelveto24. It should accept a string in the format 10:45am or 4:30pm 
#and return a string that is the representation of the time in a 24-hour format.
def twelveto24(time):
    if time[-2] == 'a': #Checks the second to last char to determine if the input time is 'am' or 'pm'
        key = 'am'
    else:
        key = 'pm'
    
    for character in time: #checks each character in the time string and removes any that are not digits
        if character.isdigit() == False:
            time = time.replace(character, '')
        
    if key == 'am': #if input time was 'am', and the hour number is a single digit, add a leading '0' that is often found in morning military time.
        if len(time) == 3:
            return '0' + time
        else: #otherwise, if the hour number is two digits long, just return the time
            return time
    else: #if input time was 'pm', convert to int and add 1200 to get the appropriate digits for military time
        new_time = int(time) + 1200
        return str(new_time) #convert the int new_time to str and return



#Write a function that does the oppostie of twelveto24.
def mil_to_civ_time(time):
    #There are a couple of base cases we need to cover: if the time is 1200, or if the time is 2400 or 0000
    if time == '1200':
        return '12:00pm'
    elif time == '2400' or time == '0000':
        return '12:00am'
    
    new_time = int(time) #Convert to int to make it easier to determine if the time is am or pm
    
    if new_time < 1200: #if less than 1200, the time is am, otherwise, the time is pm
        time = time + 'am' #adds the 'am' mark to the time string
        if time[0] == '0': #checks for and removes the leading '0' often found in morning military time
            time = time.replace('0','',1)
    else: #time is pm
        new_time = new_time - 1200 #used the int version of time and subtracted 1200 to get the appropriate civ time digits (ex: 1700 - 1200 = 500)
        time = str(new_time) + 'pm' #converts new_time to a string and adds the 'pm' mark to the time string

    time_list = list(time) #convert the time string to a list. This allows me to insert the ':' at any location

    if len(time_list) == 6: #checks to see if the hour is greater than 1 digit long so that I know where to insert the ':'. (ex: 930am only has 5 chars, but 1230am has 6)
        time_list.insert(2,':')
    else:
        time_list.insert(1,':')

    time = '' #assign an empty string to 'time' so that I can concatenate the chars from the time_list
    for item in time_list:
        time = time + item #concatenates each char in time_list

    return time
    


#Create a function named col_index. It should accept a spreadsheet column name, and return the index number of the column.
def col_index(col_name):
    multiplier = (len(col_name) - 1) * 26 #This determines the base value of the input column name (not including the last letter)

    index = multiplier + ( ord( col_name[-1].upper() ) - 64 ) #add the ascii value of the last letter in the col_name - 64. This makes the value of 'A' = 1, 'B' = 2, and so on
    return index


#Set up an if statement to prevent the print statements from running when importing this file
if __name__ == '__main__':
    print('\n1)')
    print('Testing function "is_two":')
    print(f'Result when input is "2": {is_two("2")}')
    print(f'Result when input is 2: {is_two(2)}')
    print(f'Result when input is "two": {is_two("two")}')

    print('\n2)')
    print('Testing function "is_vowel":')
    print(f'Result when input is "e": {is_vowel("e")}')
    print(f'Result when input is "b": {is_vowel("b")}')

    print('\n3)')
    print('Testing function "is_consonant":')
    print(f'Result when input is "e": {is_consonant("e")}')
    print(f'Result when input is "b": {is_consonant("b")}')

    print('\n4)')
    print('Testing function "capitalize_consonant":')
    print(f'Result when input is "bridge": {capitalize_consonant("bridge")}')
    print(f'Result when input is "apple": {capitalize_consonant("apple")}')

    print('\n5)')
    print('Testing function "calculate_tip":')
    print(f'Result when input is .15, 10: {calculate_tip(.15, 10)}')
    print(f'Result when input is .25, 60: {calculate_tip(.25, 60)}')

    print('\n6)')
    print('Testing function "apply_discount":')
    print(f'Result when input is 100, .10: {apply_discount(100, .10)}')
    print(f'Result when input is 50, .30: {apply_discount(50, .30)}')

    print('\n7)')
    print('Testing function "handle_commas":')
    print(f'Result when input is "1,000,000": {handle_commas("1,000,000")}')

    print('\n8)')
    print('Testing function "get_letter_grade"')
    print(f'Result when input is 88: {get_letter_grade(88)}')
    print(f'Result when input grade is 65: {get_letter_grade(65)}')

    print('\n9)')
    print('Testing function "remove_vowels":')
    print(f'Result when input is "laeioul": {remove_vowels("laeioul")}')

    print('\n10)')
    print('Testing function "normalize_name":')
    print(f'Result when input is "%2335Joh*n Smith": {normalize_name("%2335Joh*n Smith")}')
    print(f'Result when input is "85@ LONG sEnTeNcE": {normalize_name("85@ LONG sEnTeNcE")}')
    print(f'Result when input is "% 33de*f @": {normalize_name("% 33de*f @")}')

    print('\n11)')
    print('Testing function "cumulative_sum":')
    print(f'Result when input is [1,3,5,8]: {cumulative_sum([1,3,5,8])}')
    print(f'Result when input is [1,2,3,4]: {cumulative_sum([1,2,3,4])}')

    print('\nBonus 1)')
    print('Testing function "twelveto24":')
    print(f'Result when input is "5:30am": {twelveto24("5:30am")}')
    print(f'Result when input is "5:30pm": {twelveto24("5:30pm")}')

    print('\nBonus 2)')
    print('Testing function "mil_to_civ_time":')
    print(f'Result when input is "0000": {mil_to_civ_time("0000")}')
    print(f'Result when input is "0530": {mil_to_civ_time("0530")}')
    print(f'Result when input is "1730": {mil_to_civ_time("1730")}')
    print(f'Result when input is "2400": {mil_to_civ_time("2400")}')

    print('\nBonus 3)')
    print('Testing function "col_index":')
    print(f'Result when input is "A": {col_index("A")}')
    print(f'Result when input is "Aa": {col_index("Aa")}')
    print(f'Result when input is "az": {col_index("az")}')



