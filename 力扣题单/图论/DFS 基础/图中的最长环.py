from collections import defaultdict


class Solution:
    def longestCycle(self, edges: List[int]) -> int:
        n=len(edges)
        visited=[False]*n
        ans=0
        for i,c in enumerate(edges):
            if not visited[c]:
                cur=c
                cur_path=defaultdict(int)
                p=0
                while cur!=-1:
                    if visited[cur]:
                        if cur in cur_path:
                            ans=max(ans,p-cur_path[cur])
                        break
                    else:
                        visited[cur]=True
                        cur_path[cur]=p
                        p+=1
                        cur=edges[cur]
        return ans if ans!=0 else -1
