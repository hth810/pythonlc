class Solution:
    def resultArray(self, nums: List[int], k: int) -> List[int]:
        res=[0]*k
        pre=[0]*k
        for num in nums:
            mod=num%k
            cur=[0]*k
            cur[mod]+=1
            for m in range(k):
                if pre[m]:
                    n_mod=(m*num)%k
                    cur[n_mod]+=pre[m]
            for m in range(k):
                res[m]+=cur[m]
            pre=cur.copy()
        return res