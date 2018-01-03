import math

t=int(input())

n,k=map(int,input().split())
x,y,sum='',0,0
possible=[]
young=[]
for i in range(0,n):
    for j in range(0,n):
        if i==j:
            x+='0'
        elif y<math.sqrt(k):
            x+='1'
            y+=1
        else:
            x+='0'
        possible.append(y)
        print(x)
        young.append(x)
    for b in range(len(possible)):
        sum+=pow(possible[b],2)
    if sum == k:
        print(young)
