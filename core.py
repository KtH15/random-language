#استدعاء مكتبة random
import random
#تعين كلمات الOutput
chars = 'ABCDEFGHIJKLMONPQRSTUVWXYZabcdefghijklmnobqrstuvwxyz'
#انشاء الداله المسؤلة عن اللغة
def random_lang ():
    code_input = str(input("~$ "))
    result = ""
    for _ in code_input:
        result += random.choice(chars)
    print(result)
#تشغيل الداله
random_lang()