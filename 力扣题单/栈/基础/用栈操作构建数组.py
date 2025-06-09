class Solution:
    def buildArray(self, target: List[int], n: int) -> List[str]:
        res=[]
        m=len(target)
        j=0
        i=1
        while i<=n:
            if j==m:
                break
            if i==target[j]:
                res.append('Push')
                j+=1
            else:
                res.append('Push')
                res.append('Pop')
            i+=1

        return res