import random

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '', '+']

total_list = letters + numbers + symbols 

print("Welcome to the Password Generator!!")
total_letters = int(input("How many letters do you want to have? "))
total_numbers = int(input("How many numbers do you want to have? "))
total_symbols = int(input("How many symbols do you want to have? "))

total = total_letters + total_numbers + total_symbols

password = ''
for i in range(total):
    password += random.choice(total_list)

print(f"Your new password is {password}!")
