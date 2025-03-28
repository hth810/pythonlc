class Solution:
    def minimumSum(self, n: int, k: int) -> int:
        s=set()
        i=1
        ans=0
        while n!=0:
            if k-i in s:
                i+=1
                continue
            s.add(i)
            ans+=i
            n-=1
            i+=1
        return ans

s=Solution()
print(s.minimumSum(5,4))