class Solution:
    def minFlips(self, s: str) -> int:

        l = len(s)
        s = s * 2
        tgt = '01' * l

        match = [0] * len(s)
        for j in range(len(s)):
            if s[j] == tgt[j]:
                match[j] = 1

        for j in range(1, len(s)):
            match[j] += match[j - 1]

        ans = l
        for j in range(l, len(s)):
            ans = min(ans, l - match[j] + match[j - l], match[j] - match[j - l])
        return ans