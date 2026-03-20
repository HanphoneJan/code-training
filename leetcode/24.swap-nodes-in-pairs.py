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
        """
        核心思想：模拟两两交换

        每次处理一对节点 (first, second)，步骤：
        1. 保存下一对的起始位置（swap = second.next）
        2. 让 second.next 指向 first（完成本对交换）
        3. 让 prev.next 指向 second（连接到已处理的链表尾部）
        4. 让 first.next 指向下一对起始（暂时连上后续节点）
        5. 更新 prev、first、second，处理下一对

        时间复杂度：O(n)
        空间复杂度：O(1)
        """
        # 边界：0个或1个节点，无法组成一对，直接返回
        if head is None or head.next is None:
            return head
        first = head        # 每对中的第一个节点
        second = head.next  # 每对中的第二个节点
        ans = head.next     # 新链表的头节点（原来的第二个节点，交换后排到前面）
        prev = None         # 上一对的第一个节点（交换后变成尾部），用于连接两对之间
        while first and second:
            swap = second.next   # 保存下一对的起始节点
            second.next = first  # 交换：second 指向 first（核心操作）
            if prev is not None:
                prev.next = second  # 将上一对的尾部连接到当前对的新头（second）
            first.next = swap    # first 指向下一对的起始，暂时连上后续
            prev = first         # 更新 prev 为当前对的新尾（first）
            first = swap         # 移动到下一对的第一个节点
            if first is not None:
                second = first.next  # 下一对的第二个节点
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

