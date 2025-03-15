class Solution:
    def f(self,word,k):
        n=len(word)
        cnt={}
        fu=0
        l=ans=0
        for i,c in enumerate(word):
            if c in 'aeiou':
                cnt[c]=cnt.get(c,0)+1
            else:
                fu+=1
            while len(cnt)==5 and fu>=k:
                a=word[l]
                if a in 'aeiou':
                    cnt[a]-=1
                    if cnt[a]==0:
                        del cnt[a]
                else:
                    fu-=1
                l+=1
            ans+=l

        return ans

    def countOfSubstrings(self, word: str, k: int) -> int:
        return self.f(word,k)-self.f(word,k+1)