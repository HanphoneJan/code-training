#
# @lc app=leetcode.cn id=148 lang=python3
# @lcpr version=30204
#
# [148] 排序链表
#


# @lcpr-template-start
from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


# @lcpr-template-end
# @lc code=start
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
#
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
#
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
    """
    148. 排序链表 - 归并排序（自底向上迭代法）

    核心思想：
    要求时间复杂度 O(n log n)，空间复杂度 O(1)（递归法的空间是 O(log n)）。
    使用自底向上的归并排序：
    1. 先计算链表长度
    2. 按 step = 1, 2, 4, 8... 的步长，将链表分段排序合并
    3. 每轮合并后，链表的有序段长度翻倍

    关键操作：
    - splitList(head, size)：从 head 开始，分割出前 size 个节点，返回剩余链表头
    - mergeTwoLists(l1, l2)：合并两个有序链表，返回新头和新尾

    时间复杂度：O(n log n)
    空间复杂度：O(1)
    """

    # 获取链表长度
    def getListLength(self, head: Optional[ListNode]) -> int:
        length = 0
        while head:
            length += 1
            head = head.next
        return length

    # 分割链表
    # 如果链表长度 <= size，返回 None（无需分割）
    # 否则把前 size 个节点断开，返回剩余链表的头节点
    def splitList(self, head: Optional[ListNode], size: int) -> Optional[ListNode]:
        cur = head
        for _ in range(size - 1):
            if cur is None:
                break
            cur = cur.next

        if cur is None or cur.next is None:
            return None

        next_head = cur.next
        cur.next = None  # 断开连接
        return next_head

    # 合并两个有序链表，返回 (新头节点, 新尾节点)
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]):
        cur = dummy = ListNode()  # 哨兵节点
        while list1 and list2:
            if list1.val < list2.val:
                cur.next = list1
                list1 = list1.next
            else:
                cur.next = list2
                list2 = list2.next
            cur = cur.next
        cur.next = list1 or list2  # 拼接剩余
        while cur.next:
            cur = cur.next
        return dummy.next, cur

    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        length = self.getListLength(head)
        dummy = ListNode(next=head)
        step = 1

        while step < length:
            new_list_tail = dummy
            cur = dummy.next
            while cur:
                head1 = cur
                head2 = self.splitList(head1, step)
                cur = self.splitList(head2, step)
                head, tail = self.mergeTwoLists(head1, head2)
                new_list_tail.next = head
                new_list_tail = tail
            step *= 2

        return dummy.next


# 我能写出来的链表的冒泡排序，但是会超时
# class Solution:
#     def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
#         cur = head
#         n = 0
#         while cur:
#             cur = cur.next
#             n += 1
#         if n <= 1:
#             return head
#         cur = head
#         for i in range(n):
#             cur = head
#             swapped = False
#             for _ in range(0, n - i - 1):
#                 if cur.next and cur.val > cur.next.val:
#                     cur.val, cur.next.val = cur.next.val, cur.val
#                     swapped = True
#                 cur = cur.next
#             if not swapped:
#                 break
#         return head
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


if __name__ == "__main__":
    # 辅助函数
    def build_list(values):
        dummy = ListNode()
        cur = dummy
        for v in values:
            cur.next = ListNode(v)
            cur = cur.next
        return dummy.next

    def list_to_array(head):
        res = []
        while head:
            res.append(head.val)
            head = head.next
        return res

    sol = Solution()

    tests = [
        ([4, 2, 1, 3], [1, 2, 3, 4]),
        ([-1, 5, 3, 4, 0], [-1, 0, 3, 4, 5]),
        ([], []),
        ([1], [1]),
        ([2, 1], [1, 2]),
    ]

    print("排序链表 - 测试开始")
    for i, (values, expected) in enumerate(tests, 1):
        head = build_list(values)
        result = list_to_array(sol.sortList(head))
        passed = result == expected
        status = "PASS" if passed else "FAIL"
        print(f"测试 {i}: values={values} -> {status}")
        if not passed:
            print(f"  输出: {result}")
            print(f"  期望: {expected}")
    print("测试结束")
