class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        vis=set()
        n=len(rooms)
        def dfs(i):
            vis.add(i)
            for j in rooms[i]:
                if j not in vis:
                    dfs(j)

        dfs(0)
        return len(vis)==n
