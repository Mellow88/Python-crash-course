"""HW_5"""

users = ['olha', 'ihor', 'natali']
user_name = 'natali'

if user_name in users:
    print(f"{user_name.title()}, exist in list \n")


alien_colors = ['green', 'yellow', 'red']
alien_destroy = 'green'

for alien_color in alien_colors:
    if alien_color == alien_destroy:
        message = f"You kill {alien_color} alien. You get 10 points"
        print(message)
    elif alien_color == 'yellow':
        message = f"You kill {alien_color} alien. You get 5 points"
        print(message)
    else:
        message = f"You kill {alien_color} alien. You get 15 points"
        print(message)

curent_users = ['eric', 'willie', 'admin', 'erin', 'Ever']
new_users = ['sarah', 'Willie', 'PHIL', 'ever', 'Iona']

copy_users = [value.lower() for value in curent_users]

for user in new_users:
    if user.lower() in copy_users:
        print(f"Sorry {user}, that name is taken.")
    else:
        print(f"Great, {user} is still available.")
