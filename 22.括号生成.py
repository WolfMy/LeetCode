#
# @lc app=leetcode.cn id=22 lang=python3
#
# [22] 括号生成
#

# @lc code=start
# [1] 递归暴力法 --> 52 ms	13.4 MB
'''100 ms	13.5 MB
class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        # 暴力生成所有 '(' + n-1个左右括号的组合序列
        if n < 1:
            return []
        res = []
        self.recursion('(', n, res)
        return res

    def recursion(self,seq, n, res):
        def isValid(s):
            stack = []
            for w in s:
                if w == ')':
                    w_ = stack.pop() if stack else '#'
                    if w_ != '(':
                        return False
                else:
                    stack.append(w)
            return not stack

        if len(seq) == n*2:
            if isValid(seq):
                res.append(seq)
            return
        self.recursion(seq+'(', n, res)
        self.recursion(seq+')', n, res)
剪枝优化如下'''
class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        # 暴力生成所有 '(' + n-1个左右括号的组合序列
        if n < 1:
            return []
        res = []
        self.recursion('(', n, 1, 0, res)
        return res

    def recursion(self, seq, n, left, right, res):
        def isValid(s):
            # bal必须一直大于0且最终等于0
            bal = 0
            for w in s:
                if w == '(':    bal += 1
                else:   bal -= 1
                if bal < 0: return False
            return bal == 0

        if len(seq) == n*2:
            if isValid(seq):
                res.append(seq)
            return
        # 记录左右括号数，相当于剪枝干
        if left < n:
            self.recursion(seq+'(', n, left+1, right, res)
        if right < n:
            self.recursion(seq+')', n, left, right+1, res)

# [2] 回溯法 --> 36 ms	13.7 MB
class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        ans = []
        def backtrack(S, left, right):
            if len(S) == 2 * n:
                ans.append(S)
                return
            if left < N:
                backtrack(S+'(', left+1, right)
            if right < left:
                backtrack(S+')', left, right+1)

        backtrack('', 0, 0)
        return ans
        
# @lc code=end

