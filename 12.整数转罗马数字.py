#
# @lc app=leetcode.cn id=12 lang=python3
#
# [12] 整数转罗马数字
#

# @lc code=start
# 贪心算法 + 哈希表 --> 60 ms	13.2 MB
class Solution:
    def intToRoman(self, num: int) -> str:
        # 贪心算法 + 哈希表
        hasmap = {
            1000:'M', 900:'CM', 500:'D', 400:'CD', 100:'C', 90:'XC',
            50:'L', 40:'XL', 10:'X', 9:'IX', 5:'V', 4:'IV', 1:'I'
        }
        res = ''
        for key, value in hasmap.items():
            if num//key != 0:
                count = num // key
                num %= key
                res += value * count
        return res
        
# @lc code=end

