# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
# 非递归先序遍历二叉树

class Solution(object):
    def preorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        returnList=[]
        tempStack=[]
        tempStack.append(root)

        while tempStack.__len__()!=0:
            node = tempStack.pop()
            if node==None:
                continue
            returnList.append(node.val)
            tempStack.append(node.right)
            tempStack.append(node.left)

        return returnList

