#
# @lc app=leetcode.cn id=8 lang=python3
#
# [8] 字符串转换整数 (atoi)
#

# @lc code=start
# [1] 从头遍历法 --> 通过	36 ms	13.1 MB	
class Solution:
    def myAtoi(self, str: str) -> int:
        # 去掉首尾空格
        str = str.strip()
        # 不需要转换的情况
        if not str or (not str[0].isdigit() and str[0]!='-' and str[0]!='+'):
            # 字符串为空、第一个非空格字符不是一个有效整数字符
            return 0
        # 遍历法
        n = len(str)
        # 先找到'-'或第一个数字
        i = 0
        while(i < n and str[i]!='-' and str[i]!='+' and not str[i].isdigit()):
            i += 1
        # 再找到整数的结尾
        j = i + 1
        while(j < n and str[j].isdigit()):
            j += 1
        # 如果是'-'，那么返回0
        if str[i:j] == '-' or str[i:j] == '+':
            return 0
        num = int(str[i:j])
        if num < -2147483648:
            return -2147483648
        elif num > 2147483647:
            return 2147483647
        else:
            return num
"""
# [2] 正则表达式 --> 通过	48 ms	13.1 MB
class Solution:
    def myAtoi(self, str: str) -> int:
        '''
        1.使用正则表达式：
            ^：匹配字符串开头
            [\+\-]：代表一个+字符或-字符
            ?：前面一个字符可有可无
            \d：一个数字
            +：前面一个字符的一个或多个
            \D：一个非数字字符
            *：前面一个字符的0个或多个
        2.max(min(数字, 2**31 - 1), -2**31) 用来防止结果越界
        '''
        return max(min(int(*re.findall('^[\-\+]?\d+', str.strip())), 2**31-1), -2**31)
"""
        
# @lc code=end

