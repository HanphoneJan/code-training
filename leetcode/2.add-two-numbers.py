#
# @lc app=leetcode.cn id=2 lang=python3
# @lcpr version=30204
#
# [2] 两数相加
#


# @lcpr-template-start

# @lcpr-template-end
# @lc code=start
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

from typing import Optional

class Solution:
    """
    两数相加 - 链表模拟加法

    核心思想：
    模拟手工加法过程，从链表头（个位）开始逐位相加，处理进位。

    为什么选择递归？
    链表的结构天然适合递归处理，每次处理当前节点，递归处理后续节点。

    关键点：
    1. 进位 carry 的处理：s // 10 得到新的进位
    2. 边界情况：当一个链表为空时，与0相加
    3. 最终进位：如果最后还有进位，需要新增一个节点

    时间复杂度：O(max(m,n))，m和n是两个链表的长度
    空间复杂度：O(max(m,n))，递归栈的深度
    """
    # l1 和 l2 为当前遍历的节点，carry 为进位
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode], carry=0) -> Optional[ListNode]:
        if l1 is None and l2 is None:  # 递归边界
            return ListNode(carry) if carry else None  # 如果进位了，就额外创建一个节点
        if l1 is None:  # 如果 l1 是空的，那么此时 l2 一定不是空节点
            l1, l2 = l2, l1  # 交换 l1 与 l2，保证 l1 非空，从而简化代码
        s = carry + l1.val + (l2.val if l2 else 0)  # 节点值和进位加在一起
        l1.val = s % 10  # 每个节点保存一个数位（直接修改原链表）
        l1.next = self.addTwoNumbers(l1.next, l2.next if l2 else None, s // 10)  # 进位
        return l1


# ========== 示例推演：l1 = [2,4,3], l2 = [5,6,4] ==========
#
# 表示的数字：342 + 465 = 807
#
# 第1轮：l1.val=2, l2.val=5, carry=0
#   s = 0 + 2 + 5 = 7
#   l1.val = 7 % 10 = 7
#   carry = 7 // 10 = 0
#   递归处理 l1.next, l2.next
#
# 第2轮：l1.val=4, l2.val=6, carry=0
#   s = 0 + 4 + 6 = 10
#   l1.val = 10 % 10 = 0
#   carry = 10 // 10 = 1
#
# 第3轮：l1.val=3, l2.val=4, carry=1
#   s = 1 + 3 + 4 = 8
#   l1.val = 8 % 10 = 8
#   carry = 8 // 10 = 0
#
# 递归结束，返回 l1 = [7,0,8]
# @lc code=end



#
# @lcpr case=start
# [2,4,3]\n[5,6,4]\n
# @lcpr case=end

# @lcpr case=start
# [0]\n[0]\n
# @lcpr case=end

# @lcpr case=start
# [9,9,9,9,9,9,9]\n[9,9,9,9]\n
# @lcpr case=end

#


if __name__ == "__main__":

    def _to_list(node):
        res = []
        while node:
            res.append(node.val)
            node = node.next
        return res

    def _to_node(arr):
        if not arr:
            return None
        head = ListNode(arr[0])
        cur = head
        for v in arr[1:]:
            cur.next = ListNode(v)
            cur = cur.next
        return head

    sol = Solution()

    tests = [
        ([2, 4, 3], [5, 6, 4], [7, 0, 8]),
        ([0], [0], [0]),
        ([9, 9, 9, 9, 9, 9, 9], [9, 9, 9, 9], [8, 9, 9, 9, 0, 0, 0, 1]),
    ]

    for l1, l2, expected in tests:
        result = _to_list(sol.addTwoNumbers(_to_node(l1), _to_node(l2)))
        print(f"addTwoNumbers({l1}, {l2}) = {result}, expected = {expected}")
