def tiMe(nums,k):
    def check(mid):
        cnt=1
        sum=0
        i=0
        while i<len(nums):
            sum+=nums[i]
            if sum>mid:
                sum=0
                cnt+=1
            else:
                i+=1
        if cnt<=k:
            return True
        else:
            return False
    left=max(nums)-1
    right=sum(nums)+1
    while left+1<right:
        mid=(left+right)//2
        if check(mid):
            right=mid
        else:
            left=mid
    return right



t,k=map(int,input().split())
nums=list(map(int,input().split()))
time=tiMe(nums,k)
hi=[[0]*2 for i in range(k)]
cur=k-1
h=0
for i in range(t,0,-1):
    if hi[cur][1]==0:
        hi[cur][1]=i
    if h+nums[i-1]>time:
        hi[cur][0]=i+1
        cur-=1
        h=nums[i-1]
        hi[cur][1]=i
    else:
        h+=nums[i-1]
hi[cur][0]=1

for i in range(k):
    if hi[i][0]==0:
        print(0,0)
    else:
        print(hi[i][0],hi[i][1])


