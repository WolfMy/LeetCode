#
# @lc app=leetcode.cn id=6 lang=python3
#
# [6] Z 字形变换
#

# @lc code=start
'''
算法流程：按顺序遍历字符串 s；
    1. res[i] += c：把每个字符 c 填入对应行 s_i；
    2. i += flag：更新当前字符 c 对应的行索引；
    3. flag = - flag：在达到 ZZ 字形转折点时，执行反向。
作者：jyd
链接：https://leetcode-cn.com/problems/zigzag-conversion/solution/zzi-xing-bian-huan-by-jyd/
来源：力扣（LeetCode）
著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。
'''
class Solution:
    def convert(self, s: str, numRows: int) -> str:
        n = len(s)
        if n <= numRows or numRows <= 1:
            return s
        res = ["" for _ in range(numRows)]
        i = 0
        flag = 1
        for c in s:
            res[i] += c
            i += flag
            if i == numRows-1 or i == 0:
                flag = -flag
        return ''.join(res)
        
# @lc code=end

