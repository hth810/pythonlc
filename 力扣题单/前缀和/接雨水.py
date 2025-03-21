class Solution:
    def trap(self, height: List[int]) -> int:
        l=0
        r=len(height)-1
        ans=0
        pre=sur=0
        while l<=r:
            pre=max(pre,height[l])
            sur=max(sur,height[r])
            if pre<sur:
                ans+=(pre-height[l])
                l+=1
            else:
                ans+=(sur-height[r])
                r-=1

        return ans