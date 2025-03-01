class Solution:
    def maxDistance(self, arrays: List[List[int]]) -> int:
        ans=0
        mn,mx=10**5,-10**5
        for a in arrays:
            ans=max(ans,a[-1]-mn,mx-a[0])
            mn=min(mn,a[0])
            mx=max(mx,a[-1])
        return ans