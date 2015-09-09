# Definition for a  binary tree node
class TreeNode:
     def __init__(self, x):
         self.val = x
         self.left = None
         self.right = None
pathList=[]
class Solution:
    # @param root, a tree node
    # @param sum, an integer
    # @return a list of lists of integers
    def pathSum(self, root, sum):
        #   avoid null tree
        if root is None:
            return []

        def inter(root,sum):
            output = list()
            if root is None:
                return []
            # leaf
            if root.left is None and root.right is None:
                if root.val==sum:
                    return [[root.val]]
                else:
                    return []
            if root.left is not None:
                ret = inter(root.left, sum-root.val)
                for i in range(len(ret)):
                    ret[i].insert(0,root.val)
                    # ret[i].append(root.val)
                    output.append(ret[i])
            if root.right is not None:
                ret = inter(root.right, sum-root.val)
                for i in range(len(ret)):
                    ret[i].insert(0,root.val)
                    # ret[i].append(root.val)
                    output.append(ret[i])

            return output

        return inter(root,sum)

a=TreeNode(1)
b=Solution()
print(b.pathSum(a,1))