class Solution:
    def __init__(self):
        self.res = []

    def backtrack(self, nums: List[int], track: List[int], used: List[bool]):
        if len(track) == len(nums):
            self.res.append(track.copy())
            return
        for i in range(len(nums)):
            if used[i]:
                continue
            track.append(nums[i])
            used[i] = True
            # 进入下一行决策
            self.backtrack(nums, track, used)
            track.pop()
            used[i] = False
    def permute(self, nums: List[int]) -> List[List[int]]:
        track = []
        used = [False for _ in range(len(nums))]
        self.backtrack(nums, track, used)
        return self.res
