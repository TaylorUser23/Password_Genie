import random
import datetime

def generate_password(length=13):
    #The available characters, numbers, and spec chars
    characters = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
    numbers = "0123456789"
    special_characters = "!@#$%*_~"
    
    #Adding chars and numbers first
    all_characters = characters + numbers

    #joining random numbers and chars for length in range 
    password = ''.join(random.choice(all_characters) for _ in range(length))
    #adding one spec char at the end of my chars and numbs
    g = password + random.choice(special_characters)

    return g

#take user input for length of char,num,spec char
password_length = int(input("Enter the desired password length: ")) - 1
#calling my function
generated_password = generate_password(password_length)
print("Generated Password:", generated_password)        

#printing password to this file path
file_path = r'C:\Users\Taylor\Desktop\Passwords.txt'
#file path must be changed to a path specific to your machine
#getting date and time from library
v= str(datetime.datetime.now())
#writing password and time to the file path mentioned earlier
with open(file_path, 'w') as file:
    file.write(generated_password + '\n')
    file.write(v)
print("Your password has been saved to this file:" , file_path)



#print(dir(random))