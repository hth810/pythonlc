class Solution:
    def minimumSize(self, nums: List[int], maxOperations: int) -> int:
        def check(mid):
            cnt=0
            for i in nums:
                cnt+=i//mid
                if i%mid==0:
                    cnt-=1
            return cnt<=maxOperations
        nums.sort()
        left=0
        right=nums[-1]+1
        while left+1<right:
            mid=left+(right-left)//2
            if check(mid):
                right=mid
            else:
                left=mid
        return right