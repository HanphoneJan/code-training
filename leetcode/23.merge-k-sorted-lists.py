#
# @lc app=leetcode.cn id=23 lang=python3
# @lcpr version=30204
#
# [23] 合并 K 个升序链表
#


# @lcpr-template-start

# @lcpr-template-end
# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
from typing import List,Optional

class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if len(lists) == 0:
            return None
        if len(lists) == 1:
            return lists[0]
        for i in range(len(lists)-1):
            lists[0]=self.mergeTwoLists(lists[0],lists[i+1])
        return lists[0]

    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        if list1 is None:
            return list2
        if list2 is None:
            return list1 
        first = list1
        second = list2
        ans = head = list1
        if first.val <= second.val:
            ans = head = list1
            first = first.next
        else:
            ans = head = list2
            second = second.next
        while head:
            if first is None:
                head.next=second
                break
            if second is None:
                head.next= first
                break
            if first.val <= second.val:
                head.next = first
                first = first.next
            else:
                head.next = second
                second = second.next
            head=head.next
        return ans
# @lc code=end



#
# @lcpr case=start
# [[1,4,5],[1,3,4],[2,6]]\n
# @lcpr case=end

# @lcpr case=start
# []\n
# @lcpr case=end

# @lcpr case=start
# [[]]\n
# @lcpr case=end

#

