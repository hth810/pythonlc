def left_bound(nums: List[int], target: int) -> int:
    left = 0
    # 注意
    right = len(nums)

    # 注意
    while left < right:
        mid = left + (right - left) // 2
        if nums[mid] == target:
            right = mid
        elif nums[mid] < target:
            left = mid + 1
        elif nums[mid] > target:
            # 注意
            right = mid

    return left