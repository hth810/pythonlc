class Solution:
    def trap(self, height: List[int]) -> int:
        ans=0
        l=0
        r=len(height)-1
        pre=0
        suf=0
        while l<=r:
            pre=max(pre,height[l])
            suf=max(suf,height[r])
            if pre<suf:
                ans+=pre-height[l]
                l+=1
            else:
                ans+=suf-height[r]
                r-=1
        return ans