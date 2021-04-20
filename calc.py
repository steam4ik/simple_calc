print("Калькулятор v1.0")

from colorama import init
from colorama import Fore, Back, Style
init()

print( Back.CYAN )
a = float( input("Напишите первое число: ") )
b = float( input("Напишите второе число: ") )

print( Back.BLUE )

znak = input("Выберите знак: +, - : ")
print("Вы выбрали: ", znak)

print( Back.YELLOW )
if znak == "+":
    c = a + b   
    print("Ответ: ", c)

elif znak == "-":
    c = a - b
    print("Ответ: ", c)
    

else:
    print("Выберите правильный знак!")

print( Back.WHITE )


print("vk.com/whoisrockstar")

print(	Back.BLUE )
print("Copy ↑")

input()