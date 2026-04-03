#
# @lc app=leetcode.cn id=142 lang=python3
# @lcpr version=30204
#
# [142] 环形链表 II
#


# @lcpr-template-start
from typing import Optional

# @lcpr-template-end
# @lc code=start
class Solution:
    """
    142. 环形链表 II - Floyd 判圈算法

    核心思想：
    分两步找到环的入口节点：
    1. 判断是否有环：快慢指针，快指针每次走 2 步，慢指针每次走 1 步。
       如果相遇，说明有环。
    2. 找环入口：从相遇点开始，再用一个指针从 head 出发，两个指针每次都走 1 步，
       再次相遇的节点就是环的入口。

    数学证明（为什么第二步能找到入口）：
    设 head 到环入口距离为 a，环入口到相遇点距离为 b，相遇点到环入口距离为 c。
    - 慢指针走的距离：a + b
    - 快指针走的距离：a + b + n(b + c) = 2(a + b)
    - 化简得：a = c + (n-1)(b + c)
    这意味着：从 head 走 a 步，和从相遇点走 c 步（再走 n-1 圈），会同时到达环入口。

    时间复杂度：O(n)
    空间复杂度：O(1)
    """

    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # 步骤1：快慢指针找相遇点
        slow = fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if fast is slow:  # 相遇，说明有环
                # 步骤2：一个指针从 head 出发，一个从相遇点出发
                while slow is not head:
                    slow = slow.next
                    head = head.next
                return slow  # 再次相遇的点就是环入口

        # 无环
        return None

        # 方法二：哈希表
        # node_set = set()
        # while head:
        #     if head in node_set:
        #         return head
        #     node_set.add(head)
        #     head = head.next
        # return None


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
        return nodes[0], nodes[pos] if pos >= 0 else None

    sol = Solution()

    tests = [
        ([3, 2, 0, -4], 1),   # 环入口是索引 1（值为 2）
        ([1, 2], 0),          # 环入口是索引 0（值为 1）
        ([1], -1),            # 无环
    ]

    print("环形链表 II - 测试开始")
    for i, (values, pos) in enumerate(tests, 1):
        head, expected = build_cycle(values, pos)
        result = sol.detectCycle(head)
        passed = result == expected
        status = "PASS" if passed else "FAIL"
        expected_str = expected.val if expected else None
        result_str = result.val if result else None
        print(f"测试 {i}: values={values}, pos={pos} -> {status}")
        if not passed:
            print(f"  输出: {result_str}")
            print(f"  期望: {expected_str}")
    print("测试结束")
