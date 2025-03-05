class Solution:
    def minimumRecolors(self, blocks: str, k: int) -> int:
        n=len(blocks)
        ans=0
        temp=0
        for i,c in enumerate(blocks):
            if c=='B':
                temp+=1
            if i<k-1:
                continue
            ans=max(ans,temp)
            if blocks[i-k+1]=='B':
                temp-=1
        return k-ans