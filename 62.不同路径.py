#
# @lc app=leetcode.cn id=62 lang=python3
#
# [62] 不同路径
#

# @lc code=start
# [1] 动态规划 --> 40 ms	13.1 MB
class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        if m <= 0 or n <= 0:
            return 0
        elif m == 1 or n == 1:
            return 1
        # 动态规划: dp[m][n] = dp[m-1][n] + dp[m][n-1]
        dp = [[1 for _ in range(n)] for _ in range(m)]
        for i in range(1, m):
            for j in range(1, n):
                dp[i][j] = dp[i-1][j] + dp[i][j-1]
        return dp[m-1][n-1]
        
# @lc code=end

