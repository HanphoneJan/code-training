#
# @lc app=leetcode.cn id=141 lang=python3
# @lcpr version=30204
#
# [141] 环形链表
#
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

# @lcpr-template-start

# @lcpr-template-end
# @lc code=start
from typing import Optional
class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        node_set=set()
        while head:
            if head in node_set:
                return True
            node_set.add(head)
            head = head.next
        return False
# @lc code=end



#
# @lcpr case=start
# [3,2,0,-4]\n1\n
# @lcpr case=end

# @lcpr case=start
# [1,2]\n0\n
# @lcpr case=end

# @lcpr case=start
# [1]\n-1\n
# @lcpr case=end

#

