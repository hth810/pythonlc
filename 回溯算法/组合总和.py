class Solution:
    def __init__(self):
        self.res = []

    def traverse(self, candidates: List[int], target: int, track: List[int]) -> None:
        if target == 0:
            self.res.append(track.copy())
            return
        if target < 0:
            return
        for i in range(len(candidates)):
            if candidates[i] > target:
                continue
            track.append(candidates[i])
            self.traverse(candidates[i:], target - candidates[i], track)
            track.pop()
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        track = []
        self.traverse(candidates, target, track)
        return self.res


