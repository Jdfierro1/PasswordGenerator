
import random

def password_generator():
    alphabet = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
    characters = ['!','@','#','$','%','^','&','*','(',')','/','?']
    upper = random.choices(alphabet, k=7)
    lower = random.choices(alphabet, k=8)
    special = random.choices(characters,k=3)
    lower = [char.lower() for char in lower]
    password_list = upper + lower + special 
    random.shuffle(password_list)
    shuffled_password = ''.join(password_list)
    final = '-'.join([shuffled_password[i:i+4] for i in range(0, len(shuffled_password), 4)])
    return final

test = password_generator()
print(test)