class Solution:
    def __init__(self):
        self.res=[]

    def traverse(self,n,k,track):
        if k==0:
            self.res.append(track.copy())
            return
        for i in range(n,0,-1):
            track.append(i)
            self.traverse(i-1,k-1,track)
            track.pop()

    def combine(self, n: int, k: int) -> List[List[int]]:
        track=[]
        self.traverse(n,k, track)
        return self.res
