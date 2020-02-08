#
# @lc app=leetcode.cn id=70 lang=python3
#
# [70] 爬楼梯
#

# @lc code=start
'''
# [1] 动态规划（自顶向下，记忆化） --> 通过	36 ms	13 MB
class Solution:
    def climbStairs(self, n: int) -> int:
        # 自顶向下 dp[i] = dp[i-1] + dp[i-2]
        # 使用哈希表实现记忆化
        self.cache = {}
        return self.climb(n)

    def climb(self, n):
        if n <=3 :
            return n
        if n in self.cache:
            # 如果cache中缓存了climb(n)，那么直接返回
            return self.cache[n]
        else:
            # 如果cache中没有缓存n，那么递归计算climb(n)后，添加到缓存中，再返回
            self.cache[n] = self.climb(n-1) + self.climb(n-2)
            return self.cache[n]
'''
# [2] 动态规划（自底向上） --> 通过	24 ms	12.9 MB
class Solution:
    def climbStairs(self, n: int) -> int:
        # 特判
        if n <= 3:
            return n
        # 自底向上的动态规划 dp[i] = dp[i-1] + dp[i-2]
        dp = [x+1 for x in range(3)]
        for i in range(3,n):
            dp.append(dp[i-1] + dp[i-2])
        # n阶的方法数等于dp[n-1]
        return dp[n-1]
        
# @lc code=end

