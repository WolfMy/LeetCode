#
# @lc app=leetcode.cn id=96 lang=python3
#
# [96] 不同的二叉搜索树
#

# @lc code=start
'''
# [1] 递归算法+记忆化 --> 40 ms	12.9 MB
class Solution:
    def numTrees(self, n: int) -> int:
        # 递归算法
        # 迭代1..n
        # 以i为root的二叉搜索树数量 等于 以 1..(i-1)为root的二叉搜索树数量 与 以(i+1)..n为root的二叉搜索树数量 的笛卡尔积
        # 使用哈希表实现记忆化
        self.hasmap = {}
        ans = self.recursion(1, n)
        return ans

    def recursion(self, start, end):
        if start > end:
            return 1
        ans = 0
        for i in range(start, end+1):
            if (start, i-1) in self.hasmap:
                left = self.hasmap[(start, i-1)]
            else:
                self.hasmap[(start, i-1)] = self.recursion(start, i-1)
                left = self.hasmap[(start, i-1)]
                
            if (i+1, end) in self.hasmap:
                right = self.hasmap[(i+1, end)]
            else:
                self.hasmap[(i+1, end)] = self.recursion(i+1, end)
                right = self.hasmap[(i+1, end)]
            ans += left * right
        return ans
'''

# 作者：LeetCode
# 链接：https://leetcode-cn.com/problems/unique-binary-search-trees/solution/bu-tong-de-er-cha-sou-suo-shu-by-leetcode/
# [2] 动态规划 --> 28 ms	13.2 MB
class Solution:
    def numTrees(self, n: int) -> int:
        # 动态规划: G(n) = G(i-1) * G(n-i) for i in range(1, n+1)
        G = [0] * (n+1)
        G[0], G[1] = 1, 1
        for i in range(2, n+1):
            for j in range(1, i+1):
                G[i] += G[j-1] * G[i-j]
        return G[n]
            
        
# @lc code=end

