class Solution:
    def numberOfAlternatingGroups(self, colors: List[int], k: int) -> int:
        start=0
        n = len(colors)
        ans=0
        for i in range(1,n+k-1):
            if colors[i%n] ==colors[(i-1)%n]:
                start=i
            if i-start+1<k:
                continue
            if i-start+1>=k:
                ans+=1
        return ans
