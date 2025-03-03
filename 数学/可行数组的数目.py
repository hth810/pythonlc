class Solution:
    def countArrays(self, original: List[int], bounds: List[List[int]]) -> int:
        n = len(original)
        base = original[0]
        # Initialize L and R. Here we assume values are at most 10^9,
        # so starting with a wide enough range is safe.
        L, R = -10**18, 10**18
        for i in range(n):
            diff = original[i] - base
            low_i = bounds[i][0] - diff
            high_i = bounds[i][1] - diff
            L = max(L, low_i)
            R = min(R, high_i)
        # The count of valid x is R - L + 1 if L <= R, else 0.
        return max(0, R - L + 1)