#
# @lc app=leetcode.cn id=19 lang=python3
# @lcpr version=30204
#
# [19] 删除链表的倒数第 N 个结点
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
    删除链表的倒数第 N 个结点 - 双指针（快慢指针）

    核心思想：
    使用两个指针，让快指针先走 n 步，然后快慢指针一起走。
    当快指针到达末尾时，慢指针正好在倒数第 n+1 个位置（即要删除节点的前一个）。

    为什么用 dummy 节点？
    如果删除的是头节点，需要特殊处理。使用 dummy 节点可以统一逻辑，
    让 slow 最终停在要删除节点的前一个位置。

    步骤：
    1. first 先走 n 步
    2. first 和 second 同时走，直到 first 到达末尾
    3. second.next 指向 second.next.next，删除目标节点

    时间复杂度：O(L)，L 是链表长度，只遍历一次
    空间复杂度：O(1)
    """
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        # 创建 dummy 节点，简化边界处理
        dummy = ListNode(0, head)

        # first 先走 n 步
        first = head
        for i in range(n):
            first = first.next

        # second 从 dummy 开始，最终停在要删除节点的前一个
        second = dummy

        # first 和 second 同时走，直到 first 到达末尾
        while first:
            first = first.next
            second = second.next

        # 删除倒数第 n 个节点
        second.next = second.next.next

        return dummy.next


# ========== 示例推演：head = [1,2,3,4,5], n = 2 ==========
#
# 初始：dummy -> 1 -> 2 -> 3 -> 4 -> 5
#       first指向1，second指向dummy
#
# first 先走2步：first指向3
#
# 同时走：
#   first=3, second=dummy
#   first=4, second=1
#   first=5, second=2
#   first=None, second=3
#
# second=3，删除 second.next（即节点4）
# 结果：dummy -> 1 -> 2 -> 3 -> 5
# @lc code=end



#
# @lcpr case=start
# [1,2,3,4,5]\n2\n
# @lcpr case=end

# @lcpr case=start
# [1]\n1\n
# @lcpr case=end

# @lcpr case=start
# [1,2]\n1\n
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
        ([1, 2, 3, 4, 5], 2, [1, 2, 3, 5]),
        ([1], 1, []),
        ([1, 2], 1, [1]),
        ([1, 2], 2, [2]),
    ]

    for head, n, expected in tests:
        result = _to_list(sol.removeNthFromEnd(_to_node(head), n))
        print(f"removeNthFromEnd({head}, {n}) = {result}, expected = {expected}")
