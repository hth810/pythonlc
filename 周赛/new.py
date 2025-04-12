class Solution:
    def minOperations(self, queries: List[List[int]]) -> int:
        res = 0
        for l, r in queries:
            total = 0
            k = 1
            while True:
                low = pow(4,k-1)
                high = pow(4,k)-1
                if low > r:
                    break
                a = max(l, low)
                b = min(r, high)
                if a > b:
                    k += 1
                    continue
                cnt = b - a + 1
                total += cnt * k
                k += 1
            res += (total + 1) // 2
        return res
