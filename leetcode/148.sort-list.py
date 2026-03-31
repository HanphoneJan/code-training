#
# @lc app=leetcode.cn id=148 lang=python3
# @lcpr version=30204
#
# [148] 排序链表
#


# @lcpr-template-start

# @lcpr-template-end
# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:



        
        # 链表的冒泡排序，会超时
        # cur = head
        # n = 0
        # while cur:
        #     cur = cur.next
        #     n+=1
        # if n<=1:
        #     return head
        # cur = head
        # for i in range(n):
        #     cur = head
        #     swapped = False
        #     for _ in range(0,n-i-1):
        #         if cur.next and cur.val > cur.next.val:
        #             cur.val,cur.next.val = cur.next.val,cur.val
        #             swapped = True
        #         cur = cur.next
        #     if not swapped:
        #         break
        # return head
# @lc code=end



#
# @lcpr case=start
# [4,2,1,3]\n
# @lcpr case=end

# @lcpr case=start
# [-1,5,3,4,0]\n
# @lcpr case=end

# @lcpr case=start
# []\n
# @lcpr case=end

#

