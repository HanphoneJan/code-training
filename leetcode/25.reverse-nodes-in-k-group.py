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

    def _revk(arr, k):
        return _to_list(sol.reverseKGroup(_to_node(arr), k))

    _run_tests([
        ("[1,2,3,4,5],k=2", lambda: _revk([1,2,3,4,5],2), [2,1,4,3,5]),
        ("[1,2,3,4,5],k=3", lambda: _revk([1,2,3,4,5],3), [3,2,1,4,5]),
        ("[1,2],k=1",       lambda: _revk([1,2],1),        [1,2]),
        ("[1],k=1",         lambda: _revk([1],1),           [1]),
    ])
