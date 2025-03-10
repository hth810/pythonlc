class Solution:
    def maxConsecutiveAnswers(self, answerKey: str, k: int) -> int:
        n=len(answerKey)
        l=0
        ans=0
        cnt_t=0
        cnt_f=0
        for r,c in enumerate(answerKey):
            if c=='T':
                cnt_t+=1
            while cnt_t>k:
                if answerKey[l]=='T':
                    cnt_t-=1
                l+=1
            ans=max(ans,r-l+1)
        l=0
        for r, c in enumerate(answerKey):
            if c == 'F':
                cnt_f += 1
            while cnt_f > k:
                if answerKey[l] == 'F':
                    cnt_f -= 1
                l += 1
            ans = max(ans, r - l + 1)
        return ans