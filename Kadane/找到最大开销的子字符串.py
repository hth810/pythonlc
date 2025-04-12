from collections import defaultdict


class Solution:
    def maximumCostSubstring(self, s: str, chars: str, vals: List[int]) -> int:
        cnt=defaultdict(int)
        n=len(vals)
        for i in range(n):
            cnt[chars[i]]=vals[i]
        nums=[]
        for i,c in enumerate(s):
            if c in cnt:
                nums.append(cnt[c])
            else:
                nums.append(ord(c)-96)
        ans=temp=nums[0]
        for i in nums[1:]:
            temp=max(i,temp+i)
            ans=max(ans,temp)
        return max(ans,0)
