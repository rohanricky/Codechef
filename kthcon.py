def hull():
    if n<3:
        return
    hull=[]
    l=0
    for i in range(1,n):
        if point[i].x<point[l].x:
            l=i

    p=l
    while True:
        hull.append(point[p])
        q=(p+1)%n
        for i in range(n):
            if orientation(point[p],point[i],point[q]) == 2:
                q=i
        p=q
        if p==l:
            break

    print("gap")
    for i in range(len(hull)):
        print(str(hull[i].x)+" "+str(hull[i].y))

def orientation(p,q,r):
    val = (q.y - p.y) * (r.x - q.x) -(q.x - p.x) * (r.y - q.y)
    if val==0:
        return
    return 1 if (val>0) else 2

class Point:
    def __init__(self,x,y):
        self.x=x
        self.y=y

n = int(input())
point=[]
area=0
for i in range(n):
    i,j=map(int,input().split())
    point.append(Point(i,j))

hull()
