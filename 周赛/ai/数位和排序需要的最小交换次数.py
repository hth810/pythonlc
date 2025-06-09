class Solution:
    def minSwaps(self, nums: List[int]) -> int:
        def count(x):
            s=0
            while x:
                s+=x%10
                x//=10
            return s
        s=[]
        n=len(nums)
        for i,c in enumerate(nums):
            s.append((count(c),c,i))
        s.sort(key=lambda x:(x[0],x[1]))
        pos=[0]*n
        for k in range(n):
            i=s[k][2]
            pos[i]=k
        vis=[False]*n
        res=0
        for j in range(n):
            if not vis[j]:
                cur=j
                cnt=0
                while not vis[cur]:
                    vis[cur]=True
                    cur=pos[cur]
                    cnt+=1
                res+=(cnt-1)
        return res
