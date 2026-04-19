import random
import string
def generate_password(length):
    characters = string.ascii_letters + string.digits + string.punctuation
    return ''.join(random.choice(characters) for _ in range(length))

while True:
    try:
        length = int(input("enter the length of the password:"))

        if length <= 0:
            print("length must be grater than 0" )
            continue
        password = generate_password(length)
        print("Generated Password:", password)
        break
    except ValueError:
        print("please enter a valid number")



