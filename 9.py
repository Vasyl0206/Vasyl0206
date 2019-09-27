# 1.  Напишіть скрипт-гру, яка генерує випадковим чином число з діапазону чисел від 1 до 100 
# і пропонує користувачу вгадати це число. Програма зчитує числа, які вводить користувач і видає 
# користувачу підказки про те чи загадане число більше чи менше за введене користувачем. Гра має 
# тривати до моменту поки користувач не введе число, яке загадане програмою, тоді друкує повідомлення привітання. 
#(для виконання завдання необхідно імпортувати  модуль random, а з нього функцію randint())

# import random
# num_rand = random.randint(0,101)

# def rand(num):
#     num = int (input ('Guess a number: '))
#     while 0<num<101:
        
       
#         if num > num_rand:
#             print ('Guesses number is less')
#             rand('num')
#         elif num < num_rand:
#             print ('Guesses number is bigger')
#             rand('num')
#         elif num == num_rand:            
#             print ('Congratulations! The right number is ' , + num_rand)
                   
#     else:
#         print ('Write a number from 0 to 100')
#         rand('num')
#     return num    
# rand('num')


# 2.  Напишіть скрипт, який обчислює площу прямокутника a*b, площу трикутника 0.5*h*a, площу кола pi*r**2. 
#(для виконання завдання необхідно імпортувати  модуль math, а з нього функцію pow() та значення змінної пі).
import math

choi = int (input (' 1-Площа прямокутника \n 2-Площа трикутника \n 3-Площа кола \n Зробіть вибір:'))
if choi == 1:
    a = int (input ('Ведіть значення,в м "а" '))
    b = int (input ('Ведіть значення,в м "b" '))
    print ('Площа Прямокутника рівна - ', a*b, 'м2')
elif choi == 2:
    c = int (input ('Ведіть значення,в м "c" '))
    h = int (input ('Ведіть значення,в м "h" '))
    print ('Площа Трикутника рівна - ', 0.5*h*c, 'м2')
elif choi == 3:
    r = int (input ('Ведіть значення,в м "r" '))
    print ('Площа Кола рівна - ', math.pi * math.pow(r,2), 'м2')
else:
    print ('Невірний вибір',)



