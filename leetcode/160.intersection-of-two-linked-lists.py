#
# @lc app=leetcode.cn id=160 lang=python3
# @lcpr version=30204
#
# [160] 相交链表
#


# @lcpr-template-start
from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


# @lcpr-template-end
# @lc code=start
class Solution:
    """
    160. 相交链表 - 双指针（浪漫相遇法）

    核心思想：
    设链表 A 长度为 a + c，链表 B 长度为 b + c，其中 c 是公共部分长度。
    让两个指针 p 和 q 同时分别从 headA 和 headB 出发，走到末尾后跳到另一条链表的头。

    走过的路径：
    - p：a + c + b
    - q：b + c + a

    如果存在交点，它们一定会在公共部分的起点相遇（走 a + c + b = b + c + a 步后）。
    如果不存在交点，它们会同时走到 None。

    为什么能相遇？
    两个指针走过的总路程相等，如果前面不同部分长度分别为 a 和 b，
    那么在交换起点后，刚好补齐了长度差，同时到达交点。

    时间复杂度：O(a + b)
    空间复杂度：O(1)
    """

    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        p, q = headA, headB
        while p is not q:
            # 如果 p 走到末尾，跳到 headB；否则继续走
            p = p.next if p else headB
            # 如果 q 走到末尾，跳到 headA；否则继续走
            q = q.next if q else headA
        return p  # 相遇点（交点或 None）


# @lc code=end


#
# @lcpr case=start
# 8\n[4,1,8,4,5]\n[5,6,1,8,4,5]\n2\n3\n
# @lcpr case=end

# @lcpr case=start
# 2\n[1,9,1,2,4]\n[3,2,4]\n3\n1\n
# @lcpr case=end

# @lcpr case=start
# 0\n[2,6,4]\n[1,5]\n3\n2\n
# @lcpr case=end


if __name__ == "__main__":
    # 辅助函数：构建相交链表
    def build_intersection(skipA, skipB, listA, listB, intersectVal):
        if intersectVal == 0:
            # 不相交
            dummyA = ListNode(0)
            cur = dummyA
            for v in listA:
                cur.next = ListNode(v)
                cur = cur.next
            dummyB = ListNode(0)
            cur = dummyB
            for v in listB:
                cur.next = ListNode(v)
                cur = cur.next
            return dummyA.next, dummyB.next, None

        nodesA = [ListNode(v) for v in listA]
        nodesB = [ListNode(v) for v in listB]
        for i in range(len(nodesA) - 1):
            nodesA[i].next = nodesA[i + 1]
        for i in range(len(nodesB) - 1):
            nodesB[i].next = nodesB[i + 1]

        # 找到交点
        intersect_node = nodesA[skipA]
        nodesB[skipB].next = intersect_node
        return nodesA[0], nodesB[0], intersect_node

    sol = Solution()

    print("相交链表 - 测试开始")

    # 测试 1
    headA, headB, expected = build_intersection(
        2, 3, [4, 1, 8, 4, 5], [5, 6, 1, 8, 4, 5], 8
    )
    result = sol.getIntersectionNode(headA, headB)
    passed = result == expected
    print(f"测试 1: 交点值=8 -> {'PASS' if passed else 'FAIL'}")

    # 测试 2
    headA, headB, expected = build_intersection(
        3, 1, [1, 9, 1, 2, 4], [3, 2, 4], 2
    )
    result = sol.getIntersectionNode(headA, headB)
    passed = result == expected
    print(f"测试 2: 交点值=2 -> {'PASS' if passed else 'FAIL'}")

    # 测试 3（不相交）
    headA, headB, expected = build_intersection(
        3, 2, [2, 6, 4], [1, 5], 0
    )
    result = sol.getIntersectionNode(headA, headB)
    passed = result == expected
    print(f"测试 3: 不相交 -> {'PASS' if passed else 'FAIL'}")

    print("测试结束")
