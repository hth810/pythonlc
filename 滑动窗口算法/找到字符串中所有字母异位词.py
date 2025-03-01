class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        need, window = {}, {}
        slow, fast,valid = 0, 0,0
        res = []
        for i in p:
            need[i] = need.get(i, 0) + 1
        while fast < len(s):
            c = s[fast]
            fast += 1
            if c in need:
                window[c] = window.get(c, 0) + 1
                if window[c] == need[c]:
                    valid += 1
            while valid == len(need):
                if fast - slow == len(p):
                    res.append(slow)
                d = s[slow]
                slow += 1
                if d in need:
                    if window[d] == need[d]:
                        valid -= 1
                    window[d] -= 1
        return res
