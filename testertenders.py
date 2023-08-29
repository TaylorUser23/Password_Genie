import random
import datetime

def generate_password(length=13):
    characters = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
    numbers = "0123456789"
    special_characters = "!@#$%*_~"

    all_characters = characters + numbers


    password = ''.join(random.choice(all_characters) for _ in range(length))

    g = password + random.choice(special_characters)

    return g

 
password_length = int(input("Enter the desired password length: ")) - 1

generated_password = generate_password(password_length)
print("Generated Password:", generated_password)        

file_path = r'C:\Users\Taylor\Desktop\Passwords.txt'

v= str(datetime.datetime.now())

with open(file_path, 'w') as file:
    file.write(generated_password + '\n')
    file.write(v)
print("Your password has been saved to this file:" , file_path)
#figure out how to make the output look cleaner like a string, prob check the a and b variable and try those as strings
#also, try print it to a text doc somewhere eveytime it makes a password
#print(dir(random))