class Solution:
    def maximizeWin(self, prizePositions: List[int], k: int) -> int:
        n=len(prizePositions)
        if k*2+1>=prizePositions[-1]-prizePositions[0]:
            return n
        ans=l=0
        temp=[0]*(n+1)
        for r,c in enumerate(prizePositions):
            while c-prizePositions[l]>k:
                l+=1
            ans=max(ans,temp[l]+r-l+1)
            temp[r+1]=max(temp[r],r-l+1)

        return ans
