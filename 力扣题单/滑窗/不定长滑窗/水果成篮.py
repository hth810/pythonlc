class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        window={}
        l=0
        ans=0
        for r,c in enumerate(fruits):
            window[c]=window.get(c,0)+1
            while len(window)>2 and l<r:
                window[fruits[l]]-=1
                if window[fruits[l]]==0:
                    del window[fruits[l]]
                l+=1
            ans=max(ans,r-l+1)
        return ans