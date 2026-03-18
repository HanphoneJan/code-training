#
# @lc app=leetcode.cn id=21 lang=python3
# @lcpr version=30204
#
# [21] 合并两个有序链表
# 题目：将两个升序链表合并为一个新的升序链表
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
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        """
        核心思想：双指针逐个比较

        合并有序链表的策略：
        - 比较两个链表当前节点的值
        - 将较小值的节点接到结果链表
        - 移动较小值链表的头指针
        - 重复直到其中一个链表为空
        - 将非空链表的剩余部分直接接上

        为什么不用新建节点？
        可以直接复用原链表的节点，通过改变 next 指针来重组链表，
        这样空间复杂度是 O(1)。

        时间复杂度：O(n+m)，n和m分别是两个链表的长度
        空间复杂度：O(1)，只使用常数额外空间
        """
        # 边界情况处理：如果其中一个链表为空，直接返回另一个
        if list1 is None:
            return list2
        if list2 is None:
            return list1

        # 用 first 和 second 分别遍历两个链表
        first = list1
        second = list2

        # 确定新链表的头节点
        # 比较两个链表的第一个节点，较小的作为头节点
        if first.val <= second.val:
            ans = head = first  # head 用于遍历，ans 保存头节点
            first = first.next  # first 移动到下一个节点
        else:
            ans = head = second
            second = second.next

        # 遍历两个链表，逐个比较并连接
        while head:
            # 情况1：first 已经遍历完，将 second 的剩余部分接上
            if first is None:
                head.next = second
                break

            # 情况2：second 已经遍历完，将 first 的剩余部分接上
            if second is None:
                head.next = first
                break

            # 情况3：两个链表都还有节点，比较并连接较小的
            if first.val <= second.val:
                head.next = first  # 将 first 节点接到结果链表
                first = first.next  # first 指针前移
            else:
                head.next = second
                second = second.next

            # 结果链表的头指针前移
            head = head.next

        return ans


# ========== 示例推演：list1 = [1,2,4], list2 = [1,3,4] ==========
#
# 初始：
#   list1: 1 -> 2 -> 4
#   list2: 1 -> 3 -> 4
#
# 确定头节点：list1.val=1 <= list2.val=1，ans = head = list1[0]，first指向list1[1]
#   ans: 1 (来自list1)
#
# 第1轮：first.val=2, second.val=1
#   second.val 较小，head.next = list2[0]，second指向list2[1]
#   ans: 1 -> 1
#   head = head.next（指向第二个节点）
#
# 第2轮：first.val=2, second.val=3
#   first.val 较小，head.next = list1[1]，first指向list1[2]
#   ans: 1 -> 1 -> 2
#
# 第3轮：first.val=4, second.val=3
#   second.val 较小，head.next = list2[1]，second指向list2[2]
#   ans: 1 -> 1 -> 2 -> 3
#
# 第4轮：first.val=4, second.val=4
#   first.val <= second.val，head.next = list1[2]，first变为None
#   ans: 1 -> 1 -> 2 -> 3 -> 4
#
# 第5轮：first is None，head.next = second（list2[2]）
#   ans: 1 -> 1 -> 2 -> 3 -> 4 -> 4
#   break
#
# 最终结果：[1,1,2,3,4,4]
# @lc code=end


# @lcpr case=start
# [1,2,4]\n[1,3,4]\n
# @lcpr case=end

# @lcpr case=start
# []\n[]\n
# @lcpr case=end

# @lcpr case=start
# []\n[0]\n
# @lcpr case=end

#
