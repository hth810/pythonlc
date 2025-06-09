from collections import Counter


class Solution:
    def smallestPalindrome(self, s: str) -> str:
        s=list(map(str,s))
        s.sort()
        cnt=Counter(s)
        ans=''
        temp=''
        for i,c in cnt.items():
            if c%2:
                temp=i
            for _ in range(c//2):
                ans+=i
        ans+=temp+ans[::-1]
        return ans