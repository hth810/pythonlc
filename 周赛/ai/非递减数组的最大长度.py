class Solution:
    def maximumPossibleSize(self, nums: List[int]) -> int:
        stack=[]
        for i in reversed(nums):
            cur=i
            while stack and cur>stack[-1]:
                p=stack.pop()
                cur=max(cur,p)
            stack.append(cur)
        return len(stack)