print("Калькулятор v1.0")

a = float( input("Напишите первое число: ") )
b = float( input("Напишите второе число: ") )

znak = input("Выберите знак: +, - : ")
print("Вы выбрали: ", znak)

if znak == "+":
    c = a + b   
    print("Ответ: ", c)

elif znak == "-":
    c = a - b
    print("Ответ: ", c)
    

else:
    print("Выберите правильный знак!")


print("vk.com/whoisrockstar")

input()