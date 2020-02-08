#
# @lc app=leetcode.cn id=303 lang=python3
#
# [303] 区域和检索 - 数组不可变
#

# @lc code=start
# [1] 动态规划（区间规划） --> 通过	4124 ms	21.6 MB
class Solution:
    def longestPalindrome(self, s: str) -> str:
        n = len(s)
        # 特判
        if n <= 1:
            return s
        
        # 动态规划 dp[i][j]表示s[i]到s[j]是否是回文
        # 初始化
        dp = [[False for _ in range(n)] for _ in range(n)]
        # dp[i][i]单字符一定是回文
        for i in range(n):
            dp[i][i] = True
        # 记录回文子串起始位置和长度，初始化默认第一个字符
        start = 0
        max_len = 1
        # 若s[i]==s[j]，且 dp[i+1][j-1]==True，那么dp[i][j]=True
        # 否则dp[i][j]=False
        ''' 易错点
            因为 dp[i][j] 取决于 dp[i+1][j-1]，所以应该保证dp[i+1][j-1]比dp[i][j]先取值，且i < j。
            解决方案:[1] j在外层循环，i在内层循环
                    [2] i从大到小取值
        '''
        for i in range(n-2, -1, -1):
            for j in range(i+1, n):
                if s[i] == s[j]:
                    if j - i <=2:
                        # 如果i j相邻或间隔1个字符，那么一定是回文
                        dp[i][j] = True
                    else:
                        dp[i][j] = dp[i+1][j-1]
                if dp[i][j]:
                    # 如果i到j是回文，那么判断是否最长
                    if j-i+1 > max_len:
                        max_len = j - i + 1
                        start = i
        return s[start : start+max_len]

# @lc code=end

