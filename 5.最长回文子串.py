#
# @lc app=leetcode.cn id=5 lang=python3
#
# [5] 最长回文子串
#

# @lc code=start
"""
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
                # #################################
                if s[i] == s[j]:
                    if j - i <=2:
                        # 如果i j相邻或间隔1个字符，那么一定是回文
                        dp[i][j] = True
                    else:
                        dp[i][j] = dp[i+1][j-1]
                # 以上可简化为 dp[i][j] = (s[i] == s[j]) and (j - i <= 2 or dp[i+1][j-1])

                if dp[i][j]:
                    # 如果i到j是回文，那么判断是否最长
                    if j-i+1 > max_len:
                        max_len = j - i + 1
                        start = i
        return s[start: start+max_len]
"""
# [2] 中心扩散法 --> 通过	1596 ms	13.1 MB
class Solution:
    def longestPalindrome(self, s: str) -> str:
        n = len(s)
        # 特判
        if n <= 1:
            return s
        # 记录回文子串最大长度，初始化默认第一个字符
        max_len = 1
        max_palindrome = s[0]
        # 中心扩散法
        # 第一个无法扩散
        for i in range(1, n):
            palindrome1, len1 = self.centerSpread(s, i, 1)
            palindrome2, len2 = self.centerSpread(s, i, 2)
            cur_max_palindrome = palindrome1 if len1 > len2 else palindrome2
            if len(cur_max_palindrome) > max_len:
                max_len = len(cur_max_palindrome)
                max_palindrome = cur_max_palindrome
        return max_palindrome
    
    def centerSpread(self, s, i, type):
        # 扩散方式有2种：从当前索引字符扩散、从当前索引左侧间隙扩散
        # 从当前索引字符扩散：得到最长回文子串长度是奇数
        # 从当前索引左侧间隙扩散：得到最长回文子串长度是偶数
        left = i - 1
        if type == 1:
            # 从当前索引字符扩散
            right = i + 1
        elif type == 2:
            # 从当前索引左侧间隙扩散
            right = i
        while(left >= 0 and right <= len(s)-1 and s[left] == s[right]):
            # 若扩散的左右指针对应的字符相等,则继续同时向外扩散，直到到达s边界
            left -= 1
            right += 1
        left += 1
        right -= 1
        cur_max_len = right - left + 1
        palindrome = s[left: right+1]
        return palindrome, cur_max_len

# @lc code=end

