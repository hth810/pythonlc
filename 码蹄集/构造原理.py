def f(summ,refer,x,i,j):
    summ[i][j]=min(x,refer[j])
    y=x-refer[j]
    if y<=0:
        return
    if j==1:
        j=i//2+1
        i=(i+1)//2+1
    else:
        j-=1
        i+=1
    f(summ,refer,y,i,j)
    return summ


n=int(input())
summ=[[0 for i in range(5)] for j in range(10)]
refer=[0,2,6,10,14]
ch='&spdf'
newSum=f(summ,refer,n,1,1)
i=1
flag=False
while True:
    for j in range(1,5):
        if not newSum[i][1]:
            flag=True
            break
        if newSum[i][j]:
            print(i,end='')
            print(ch[j],end='')
            print(newSum[i][j],end=' ')
    print()
    i+=1
    if flag:
        break