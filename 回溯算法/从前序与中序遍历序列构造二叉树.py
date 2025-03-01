class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def __init__(self):
        self.valToIndex={}
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        for i in range(len(inorder)):
            self.valToIndex[inorder[i]]=i
        return self.build(preorder,0,len(preorder)-1,inorder,0,len(inorder)-1)
    def build(self,preorder,preStart,preEnd,inorder,inStart,inEnd):
        if preStart>preEnd:
            return None
        rootVal=preorder[preStart]
        index=self.valToIndex[rootVal]

        left_size=index-inStart
        root=TreeNode(rootVal)

        root.left=self.build(preorder,preStart+1,preStart+left_size,inorder,inStart,index-1)
        root.right=self.build(preorder,preStart+left_size+1,preEnd,inorder,index+1,inEnd)

        return root
