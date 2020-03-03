#
# @lc app=leetcode.cn id=20 lang=python3
#
# [20] 有效的括号
#

# @lc code=start
# [1] 栈 --> 32 ms	13.5 MB
class Solution:
    def isValid(self, s: str) -> bool:
        if not s:
            return True
        stack = []
        hasmap = {')':'(', ']':'[', '}':'{'}
        for w in s:
            if w in hasmap:
                w_ = stack.pop() if stack else '#'
                if w_ != hasmap[w]:
                    return False
            else:
                stack.append(w)
        return not stack
# @lc code=end

