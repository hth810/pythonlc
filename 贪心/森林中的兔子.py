import math
from collections import Counter


class Solution:
    def numRabbits(self, answers: List[int]) -> int:
        cnt=Counter(answers)
        ans=0
        for i,c in cnt.items():
            ans+=math.ceil(c/(i+1))*(i+1)
        return ans
