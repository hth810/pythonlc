class Solution:
    def splitArray(self, nums: List[int], k: int) -> int:
        def judge(s):
            slice=1
            sum=0
            i=0
            while i<len(nums):
                sum+=nums[i]
                if sum>s:
                    sum=0
                    slice+=1
                else:
                    i+=1
            if slice<=k:
                return True
            else:
                return False
        left=max(nums)-1
        right=sum(nums)+1
        while left+1<right:
            mid=(left+right)//2
            if judge(mid):
                right=mid
            else:
                left=mid
        return right
