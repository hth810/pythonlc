MOD=10**9+7
class Solution:
    def assignEdgeWeights(self, edges: List[List[int]]) -> int:
        n=max(e for _,e in edges)
        tree=[[] for _ in range(n+1)]
        for i,j in edges:
            tree[i].append(j)
            tree[j].append(i)
        q=[]
        q.append(1)
        vis=[0]*(n+1)
        vis[1]=1
        dep=-1
        while q:
            tmp=q
            q=[]
            dep+=1
            for i in tmp:
                for j in tree[i]:
                    if vis[j]!=1:
                        q.append(j)
                        vis[j]=1
        if dep==0:
            return 0
        else:
            return pow(2,dep-1,MOD)


