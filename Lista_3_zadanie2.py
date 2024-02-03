import random
import array

max_len = 12

symbols = ['@', '#', '$', '%', '=', ':', '?', '.', '/',
           '|', '~', '>', '*', '(', ')', '<']

digits = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']

small_letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'm',
                'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

uppercase = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'M', 'N', 'O',
             'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']

symbols_list = symbols + digits + small_letters + uppercase

rand_digit = random.choice(digits)
rand_upper = random.choice(uppercase)
rand_lower = random.choice(small_letters)
rand_symbol = random.choice(symbols)

random_list = rand_digit + rand_upper + rand_lower + rand_symbol

for x in range(max_len):
    temp_pass = random_list + random.choice(symbols_list)

    temp_pass_list = array.array('u', temp_pass)
    random.shuffle(temp_pass_list)

password = ""
for x in temp_pass_list:
    password = password + x

print(password)
