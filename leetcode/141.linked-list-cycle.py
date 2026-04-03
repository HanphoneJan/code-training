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
from typing import Optional

# @lcpr-template-end
# @lc code=start
class Solution:
    """
    141. 环形链表 - 快慢指针（Floyd 判圈算法）

    核心思想：
    把链表想象成跑道，如果有环，跑得快的人一定会追上跑得慢的人。
    - 慢指针 slow 每次走 1 步
    - 快指针 fast 每次走 2 步

    为什么一定能追上？
    如果链表有环，快指针会先入环，然后在环内绕圈。
    慢指针入环后，快指针相对于慢指针的速度是 1 步/轮，所以一定会在某轮相遇。

    时间复杂度：O(n)，无环时 fast 走到末尾；有环时最多走一圈半
    空间复杂度：O(1)
    """

    def hasCycle(self, head: Optional[ListNode]) -> bool:
        # 快慢指针初始化都指向头节点
        slow, fast = head, head

        while fast and fast.next:
            slow = slow.next          # 慢指针走 1 步
            fast = fast.next.next     # 快指针走 2 步
            if slow == fast:          # 相遇，说明有环
                return True

        # fast 走到链表末尾，说明无环
        return False

        # 方法二：哈希表存储节点
        # node_set = set()
        # while head:
        #     if head in node_set:
        #         return True
        #     node_set.add(head)
        #     head = head.next
        # return False


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


if __name__ == "__main__":
    # 辅助函数：构建带环链表
    def build_cycle(values, pos):
        if not values:
            return None
        nodes = [ListNode(v) for v in values]
        for i in range(len(nodes) - 1):
            nodes[i].next = nodes[i + 1]
        if pos >= 0:
            nodes[-1].next = nodes[pos]
        return nodes[0]

    sol = Solution()

    tests = [
        ([3, 2, 0, -4], 1, True),   # 尾节点指向索引 1
        ([1, 2], 0, True),          # 尾节点指向索引 0
        ([1], -1, False),           # 无环
        ([], -1, False),            # 空链表
    ]

    print("环形链表 - 测试开始")
    for i, (values, pos, expected) in enumerate(tests, 1):
        head = build_cycle(values, pos)
        result = sol.hasCycle(head)
        passed = result == expected
        status = "PASS" if passed else "FAIL"
        print(f"测试 {i}: values={values}, pos={pos} -> {status}")
        if not passed:
            print(f"  输出: {result}")
            print(f"  期望: {expected}")
    print("测试结束")
