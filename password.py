# random password generator
import random

print("Your password: ")

#possible password characters
chars = 'qwertyuiopasdfghjklzxcvbnm1234567890!@#$%^&*()?'

password =""

#16 is the length of the password 
for i in range(16):
    password += random.choice(chars)

print (password)