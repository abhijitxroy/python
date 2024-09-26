import random
import string

alphabets = string.ascii_letters
digits = string.digits
wild_characters = string.punctuation

allValues = alphabets+digits+wild_characters;
# print(allValues)

def generate_password(pwd_length):
    pwd = ''
    for i in range(pwd_length):
        
        pickRandomValue = random.choice(allValues)
        pwd += str(pickRandomValue)
    print('Your', pwd_length, 'Digit OTP:',pwd)

# print n length password
pwd_length = 6
generate_password(pwd_length)