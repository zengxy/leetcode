class Solution:
    # @param root, a tree node
    # @return an integer
    def maxDepth(self, root):
        if root==None:
            return 0
        elif root.left==None and root.right==None:
            return 1
        else:
            l=self.maxDepth(root.left)
            r=self.maxDepth(root.right)
            if l>r:
                return l+1
            else:
                return r+1