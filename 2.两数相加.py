#
# @lc app=leetcode.cn id=2 lang=python3
#
# [2] 两数相加
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

# [1] 遍历链表 --> 通过	76 ms	13.2 MB
class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        res = ListNode((l1.val + l2.val) % 10)
        # 进位标识
        carry = (l1.val + l2.val) // 10
        # p指向res
        p = res
        while(l1.next and l2.next):
            l1 = l1.next
            l2 = l2.next
            p.next = ListNode((l1.val + l2.val + carry) % 10)
            carry = (l1.val + l2.val + carry) // 10
            p = p.next
        # l1可能没有遍历完全
        while(l1.next):
            l1 = l1.next
            if not carry:
                p.next = l1
                break
            p.next = ListNode((l1.val + carry) % 10)
            carry = (l1.val + carry) // 10
            p = p.next
        # l2可能没有遍历完全
        while(l2.next):
            l2 = l2.next
            if not carry:
                p.next = l2
                break
            p.next = ListNode((l2.val + carry) % 10)
            carry = (l2.val + carry) // 10
            p = p.next
        # 如果最高位相加仍有进位，那么添加一位
        if carry:
            p.next = ListNode(carry)
        return res

'''
# [2] 遍历链表 --> 通过	116 ms	13.3 MB
class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        # 哑结点
        res = ListNode(0)
        # 进位标识
        carry = 0
        # p指向res
        p = res
        # 减少代码冗余度
        while(l1 or l2):
            x = l1.val if l1 else 0
            y = l2.val if l2 else 0
            sum = x + y + carry
            carry = sum // 10
            p.next = ListNode(sum % 10)
            p = p.next
            l1 = l1.next if l1 else l1
            l2 = l2.next if l2 else l2
        if carry:
            p.next = ListNode(carry)
        return res.next
''' 
# @lc code=end

