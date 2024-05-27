import random
print('Hello world')
code = "+-/*!&$#?=@abcdefghijklnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890"
p_length = int(input('Podaj numerycznie długośc hasła:'))
password = ''
for i in range(p_length):
    password += code[random.randint(0, len(code))]
print(password)
