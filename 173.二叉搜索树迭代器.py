#
# @lc app=leetcode.cn id=173 lang=python3
#
# [173] 二叉搜索树迭代器
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
# [1] 扁平化二叉搜索树 --> 172 ms	19.5 MB
class BSTIterator:
    def __init__(self, root: TreeNode):
        self.data = []
        stack = []
        while stack or root:
            while root:
                stack.append(root)
                root = root.left
            root = stack.pop()
            self.data.append(root.val)
            root = root.right

    def next(self) -> int:
        """
        @return the next smallest number
        """
        return self.data.pop(0)

    def hasNext(self) -> bool:
        """
        @return whether we have a next smallest number
        """
        return len(self.data)!=0

# [2] 受控递归 --> 92 ms	20.6 MB
class BSTIterator:
    def __init__(self, root: TreeNode):
        self.stack = []
        self.node = root

    def next(self) -> int:
        """
        @return the next smallest number
        """
        while self.node:
            self.stack.append(self.node)
            self.node = self.node.left
        nextNode = self.stack.pop()
        self.node = nextNode.right
        return nextNode.val
        
    def hasNext(self) -> bool:
        """
        @return whether we have a next smallest number
        """
        return self.node!=None or len(self.stack)!=0

# Your BSTIterator object will be instantiated and called as such:
# obj = BSTIterator(root)
# param_1 = obj.next()
# param_2 = obj.hasNext()
# @lc code=end

