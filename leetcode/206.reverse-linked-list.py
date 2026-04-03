#
# @lc app=leetcode.cn id=206 lang=python3
# @lcpr version=30204
#
# [206] 反转链表
#

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
# @lcpr-template-start

# @lcpr-template-end
# @lc code=start
# Definition for singly-linked list.
# 链表的经典操作
from typing import Optional
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None or head.next is None:
            return head
        cur = head
        pre = None # 为什么是存储pre而不是next，pre和next和next.next的使用场景
        while cur:
            tmp = cur.next
            cur.next = pre
            pre = cur
            cur = tmp
        return pre
# @lc code=end



#
# @lcpr case=start
# [1,2,3,4,5]\n
# @lcpr case=end

# @lcpr case=start
# [1,2]\n
# @lcpr case=end

# @lcpr case=start
# []\n
# @lcpr case=end

#

