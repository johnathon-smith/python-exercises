#Write some python code to describe the following situations. 

#You have rented some movies for your kids: The little mermaid (for 3 days),
# Brother Bear (for 5 days, they love it), 
# and Hercules (1 day, you don't know yet if they're going to like it). 
# If price for a movie per day is 3 dollars, how much will you have to pay?

num_movies = 3
days_rented = 9
price_per_day = 3
total_price = days_rented * price_per_day

#Suppose you're working as a contractor for 3 companies: Google, Amazon and Facebook, 
#they pay you a different rate per hour. Google pays 400 dollars per hour, Amazon 380, 
#and Facebook 350. How much will you receive in payment for this week? You worked 10 hours for Facebook, 
#6 hours for Google and 4 hours for Amazon.

facebook_rate = 350
google_rate = 400
amazon_rate = 380

facebook_hours_worked = 10
google_hours_worked = 6
amazon_hours_worked = 4

total_pay = (facebook_hours_worked * facebook_rate) + (google_rate * google_hours_worked) + (amazon_hours_worked * amazon_rate)


#A student can be enrolled to a class only if the class is not full and the class schedule 
#does not conflict with her current schedule.

class_is_not_full = True
no_schedule_conflict = True
can_enroll = class_is_not_full and no_schedule_conflict

#A product offer can be applied only if people buys more than 2 items, and the offer has not expired.
#Premium members do not need to buy a specific amount of products.

is_premium_member = True
offer_is_valid = True
num_items = 2

offer_applied = offer_is_valid and (is_premium_member or num_items > 2)

#Use the following code to follow the instructions below:
username = 'codeup'
password = 'notastrongpassword'

#Create a variable that holds a boolean value for each of the following conditions:
#the password must be at least 5 characters
password_is_at_least_5_characters = len(password) >= 5
#the username must be no more than 20 characters
username_is_less_than_20_characters = len(username) < 20
#the password must not be the same as the username
password_does_not_equal_username = password != username
#bonus neither the username or password can start or end with whitespace
does_not_start_or_end_with_whitespace = (username[0] != ' ' and username[-1] != ' ') and (password[0] != ' ' and password[-1] != ' ')