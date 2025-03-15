class Solution:
    def maximumPopulation(self, logs: List[List[int]]) -> int:
        diff=[0]*102
        f=[0]*102
        for b,d in logs:
            diff[b-1950]+=1
            diff[d-1950]-=1
        f[0]=diff[0]
        for i in range(1,102):
            f[i]=diff[i]+f[i-1]
        a=f.index(max(f))
        return a+1950