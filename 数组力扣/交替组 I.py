class Solution:
    def numberOfAlternatingGroups(self, colors: List[int]) -> int:
        n=len(colors)
        ans=0
        for i in range(n):
            left=(i-1+n)%n
            right=(i+1+n)%n
            if colors[i]!=colors[left] and colors[i]!=colors[right]:
                ans+=1

        return ans