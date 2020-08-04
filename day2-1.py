import random
A=random. randint(1,10)
B=input('請輸入1-10中的一個數字') 
B=int(B) 
if A==B:
    print('correct')
elif B<1 or B>10:
    print('error')
else:
    print('wrong')