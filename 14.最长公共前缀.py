#
# @lc app=leetcode.cn id=14 lang=python3
#
# [14] 最长公共前缀
#

# @lc code=start
# [1] 暴力法 --> 56 ms	13.1 MB
class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        n = len(strs)
        if n == 0:
            return ""
        elif n == 1:
            return strs[0]
            
        i = 0
        min_len = float("inf")
        for s in strs:
            min_len = min(min_len, len(s))
        while(i < min_len):
            for j in range(n-1):
                if strs[j][i] != strs[j+1][i]:
                    return strs[0][:i]
                if j == n - 2:
                    i += 1
        return strs[0][:i]
            
        
# @lc code=end

