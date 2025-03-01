def bubbleSort(nums: List[int]) -> List[int]:
    n = len(nums)
    for a in range(len(nums)):
        for i in range(n-1, a, -1):
            if nums[i] < nums[i-1]:
                nums[i], nums[i-1] = nums[i-1], nums[i]