#
# @lc app=leetcode.cn id=3 lang=python3
#
# [3] 无重复字符的最长子串
#

# @lc code=start
"""
# [1] 动态规划 --> 136 ms	13.2 MB  +哈希表 --> 76 ms	13.4 MB
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        n = len(s)
        if n <= 1: 
            return n
        # 动态规划 dp[i]表示前i个字符中（包括i）最长子串的长度
        # dp[i] = dp[i-1]+1 if s[i] not in substring else dp[i-1]-substring.index(s[i])
        dp = [1]
        max_len = 1
        '''
        for i in range(1,n):
            if s[i] == s[i-1]:
                dp.append(1)
                continue
            substring = s[i - dp[i-1]: i]
            if s[i] not in substring:
                dp.append(dp[i-1] + 1)
            else:
                dp.append(dp[i-1] - substring.index(s[i]))
            max_len = max(max_len, dp[i])
        '''
        # 利用哈希表代替子串
        hasmap = {s[0]: 0}
        for i in range(1,n):
            if s[i] == s[i-1]:
                dp.append(1)
            else:
                if s[i] not in hasmap:
                    dp.append(dp[i-1] + 1)
                else:
                    dp.append(min(dp[i-1]+1,i - hasmap[s[i]]))
            hasmap[s[i]] = i
            max_len = max(max_len, dp[i])
        return max_len
"""
# [2] 哈希表 --> 68 ms	13.2 MB
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        n = len(s)
        if n <= 1: 
            return n
        # 利用哈希表记录字符索引
        hasmap = {}
        max_len = 0
        cur_len = 0
        for i in range(n):
            if s[i] not in hasmap:
                cur_len += 1
            else:
                cur_len = min(cur_len+1, i - hasmap[s[i]])
            hasmap[s[i]] = i
            max_len = max(max_len, cur_len)
        return max_len
'''
# [3] 滑动窗口 --> 96 ms	13.2 MB
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        n = len(s)
        if n <= 1: 
            return n
        # 滑动窗口：窗口内的无重复字符
        # 双指针，指向滑窗左右边界
        i = 0
        j = 1
        max_len = 1
        while(i <= j and j < n):
            if s[j] in s[i:j]:
                # 如果j是重复字符，那么移动i到重复字符处
                i += s[i:j].index(s[j]) + 1
            else:
                j += 1
            max_len = max(max_len, len(s[i:j]))
        return max_len
# [4] 滑动窗口+哈希表 --> 92 ms	13.2 MB
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        n = len(s)
        if n <= 1: 
            return n
        # 滑动窗口：窗口内的无重复字符
        # 哈希表记录字符索引
        hasmap = {}
        # 双指针，指向滑窗左右边界
        i = 0
        j = 0
        max_len = 0
        for j in range(n):
            if s[j] in hasmap:
                i = max(i, hasmap[s[j]]+1)
            hasmap[s[j]] = j
            max_len = max(max_len, j-i+1)
        return max_len
'''

# @lc code=end

