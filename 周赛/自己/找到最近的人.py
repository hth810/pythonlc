class Solution:
    def findClosest(self, x: int, y: int, z: int) -> int:
        a=abs(z-x)
        b=abs(z-y)
        if a>b:
            return 2
        elif a==b:
            return 0
        else:
            return 1