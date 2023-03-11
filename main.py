import random

name = input("Enter your name here: ")
how_many = input("How many iterations do you need: ")

def password_gen(names):
    #Add space to the string
    name_space = ''
    for ch in name:
        name_space = name_space + ch + ' '

    name_arr = name_space.split()

    special_chars = ['!', '@', '#', '$', '%', '^', '&', '*', '_', '-', '+', '=', '`', '|', "(", ")", '{', '}', ':', ';', '<', '>', ',', '.', '?', '/', '1', '2', '3', '4', '5', '6']

    password_generated = []

    #Adds the special characters and the name characters to the password_generated variable
    for i in name_arr:
        password_generated.append(special_chars[random.randint(0, len(special_chars)-1)])
        password_generated.insert(random.randint(0, len(name_arr)-1), i)

    #Convert the password_generated list to a string
    password = ''.join(password_generated)
    return password

count_int = int(how_many)
count = 0

while count< count_int:
    print(password_gen(name))
    count += 1