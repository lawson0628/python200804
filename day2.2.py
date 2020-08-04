n=int(input('請輸入一個數來判別它是否為質數'))
c=2
while c<n:
        if n%c==0:
            print('不是質數')
            break
        c+=1 
if c==n:
            print('是質數')
    