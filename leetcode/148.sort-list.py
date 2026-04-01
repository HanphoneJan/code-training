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
# 实现归并排序还是比较复杂的；集成归并排序+递归/迭代+链表操作的经典题目
from typing import Optional


# 分治+递归做法
# class Solution:
#     # 876. 链表的中间结点（快慢指针）
#     def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
#         slow = fast = head
#         while fast and fast.next:
#             pre = slow  # 记录 slow 的前一个节点
#             slow = slow.next
#             fast = fast.next.next
#         pre.next = None  # 断开 slow 的前一个节点和 slow 的连接
#         return slow

#     # 21. 合并两个有序链表（双指针）
#     def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
#         cur = dummy = ListNode()  # 用哨兵节点简化代码逻辑
#         while list1 and list2:
#             if list1.val < list2.val:
#                 cur.next = list1  # 把 list1 加到新链表中
#                 list1 = list1.next
#             else:  # 注：相等的情况加哪个节点都是可以的
#                 cur.next = list2  # 把 list2 加到新链表中
#                 list2 = list2.next
#             cur = cur.next
#         cur.next = list1 if list1 else list2  # 拼接剩余链表
#         return dummy.next

#     def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
#         # 如果链表为空或者只有一个节点，无需排序
#         if head is None or head.next is None:
#             return head
#         # 找到中间节点 head2，并断开 head2 与其前一个节点的连接
#         # 比如 head=[4,2,1,3]，那么 middleNode 调用结束后 head=[4,2] head2=[1,3]
#         head2 = self.middleNode(head)
#         # 分治
#         head = self.sortList(head)
#         head2 = self.sortList(head2)
#         # 合并
#         return self.mergeTwoLists(head, head2)
class Solution:
    # 获取链表长度
    def getListLength(self, head: Optional[ListNode]) -> int:
        length = 0
        while head:
            length += 1
            head = head.next
        return length

    # 分割链表
    # 如果链表长度 <= size，不做任何操作，返回空节点
    # 如果链表长度 > size，把链表的前 size 个节点分割出来（断开连接），并返回剩余链表的头节点
    def splitList(self, head: Optional[ListNode], size: int) -> Optional[ListNode]:
        # 先找到 next_head 的前一个节点
        cur = head
        for _ in range(size - 1):
            if cur is None:
                break
            cur = cur.next

        # 如果链表长度 <= size
        if cur is None or cur.next is None:
            return None  # 不做任何操作，返回空节点

        next_head = cur.next
        cur.next = None  # 断开 next_head 的前一个节点和 next_head 的连接
        return next_head

    # 21. 合并两个有序链表（双指针）
    # 返回合并后的链表的头节点和尾节点
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        cur = dummy = ListNode()  # 用哨兵节点简化代码逻辑
        while list1 and list2:
            if list1.val < list2.val:
                cur.next = list1  # 把 list1 加到新链表中
                list1 = list1.next
            else:  # 注：相等的情况加哪个节点都是可以的
                cur.next = list2  # 把 list2 加到新链表中
                list2 = list2.next
            cur = cur.next
        cur.next = list1 or list2  # 拼接剩余链表
        while cur.next:
            cur = cur.next
        # 循环结束后，cur 是合并后的链表的尾节点
        return dummy.next, cur

    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        length = self.getListLength(head)  # 获取链表长度
        dummy = ListNode(next=head)  # 用哨兵节点简化代码逻辑
        step = 1  # 步长（参与合并的链表长度）
        while step < length:
            new_list_tail = dummy  # 新链表的末尾
            cur = dummy.next  # 每轮循环的起始节点
            while cur:
                # 从 cur 开始，分割出两段长为 step 的链表，头节点分别为 head1 和 head2
                head1 = cur
                head2 = self.splitList(head1, step)
                cur = self.splitList(head2, step)  # 下一轮循环的起始节点
                # 合并两段长为 step 的链表
                head, tail = self.mergeTwoLists(head1, head2)
                # 合并后的头节点 head，插到 new_list_tail 的后面
                new_list_tail.next = head
                new_list_tail = tail  # tail 现在是新链表的末尾
            step *= 2
        return dummy.next


# 我能写出来的链表的冒泡排序，但是会超时
# class Solution:        
#     def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
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

