import random
A=random.randint(1,20)
I=0
while True:
    B=input('請輸入1-20中的一個數字') 
    B=int(B) 
    if A<B:
        print('太大 只能猜五次喔')
    if A==B:
        print("猜對了")
        break
    if A>B:
        print('太小 只能猜五次喔')  
    elif B<1 or B>20:
        print('error type in again')
    
    I=I+1
    if I==5:
        print("正確答案是"+str(A))
        break
    
     