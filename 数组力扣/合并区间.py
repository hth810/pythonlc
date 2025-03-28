class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key=lambda x:x[0])
        l=intervals[0][0]
        pre=intervals[0][1]
        ans=[]
        for a,b in intervals:
            if a>pre:
                ans.append([l,pre])
                l=a
            if b>pre:
                pre=b
        ans.append([l,pre])
        return ans
