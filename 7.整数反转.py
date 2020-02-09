#
# @lc app=leetcode.cn id=7 lang=python3
#
# [7] 整数反转
#

# @lc code=start
# [1] 字符串+列表 --> 通过	28 ms	12.9 MB
class Solution:
    def reverse(self, x: int) -> int:
        # 先将int转str，再将str转list
        x_list = list(str(x))
        # 删除负号
        if x < 0:
            x_list.remove('-')
        # 利用列表的reverse方法反转x
        x_list.reverse()
        # 再将list转为str，str转int
        x_reverse = int(''.join(x_list))
        if x < 0:
            x_reverse = -1 * x_reverse
        if x_reverse < -2**31 or x_reverse > 2**31 - 1:
            return 0
        return x_reverse
'''
# [2] 弹出和推入数字 & 溢出前进行检查 --> 通过	36 ms	13.2 MB
class Solution:
    def reverse(self, x: int) -> int:
        # 循环
        # pop = x % 10  x /= 10
        # ans = ans * 10 + pop
        flag = 1 if x > 0 else 0    # flag 0:x<0 1:x>0
        x = abs(x)
        ans = 0
        while(x != 0):
            pop = x % 10
            ans = ans * 10 + pop
            if ans > 2147483647 or ans < -2147483648:
                return 0
            x //= 10
        return ans if flag else -ans
'''
# @lc code=end

