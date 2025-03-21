class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        n=len(graph)
        path=[0]
        ans=[]
        def dfs():
            if path[-1]==n-1:
                ans.append(path.copy())
            for i in graph[path[-1]]:
                path.append(i)
                dfs()
                path.pop()
        dfs()
        return ans