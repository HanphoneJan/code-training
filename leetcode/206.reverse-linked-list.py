#
# @lc app=leetcode.cn id=206 lang=python3
# @lcpr version=30204
#
# [206] 反转链表
#

# @lcpr-template-start
from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def __repr__(self):
        """用于打印链表"""
        result = []
        cur = self
        while cur:
            result.append(str(cur.val))
            cur = cur.next
        return " -> ".join(result) + " -> None"
# @lcpr-template-end
# @lc code=start
class Solution:
    """
    反转链表 - 迭代法

    问题描述：
    给你单链表的头节点 head，请你反转链表，并返回反转后的链表。

    核心思路：
    使用三个指针：pre（前一个节点）、cur（当前节点）、nxt（下一个节点）
    遍历链表，每次将 cur.next 指向 pre，实现局部反转

    指针移动顺序：
    1. 保存 cur.next 到 nxt（防止断链）
    2. 将 cur.next 指向 pre（反转）
    3. pre 移动到 cur
    4. cur 移动到 nxt

    为什么用 pre 而不是 next？
    - 反转后，当前节点需要指向前一个节点
    - 所以需要保存前一个节点的引用

    时间复杂度：O(n) - 遍历一次链表
    空间复杂度：O(1) - 只使用三个指针
    """

    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        """
        反转单链表
        """
        # 链表的经典操作
        # 空链表或只有一个节点，直接返回
        if head is None or head.next is None:
            return head

        # pre: 前一个节点（已反转部分的头节点）
        # cur: 当前处理的节点
        pre = None  # 初始时，已反转部分为空
        cur = head

        while cur:
            # 保存下一个节点，防止断链后找不到
            nxt = cur.next

            # 反转：将当前节点的 next 指向前一个节点
            cur.next = pre

            # 移动指针：pre 和 cur 都向前移动一步
            pre = cur      # pre 移动到当前节点
            cur = nxt      # cur 移动到下一个待处理节点

        # 循环结束时，pre 指向新的头节点（原尾节点）
        return pre

    def reverseListRecursive(self, head: Optional[ListNode]) -> Optional[ListNode]:
        """
        反转链表 - 递归法

        核心思路：
        递归到链表末尾，然后逐层返回时反转指针

        时间复杂度：O(n)
        空间复杂度：O(n) - 递归栈空间
        """
        # 递归终止条件
        if not head or not head.next:
            return head

        # 递归反转后续链表
        new_head = self.reverseListRecursive(head.next)

        # 反转当前节点与下一个节点的指针
        head.next.next = head
        head.next = None

        return new_head


# @lc code=end



#
# @lcpr case=start
# [1,2,3,4,5]\n
# @lcpr case=end

# @lcpr case=start
# [1,2]\n
# @lcpr case=end

# @lcpr case=start
# []\n
# @lcpr case=end

#

if __name__ == "__main__":
    sol = Solution()

    # 辅助函数：根据列表创建链表
    def create_linked_list(values):
        """根据值列表创建链表"""
        if not values:
            return None
        head = ListNode(values[0])
        cur = head
        for val in values[1:]:
            cur.next = ListNode(val)
            cur = cur.next
        return head

    # 辅助函数：将链表转换为列表（用于验证）
    def linked_list_to_list(head):
        """将链表转换为列表"""
        result = []
        cur = head
        while cur:
            result.append(cur.val)
            cur = cur.next
        return result

    # 测试用例 1：基本示例
    head1 = create_linked_list([1, 2, 3, 4, 5])
    print(f"Test 1 - Original: {linked_list_to_list(head1)}")
    reversed1 = sol.reverseList(head1)
    result1 = linked_list_to_list(reversed1)
    print(f"Test 1 - Reversed: {result1}")
    assert result1 == [5, 4, 3, 2, 1], f"Expected [5,4,3,2,1], got {result1}"

    # 测试用例 2：两个节点
    head2 = create_linked_list([1, 2])
    print(f"Test 2 - Original: {linked_list_to_list(head2)}")
    reversed2 = sol.reverseList(head2)
    result2 = linked_list_to_list(reversed2)
    print(f"Test 2 - Reversed: {result2}")
    assert result2 == [2, 1], f"Expected [2,1], got {result2}"

    # 测试用例 3：空链表
    head3 = create_linked_list([])
    reversed3 = sol.reverseList(head3)
    result3 = linked_list_to_list(reversed3)
    print(f"Test 3 - Empty list: {result3}")
    assert result3 == [], f"Expected [], got {result3}"

    # 测试用例 4：单个节点
    head4 = create_linked_list([1])
    print(f"Test 4 - Original: {linked_list_to_list(head4)}")
    reversed4 = sol.reverseList(head4)
    result4 = linked_list_to_list(reversed4)
    print(f"Test 4 - Reversed: {result4}")
    assert result4 == [1], f"Expected [1], got {result4}"

    # 测试用例 5：递归法测试
    head5 = create_linked_list([1, 2, 3, 4])
    print(f"Test 5 (Recursive) - Original: {linked_list_to_list(head5)}")
    reversed5 = sol.reverseListRecursive(head5)
    result5 = linked_list_to_list(reversed5)
    print(f"Test 5 (Recursive) - Reversed: {result5}")
    assert result5 == [4, 3, 2, 1], f"Expected [4,3,2,1], got {result5}"

    print("\nAll tests passed!")
