#
# @lc app=leetcode.cn id=9 lang=python3
#
# [9] 回文数
#

# @lc code=start
'''
# [1] 整数反转 --> 通过	92 ms	13.1 MB
# 缺陷：整数反转后可能出现整数溢出问题，所以可以考虑“反转一半数字”
class Solution:
    def isPalindrome(self, x: int) -> bool:
        # 特判：x为负，一定不是回文
        if x < 0:
            return False
        # 反转整数
        x_reverse = list(str(x))
        x_reverse.reverse()
        x_reverse = int(''.join(x_reverse))
        if x_reverse == x:
            return True
        else:
            return False
'''
# [2] 中心扩散法 --> 通过	76 ms	13 MB
class Solution:
    def isPalindrome(self, x: int) -> bool:
        # 特判：x为负，一定不是回文
        if x < 0:
            return False
        # 中心扩散法
        # 获取x长度，判断奇偶
        digit = len(str(x))
        x = str(x)
        center = digit // 2
        # 左右指针
        left = center - 1
        if digit % 2 == 0:
            right = center
        else:
            right = center + 1
        # 左右指针向外扩散，判断对应字符是否相等
        while(left >= 0 and right <= digit-1):
            if x[left] != x[right]:
                return False
            left -= 1
            right += 1
        return True
'''
# [3] 反转一半整数 --> 通过	84 ms	13 MB
class Solution:
    def isPalindrome(self, x: int) -> bool:
        # 特判：x为负，一定不是回文；x最低位为0，一定不是回文（除了0本身）
        if x < 0 or (x % 10 == 0 and x != 0):
            return False
        # 反转一半整数（数学方法：弹入和推出数字）
        reverse = 0
        while(x > reverse):
            reverse = reverse * 10 + x % 10
            x //= 10
        return x == reverse or x == (reverse // 10)
'''
# @lc code=end

