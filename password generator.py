#  Программа, генерирующая 8-значные пароли, содержащие хотя бы одну прописную букву, строчную букву и цифру.

import string


small_letters = list(string.ascii_lowercase)
capital_letters = list(string.ascii_uppercase)
numbers = [i for i in range(10)]
characters = small_letters + capital_letters + numbers

while True:
    try:
        choice = int(input('wanna generate a random password consisting of at least one capital letter,'
                           'one small letter and one number?\nenter 1 for yes or 0 for exit\n'))
        if choice == 0:
            print('okay bye!\n')
            break
        if choice == 1:
            print('okay\n')
        else:
            print('wrong number!\n')
    except ValueError:
            print('integers only!\n')



