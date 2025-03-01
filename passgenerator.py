import random
import string

print("Password Generator")
length = int(input("Enter the desired password length: "))

all_chars = string.ascii_letters + string.digits
password = "".join(random.choice(all_chars) for _ in range(length))

print("Your generated password:", password)