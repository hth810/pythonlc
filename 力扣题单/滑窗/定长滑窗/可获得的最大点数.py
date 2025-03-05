class Solution:
    def maxScore(self, cardPoints: List[int], k: int) -> int:
        n=len(cardPoints)
        m=n-k
        s=sum(cardPoints)
        if m==0:
            return s
        ans=s
        temp=0
        for i,c in enumerate(cardPoints):
            temp+=c
            if i<m-1:
                continue
            ans=min(ans,temp)
            temp-=cardPoints[i-m+1]
        return s-ans