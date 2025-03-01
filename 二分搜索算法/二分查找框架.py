# def binarySearch(nums: List[int], target: int) -> int:
#     left, right = 0, len(nums) - 1
#
#     while ...:
#         mid = left + (right - left) // 2
#         if nums[mid] == target:
#             ...
#         elif nums[mid] < target:
#             left = ...
#         elif nums[mid] > target:
#             right = ...
#     return ...

#不要出现 else，而是把所有情况用 else if 写清楚，这样可以清楚地展现所有细节
#另外提前说明一下，计算 mid 时需要防止溢出
#>x=>=x+1
#<x=(>=x)-1
#<=x=>x-1
def binarySearch(nums:List[int], target:int) -> int:
    left = 0
    # 注意
    right = len(nums) - 1

    while left <= right:
        mid = left + (right - left) // 2
        if nums[mid] == target:
            return mid
        elif nums[mid] < target:
            # 注意
            left = mid + 1
        elif nums[mid] > target:
            # 注意
            right = mid - 1


def binarySearch1(nums:List[int], target:int) -> int:
    left = 0
    # 注意
    right = len(nums)

    while left <= right:
        mid = left + (right - left) // 2
        if nums[mid] == target:
            return mid
        elif nums[mid] < target:
            # 注意
            left = mid + 1
        elif nums[mid] > target:
            # 注意
            right = mid
