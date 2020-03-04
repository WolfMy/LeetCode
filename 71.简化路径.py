#
# @lc app=leetcode.cn id=71 lang=python3
#
# [71] 简化路径
#

# @lc code=start
# [1] 分割路径+栈 --> 48 ms	13.4 MB
class Solution:
    def simplifyPath(self, path: str) -> str:
        if not path:
            return ''
        # 分割路径
        split_path = path.split('/')
        # 路径入栈
        stack = []
        for p in split_path:
            # 若遇到'..'，那么将上一级目录弹出栈
            if p == '..':
                if stack:   stack.pop()
            # 若遇到'.'，那么跳过
            elif p == '.':  continue
            elif p == '':   continue
            else:   stack.append(p)
        # 根据栈中内容，生成路径
        return '/' + '/'.join(stack)
# @lc code=end

