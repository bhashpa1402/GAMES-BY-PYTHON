import string
import random

pwd_len = int(input("Enter the length of password : "))

# deciding char for password
char_pwd = (string.ascii_letters) + (string.digits) + (string.punctuation)

# making to password as string

pwd = "".join([random.choice(char_pwd) for i in range(pwd_len)])

# .join helps to create whole list as one string

print(pwd)