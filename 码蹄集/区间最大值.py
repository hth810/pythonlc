
def main():
    n,k=map(int,input().split())
    a=list(map(int,input().split()))
    cnt={}
    s=set()
    for i in range(0,k):
        cnt[a[i]]=cnt.get(a[i],0)+1
    for i in range(0,k):
        if cnt[a[i]]==1:
            s.add(a[i])
    if not s:
        print('-1',end=' ')
    else:
        print(max(s),end=' ')
    for i in range(k,n):
        if cnt[a[i-k]]==1:
            s.remove(a[i-k])
        if cnt[a[i-k]]==2:
            s.add(a[i-k])
        cnt[a[i-k]]-=1

        cnt[a[i]]=cnt.get(a[i],0)+1

        if cnt[a[i]]==1:
            s.add(a[i])
        if cnt[a[i]]==2:
            s.remove(a[i])
        if not s:
            print('-1',end=' ')
        else:
            print(max(s),end=' ')





if __name__ == '__main__':
    main()