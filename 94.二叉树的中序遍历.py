#
# @lc app=leetcode.cn id=94 lang=python3
#
# [94] 二叉树的中序遍历
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
'''
# [1] 递归算法 --> 40 ms	13.1 MB
class Solution:
    def inorderTraversal(self, root: TreeNode) -> List[int]:
        ans = []
        self.dfs(root, ans)
        return ans

    def dfs(self, child, ans):
        if not child:
            return
        self.dfs(child.left, ans)
        ans.append(child.val)
        self.dfs(child.right, ans)
'''
# [2] 基于栈的遍历 --> 36 ms	13.2 MB
class Solution:
    def inorderTraversal(self, root: TreeNode) -> List[int]:
        # 借助栈来替代递归
        stack = []
        p = root
        res = []
        while(p or stack):
            while(p):
                # 当前结点入栈
                stack.append(p)
                # 尝试入栈当前结点的左子树
                p = p.left
            p = stack.pop()
            res.append(p.val)
            p = p.right
        return res

# [3] 莫里斯遍历 --> 40 ms	13 MB
'''
线索二叉树: https://baike.baidu.com/item/%E7%BA%BF%E7%B4%A2%E4%BA%8C%E5%8F%89%E6%A0%91/10810037?fr=aladdin
莫里斯方法解析: https://stackoverflow.com/questions/5502916/explain-morris-inorder-tree-traversal-without-using-stacks-or-recursion
思路：
Step 1: 将当前节点current初始化为根节点
Step 2: While current不为空，
    若current没有左子节点：
        a. 将current添加到输出
        b. 进入右子树，亦即, current = current.right
    否则：
        a. 在current的左子树中，令current成为最右侧节点的右子节点
        b. 进入左子树，亦即，current = current.left

作者：LeetCode
链接：https://leetcode-cn.com/problems/binary-tree-inorder-traversal/solution/er-cha-shu-de-zhong-xu-bian-li-by-leetcode/
来源：力扣（LeetCode）
著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。
class Solution:
    def inorderTraversal(self, root: TreeNode) -> List[int]:
        # 莫里斯遍历
        current = root
        res = []
        # 线索二叉树
        while(current):
            if not current.left:
                res.append(current.val)
                current = current.right
            else:
                current_left = current.left
                pre = current_left
                while(pre.right):
                    pre = pre.right
                pre.right = current
                # 删除current的左子树
                current.left = None
                current = current_left
        return res
'''
# @lc code=end

