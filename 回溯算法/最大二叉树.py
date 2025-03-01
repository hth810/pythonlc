class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def constructMaximumBinaryTree(self, nums: List[int]) -> Optional[TreeNode]:
        return self.build(nums,0,len(nums)-1)

    def build(self,nums,lo,hi):
        if lo>hi:
            return None
        index=-1
        maxVal=float("-inf")
        for i in range(lo,hi+1):
            if maxVal<nums[i]:
                index=i
                maxVal=nums[i]
        root=TreeNode(maxVal)
        root.left=self.build(nums,lo,index-1)
        root.right=self.build(nums,index+1,hi)

        return  root

