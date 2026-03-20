#
# @lc app=leetcode.cn id=23 lang=python3
# @lcpr version=30204
#
# [23] 合并 K 个升序链表
#


# @lcpr-template-start

# @lcpr-template-end
# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
from typing import List,Optional


# ACM 模式兼容：在非 LeetCode 环境下定义 ListNode（LeetCode 环境已预定义）
try:
    ListNode
except NameError:
    class ListNode:
        def __init__(self, val=0, next=None):
            self.val = val
            self.next = next

class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        """
        核心思想：逐一两两合并（复用合并两个有序链表的逻辑）

        策略：将 lists[0] 依次与 lists[1], lists[2], ... 合并
        每次合并后的结果存回 lists[0]，最终 lists[0] 就是答案。

        时间复杂度：O(k*N)，k 是链表数量，N 是节点总数
        注意：这不是最优方案（最优是分治合并，O(N log k)），但实现简单
        """
        # 边界：空列表
        if len(lists) == 0:
            return None
        # 边界：只有一个链表，直接返回
        if len(lists) == 1:
            return lists[0]
        # 依次将 lists[0] 与后续每个链表合并，结果存回 lists[0]
        for i in range(len(lists) - 1):
            lists[0] = self.mergeTwoLists(lists[0], lists[i + 1])
        return lists[0]

    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        """合并两个升序链表（双指针逐个比较）"""
        # 边界：其中一个为空，直接返回另一个
        if list1 is None:
            return list2
        if list2 is None:
            return list1
        first = list1
        second = list2
        # 确定新链表的头节点：值较小的节点作为头
        if first.val <= second.val:
            ans = head = list1  # ans 保存头节点用于最终返回，head 用于遍历
            first = first.next
        else:
            ans = head = list2
            second = second.next
        # 逐个比较两个链表的当前节点，连接较小的那个
        while head:
            if first is None:
                # first 已用完，将 second 剩余部分直接接上
                head.next = second
                break
            if second is None:
                # second 已用完，将 first 剩余部分直接接上
                head.next = first
                break
            # 比较当前节点值，连接较小的那个
            if first.val <= second.val:
                head.next = first
                first = first.next
            else:
                head.next = second
                second = second.next
            head = head.next  # 结果链表指针后移
        return ans
# @lc code=end



#
# @lcpr case=start
# [[1,4,5],[1,3,4],[2,6]]\n
# @lcpr case=end

# @lcpr case=start
# []\n
# @lcpr case=end

# @lcpr case=start
# [[]]\n
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
    import sys

    def _run_tests(cases):
        passed = 0
        for desc, func, expected in cases:
            try:
                got = func()
            except Exception as e:
                got = f"ERROR: {e}"
            ok = got == expected
            passed += ok
            print(f"  [{'PASS' if ok else 'FAIL'}] {desc}")
            if not ok:
                print(f"         Expected : {expected}")
                print(f"         Got      : {got}")
        print(f"\n  {passed}/{len(cases)} passed")
        sys.exit(0 if passed == len(cases) else 1)

    sol = Solution()

    def _mergek(arrs):
        return _to_list(sol.mergeKLists([_to_node(a) for a in arrs]))

    _run_tests([
        ("[[1,4,5],[1,3,4],[2,6]]", lambda: _mergek([[1,4,5],[1,3,4],[2,6]]),
                                     [1,1,2,3,4,4,5,6]),
        ("[] -> []",                 lambda: _mergek([]),    []),
        ("[[]] -> []",               lambda: _mergek([[]]),  []),
        ("单链表(已升序)",            lambda: _mergek([[1,2,3]]), [1,2,3]),
        ("两链表",                    lambda: _mergek([[1,3],[2,4]]), [1,2,3,4]),
    ])
