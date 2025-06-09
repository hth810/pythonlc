class Solution:
    def closestMeetingNode(self, edges: List[int], node1: int, node2: int) -> int:
        ans=float('inf')
        path1=set()
        path2=set()
        i,j=node1,node2
        while i not in path1 or j not in path2:
            path1.add(i)
            path2.add(j)
            if i in path2:
                ans=i
            if j in path1:
                ans=min(ans,j)
            if ans<float('inf'):
                return ans
            if edges[i]!=-1:
                i=edges[i]
            if edges[j]!=-1:
                j=edges[j]

        return -1