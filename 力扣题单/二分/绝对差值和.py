from bisect import bisect_left

MOD=10**9+7
class Solution:
    def minAbsoluteSumDiff(self, nums1: List[int], nums2: List[int]) -> int:
        ans=float('inf')
        n=len(nums1)
        cnt=sum(abs(nums1[i]-nums2[i]) for i in range(n))
        if not cnt:
            return 0
        s=sorted(nums1)
        for i,c in enumerate(nums2):
            a=bisect_left(s,c)
            if a:
                ans=min(ans,cnt-abs(nums1[i]-nums2[i])+abs(nums2[i]-s[a-1]))
            if a<n:
                ans=min(ans,cnt-abs(nums1[i]-nums2[i])+abs(nums2[i]-s[a]))

        return ans%MOD