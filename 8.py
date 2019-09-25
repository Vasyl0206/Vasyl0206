# #EX1 Написати функцію, яка знаходить середнє арифметичне значення довільної кількості чисел
# def ser_num (*args):
#     '''Seredne'''
#     return sum(args)/len(args)
# print (ser_num(2,4))

# #EX2 Написати функцію, яка повертає абсолютне значення числа
# def abso (arg):
#     '''absolutne'''
#     if arg < 0: 
#         arg= arg * (-1)
#     return arg

# print (abso(-51))

# #EX3 Написати функцію, яка знаходить максимальне число з двох чисел, 
# # а також в функції використати рядки документації DocStrings.

# def maks(arg1,arg2):
#     '''Maximal'''
#     if arg1>arg2:
#         print ('max= ',arg1)
#     else: 
#         print ('max= ',arg2)    
#     return 
# print (maks (1,2))    

# #Ex4Написати програму, яка обчислює площу прямокутника, трикутника та кола (написати три функції 
# #для обчислення площі, і викликати їх в головній програмі в залежності від вибору користувача)

# def pl_pryam (arg1,arg2):
#     plowa = arg1 * arg2
#     return plowa
# def pl_truk (arg1,arg2):
#     plowa2 = (arg1+arg2)/2
#     return plowa2
# def pl_kola (arg):
#     plowa3 = 3.14 * arg**2
#     return plowa3
# choi = int (input (' 1-Площа прямокутника \n 2-Площа трикутника \n 3-Площа кола \n Зробіть вибір:'))
# if choi == 1:
#     a = int (input ('Ведіть значення,в м "а" '))
#     b = int (input ('Ведіть значення,в м "b" '))
#     print ('Площа Прямокутника рівна - ', pl_pryam(a,b), 'м2')
# elif choi == 2:
#     a = int (input ('Ведіть значення,в м "c" '))
#     h = int (input ('Ведіть значення,в м "h" '))
#     print ('Площа Трикутника рівна - ', pl_truk(a,h), 'м2')
# elif choi == 3:
#     r = int (input ('Ведіть значення,в м "r" '))
#     print ('Площа Кола рівна - ', pl_kola(r), 'м2')
# else:
#     print ('Невірний вибір',)

# #EX5 Написати функцію, яка обчислює суму цифр введеного числа

# def syma(arg):
#     suma = 0
#     while arg > 0:
#         suma = suma + arg%10
#         arg = arg //10
#     return suma
# num = int (input ('Введіть число: '))
# print ('Сума = ', syma(num))

# #EX6 Написати програму калькулятор, яка складається з наступних функцій: 
# #головної, яка пропонує вибрати дію та додаткових, які реалізовують вибрані 
# # дії, калькулятор працює доти, поки ми не виберемо дію вийти з калькулятора, 
# # після виходу, користувач отримує повідомлення з подякою за вибір нашого програмного продукту!!!

def syma(arg1,arg2):
    a = arg1 + arg2
    return a
def riznuca(arg1,arg2):
    b = arg1 - arg2
    return b
def dobytok(arg1, arg2):
    c = arg1 * arg2
    return c
def chastka(arg1, arg2):
    d = arg1 / arg2
    return d
def calc(x):
    x =str(input('Виберіть дію (+,-,*,/,exit )'))
    while x == '+' or x == '-' or x == '*' or x == '/':
        if x == '+':
            a = int (input ('Ведіть значення "а" '))
            b = int (input ('Ведіть значення "b" '))
            print ('СУМА = ', syma(a,b))
            calc('x')
        elif x == '-':
            a = int (input ('Ведіть значення "а" '))
            b = int (input ('Ведіть значення "b" '))
            print ('РІЗНИЦЯ = ', riznuca(a,b))
            calc('x')
        elif x == '*':
            a = int (input ('Ведіть значення "а" '))
            b = int (input ('Ведіть значення "b" '))
            print ('ДОБУТОК = ', dobytok(a,b))
            calc('x')
        elif x == '/':
            a = int (input ('Ведіть значення "а" '))
            b = int (input ('Ведіть значення "b" '))
            print ('ЧАСТКА = ', chastka(a,b))
            calc('x')
    if x == 'exit':
        # break
        print ('Подяка за вибір нашого програмного продукту!')
    else:
        print ('Error')
        calc('x')
    
    return x
calc('x')



    
    


