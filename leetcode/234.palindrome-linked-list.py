#
# @lc app=leetcode.cn id=234 lang=python3
# @lcpr version=30204
#
# [234] 回文链表
#


# @lcpr-template-start

# @lcpr-template-end
# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
# 一眼双指针
# 能不能修改原链表？尽量不要
# 经典题目
from typing import Optional
class Solution:
    # 876. 链表的中间结点
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        slow = fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        return slow

    # 206. 反转链表
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        pre, cur = None, head
        while cur:
            nxt = cur.next
            cur.next = pre
            pre = cur
            cur = nxt
        return pre

    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        mid = self.middleNode(head)
        head2 = h2 = self.reverseList(mid)
        while head2:
            if head.val != head2.val:  # 不是回文链表
                self.reverseList(h2)  # 复原
                return False
            head = head.next
            head2 = head2.next
        self.reverseList(h2)  # 复原
        return True

# @lc code=end



#
# @lcpr case=start
# [1,2,2,1]\n
# @lcpr case=end

# @lcpr case=start
# [1,2]\n
# @lcpr case=end

#

