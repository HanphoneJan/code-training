#
# @lc app=leetcode.cn id=24 lang=python3
# @lcpr version=30204
#
# [24] 两两交换链表中的节点
#


# @lcpr-template-start

# @lcpr-template-end
# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
from typing import Optional
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None or head.next is None:
            return head
        first = head
        second = head.next
        ans = head.next
        prev = None
        while first and second:
            swap = second.next
            second.next = first
            if prev is not None:
                prev.next = second
            first.next = swap
            prev = first
            first = swap
            if first is not None:
                second = first.next
        return ans
# @lc code=end



#
# @lcpr case=start
# [1,2,3,4]\n
# @lcpr case=end

# @lcpr case=start
# []\n
# @lcpr case=end

# @lcpr case=start
# [1]\n
# @lcpr case=end

#

