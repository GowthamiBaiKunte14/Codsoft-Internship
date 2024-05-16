import random
import string
length = int(input("Enter Length: "))

uppercase_letters = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
lowercase_letters =  uppercase_letters.lower()
digits = "0123456789"
symbols = "()[]{},;:._-/\\?+*#@"

upper, lower, nums, syms = True, True, True, True

all = ""

chars = string.ascii_letters
chars += string.digits
chars += string.punctuation

password = ''.join([random.choice(chars) for i in range(length)])

for i in range(length):
    password += random.choice(chars)
   
if upper:
    all += uppercase_letters
if lower:
    all += lowercase_letters
if nums:
    all += digits
if syms:
    all += symbols

print("Your random passwors is:",password)
print(string.ascii_letters)
print(string.digits)
print(string.punctuation)