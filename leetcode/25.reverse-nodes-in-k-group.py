#
# @lc app=leetcode.cn id=25 lang=python3
# @lcpr version=30204
#
# [25] K 个一组翻转链表
#


# @lcpr-template-start

# @lcpr-template-end
# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

# ACM 模式兼容：在非 LeetCode 环境下定义 ListNode（LeetCode 环境已预定义）
try:
    ListNode
except NameError:
    class ListNode:
        def __init__(self, val=0, next=None):
            self.val = val
            self.next = next

class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        """
        K个一组翻转链表

        核心思想：分段翻转
        1. 先统计链表长度，确定需要翻转多少组
        2. 每组内部进行链表翻转
        3. 连接上一组的尾部和下一组的头部

        链表翻转技巧：
        - 使用三个指针：prev, curr, next
        - curr.next = prev 实现反向
        - 注意保存下一组的起始节点
        """
        if not head or k <= 1:
            return head

        # 创建虚拟头节点，简化边界处理
        dummy = ListNode(0)
        dummy.next = head
        group_prev = dummy  # 当前组的前一个节点

        while True:
            # 检查是否还有k个节点
            # ktail 指向当前组的最后一个节点
            ktail = group_prev
            for _ in range(k):
                ktail = ktail.next
                if not ktail:
                    # 不足k个，直接返回
                    return dummy.next

            # 记录下一组的起始节点
            group_next = ktail.next

            # 翻转当前组 [group_prev.next, ktail]
            # 翻转后：group_prev.next 变成组的尾，ktail 变成组的头
            prev = ktail.next  # 翻转后的尾部指向下一组的头
            curr = group_prev.next  # 当前组的第一个节点

            # 标准链表翻转
            while curr != group_next:
                next_temp = curr.next
                curr.next = prev
                prev = curr
                curr = next_temp

            # 更新连接：group_prev 现在指向 ktail（翻转后的头）
            # 但需要先保存原来的头（现在的尾）
            temp = group_prev.next
            group_prev.next = ktail
            group_prev = temp  # 移动到下一组的前一个位置


# @lc code=end



#
# @lcpr case=start
# [1,2,3,4,5]\n2\n
# @lcpr case=end

# @lcpr case=start
# [1,2,3,4,5]\n3\n
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
        ([1, 2, 3, 4, 5], 2, [2, 1, 4, 3, 5]),
        ([1, 2, 3, 4, 5], 3, [3, 2, 1, 4, 5]),
        ([1, 2], 1, [1, 2]),
        ([1], 1, [1]),
    ]

    for head, k, expected in tests:
        result = _to_list(sol.reverseKGroup(_to_node(head), k))
        print(f"reverseKGroup({head}, {k}) = {result}, expected = {expected}")
