def select(a,b,x1,y1,x2,y2):
    X1=max(0,x1)
    Y1=max(0,y1)
    X2=min(a,x2)
    Y2=min(b,y2)
    return (X2-X1)*(Y2-Y1)
n,a,b=map(int,input().split())
summary=0
for i in range(n):
    x1,y1,x2,y2=map(int,input().split())
    summary+=select(a,b,x1,y1,x2,y2)


print(summary)
