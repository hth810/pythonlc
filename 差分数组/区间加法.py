class Solution:
    def getModifiedArray(self, length: int, updates: List[List[int]]) -> List[int]:
        diff=[0]*length
        for start,end,inc in updates:
            diff[start]+=inc
            if end+1<length:
                diff[end+1]-=inc
        res=[0]*length
        res[0]=diff[0]
        for i in range(1,length):
            res[i]=res[i-1]+diff[i]
        return res