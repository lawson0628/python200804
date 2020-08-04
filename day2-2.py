import random
A=random.randint(1,10)
while True:
    B=input('請輸入1-10中的一個數字') 
    B=int(B) 
    if A==B:
        print('correct')
        break
    elif B<1 or B>10:
        print('error type in again')
    else:
        print('wrong')