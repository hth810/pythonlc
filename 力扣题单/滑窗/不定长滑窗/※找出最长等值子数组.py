# from collections import Counter
#
#
# class Solution:
#     def longestEqualSubarray(self, nums: List[int], k: int) -> int:
#         cnt=Counter(nums)
#         ans=0
#         for a in cnt.keys():
#             temp=0
#             other=0
#             l=0
#             for i,c in enumerate(nums):
#                 if c!=a:
#                     other+=1
#                 else:
#                     temp+=1
#                 while other>k:
#                     if nums[l]!=a:
#                         other-=1
#                     else:
#                         temp-=1
#                     l+=1
#                 ans=max(ans,temp)
#
#         return ans
from collections import defaultdict


class Solution:
    def longestEqualSubarray(self, nums: List[int], k: int) -> int:
        cnt=defaultdict(list)
        for i,c in enumerate(nums):
            cnt[c].append(i-len(cnt[c]))

        ans=0
        for pos in cnt.values():
            if len(pos)<=ans:
                continue
            l=0
            for r,x in enumerate(pos):
                while x-pos[l]>k:
                    l+=1
                ans=max(ans,r-l+1)

        return ans