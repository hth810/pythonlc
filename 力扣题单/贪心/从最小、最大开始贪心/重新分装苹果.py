class Solution:
    def minimumBoxes(self, apple: List[int], capacity: List[int]) -> int:
        s=sum(apple)
        capacity.sort(reverse=True)
        a=0
        for i,c in enumerate(capacity):
            a+=c
            if a>=s:
                return i+1