

t=int(input())

while t:
    n,m=map(int,input().split())
    if n < m:
        exit(0)

    m_values=list(map(int,input().split()))

    m_values.sort()

    chef=[]
    ass=[]
    count=0
    for i in range(1,n+1):
        if i in m_values:
            continue
        else:
            chef.append(i) if (count%2==0) else ass.append(i)
            count=count+1

    print(*chef, sep=' ')
    print(*ass,sep=' ')
    t=t-1
