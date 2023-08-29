import random

def generate_password(length=13):
    characters = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
    numbers = "0123456789"
    special_characters = "!@#$%^&*()_+=-[]{}|;:,.<>?~"

    all_characters = characters + numbers


    password = ''.join(random.choice(all_characters) for _ in range(length))

    g = password + random.choice(special_characters)

    return g


password_length = int(input("Enter the desired password length: "))

generated_password = generate_password(password_length)
print("Generated Password:", generated_password) 

#cant print to txt using a function, must be a string
#with open('Passwords.txt', 'a') as f:
    #f.write('Here is your generated password:')
    #f.write(generate_password)
    #f.close()


#print(dir(random))
