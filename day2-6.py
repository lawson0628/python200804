names=[]
scores=[]
total=0
highest=0
lowest=10000000
number=int(input('請輸入班上有多少人'))
for a in range(number):
    name=input('請輸入名字')
    score=int(input('請輸入分數'))
    names.append(name)
    scores.append(score)
    
for b in range(number):
    total=scores[b]+total
print(total)
average=float(total/number)
print(average)

for c in range(number):
    if scores[c]>highest:
        highest=scores[c]
print('最高分是',int(highest))

for d in range(number):
    if scores[d]<lowest:
        lowest=scores[d]
print('最低分是',int(lowest))