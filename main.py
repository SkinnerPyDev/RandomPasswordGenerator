import string
import random

pass_list = string.ascii_lowercase+string.ascii_uppercase+string.digits+string.punctuation
pass_lenght = int(input("Enter the lenght of the password: "))
password = ""
for i in range(0,pass_lenght):
    passchar = random.choice(pass_list)
    password = password+passchar
print(f"Your password is: {password}")