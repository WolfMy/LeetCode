#
# @lc app=leetcode.cn id=13 lang=python3
#
# [13] 罗马数字转整数
#

# @lc code=start
# [1] 哈希表 --> 56 ms	13.2 MB
class Solution:
    def romanToInt(self, s: str) -> int:
        hasmap = {
            'CM':900, 'CD':400, 'XC':90, 'XL':40, 'IX':9, 'IV':4,
            'M':1000, 'D':500, 'C':100, 'L':50,  'X':10,  'V':5, 'I':1
        }
        res = 0
        for key, value in hasmap.items():
            count = s.count(key)
            if count > 0:
                res += count * value
                s = s.replace(key, '')
        return res
'''
# [2] 哈希表 --> 76 ms	13 MB
class Solution:
    def romanToInt(self, s: str) -> int:
        hasmap = {
            'M':1000, 'D':500, 'C':100, 'L':50, 'X':10,  'V':5, 'I':1
        }
        res = 0
        for i in range(len(s)-1):
            if hasmap[s[i]] >= hasmap[s[i+1]]:
                res += hasmap[s[i]]
            else:
                res -= hasmap[s[i]]
        res += hasmap[s[-1]]
        return res
'''  
# @lc code=end

