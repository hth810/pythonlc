from bisect import bisect_left


class Solution:
    def answerQueries(self, nums: List[int], queries: List[int]) -> List[int]:
        nums.sort()
        s=[0]*len(nums)
        s[0]=nums[0]
        for i in range(1,len(nums)):
            s[i]=nums[i]+s[i-1]
        ans=[]
        for i in queries:
            a=bisect_left(s,i)
            if a==len(s):
                ans.append(a)
            elif i==s[a]:
                ans.append(a + 1)
            else:
                if a==0:
                    ans.append(0)
                    continue
                ans.append(a)
        return ans