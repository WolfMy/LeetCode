#
# @lc app=leetcode.cn id=150 lang=python3
#
# [150] 逆波兰表达式求值
#

# @lc code=start
# 边迭代边入栈 --> 32 ms	13.7 MB
class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for s in tokens:
            if s in '+-*/':
                n2 = int(stack.pop())
                n1 = int(stack.pop())
                if s == '+':    stack.append(n1+n2)
                elif s == '-':  stack.append(n1-n2)
                elif s == '*':  stack.append(n1*n2)
                elif s == '/':  stack.append(int(n1/n2))
            else:
                stack.append(s)
        return int(stack[0])
# @lc code=end

