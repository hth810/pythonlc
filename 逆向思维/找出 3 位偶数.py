from collections import Counter


class Solution:
    def findEvenNumbers(self, digits: List[int]) -> List[int]:
        cnt=Counter(digits)
        res=[]
        for i in range(100,1000,2):
            if Counter(map(int,str(i)))<=cnt:
                res.append(i)
        return res