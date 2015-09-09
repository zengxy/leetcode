# Definition for a  binary tree node
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # @param root, a tree node
    # @return a boolean
    def isBalanced(self, root):
        isBalance=[True]
        self.isB(root,isBalance)
        return isBalance[0]

    def isB(self,node,isBalance):
        if isBalance[0]==False:
            return 0
        else:
            if node==None:
                return 0
            else:
                l=self.isB(node.left,isBalance)
                r=self.isB(node.right,isBalance)
                if abs(l-r)>1:
                    isBalance[0]=False
                if l>r:
                    r=l
                return r+1



    def getDepth(self,node):
        if node==None:
            return 0
        else:
            l=self.getDepth(node.left)
            r=self.getDepth(node.right)
            if l>r:
                r=l
            return r+1


def swap(a):
    a[0]+=1

a=[3]
swap(a)
print(a)