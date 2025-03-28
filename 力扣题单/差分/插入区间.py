class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        start,end=newInterval[0],newInterval[1]
        ans=[]
        flag=False
        for s,e in intervals:
            if end<s:
                if not flag:
                    ans.append([start,end])
                    flag=True
                ans.append([s,e])
            elif e<start:
                ans.append([s,e])
            else:
                start=min(start,s)
                end=max(end,e)
        if not flag:
            ans.append([start,end])

        return ans
