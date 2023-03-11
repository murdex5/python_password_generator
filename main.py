name = input("Enter your name here: ")
name_space = ''
for ch in name:
   name_space = name_space + ch + ' '
# print(result[:-1])

name_arr = name_space.split()
# print(name_arr)

special_chars = ['!', '@', '#', '$', '%', '^', '&', '*', '_', '-', '+', '=', '`', '|', "(", ")", '{', '}', '[', ']', ':', ';', '<', '>', ',', '.', '?', '/']

password_generated = ""