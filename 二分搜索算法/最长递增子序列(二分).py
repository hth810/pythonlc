class Solution:
    def lengthOfLIS(self, nums):
        top = [0] * len(nums)
        piles = 0
        for i in range(len(nums)):
            poker = nums[i]

            left, right = 0, piles
            while left < right:
                mid = (left + right) // 2
                if top[mid] > poker:
                    right = mid
                elif top[mid] < poker:
                    left = mid + 1
                else:
                    right = mid

            if left == piles:
                piles += 1
            top[left] = poker
        return piles