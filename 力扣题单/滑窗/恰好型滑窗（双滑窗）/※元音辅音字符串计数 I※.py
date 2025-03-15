class Solution:
    def f(self,word,k):
        cnt_yuan = {}
        fu = 0
        ans = 0
        l = 0
        for i, c in enumerate(word):
            if c in 'aeiou':
                cnt_yuan[c] = cnt_yuan.get(c, 0) + 1
            else:
                fu += 1
            while fu >= k and len(cnt_yuan)==5:
                if word[l] in 'aeiou':
                    cnt_yuan[word[l]] -= 1
                    if cnt_yuan[word[l]] == 0:
                        del cnt_yuan[word[l]]
                else:
                    fu -= 1
                l += 1
            ans+=l

        return ans

    def countOfSubstrings(self, word: str, k: int) -> int:
        return self.f(word,k)-self.f(word,k+1)

