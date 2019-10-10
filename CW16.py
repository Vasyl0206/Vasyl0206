def solution(number):
    num = 0
    for i in range(1,number):
        if i %3 == 0 or i%5 == 0:
            num += i
    return num
            
    




