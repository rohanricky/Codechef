n=int(input())

count=0
great=0
flag=0
for i in range(2,int(n/2)+1):
    if not n%i==0:
        continue
    for j in range(2,int(i/2)+1):
        if i%j==0:
            break
        else:
            flag=0
            break
    if flag==0:
        great=i

print(great)

#Max input 8 digit no.
