from bisect import bisect_left


class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        n = len(arr)
        right = bisect_left(arr, x)
        left = right - 1
        for _ in range(k):
            if left < 0:
                right += 1
            elif right > n - 1 or x - arr[left] <= arr[right] - x:
                left -= 1
            else:
                right += 1

        return arr[left + 1:right]
