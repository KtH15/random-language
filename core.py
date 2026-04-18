import random
chars = 'ABCDEFGHIJKLMONPQRSTUVWXYZabcdefghijklmnobqrstuvwxyz'
def random_lang ():
    code_input = str(input("~$ "))
    result = ""
    for _ in code_input:
        result += random.choice(chars)
    print(result)
random_lang()
