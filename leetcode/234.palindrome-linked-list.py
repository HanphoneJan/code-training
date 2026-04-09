#
# @lc app=leetcode.cn id=234 lang=python3
# @lcpr version=30204
#
# [234] 回文链表
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
    回文链表 - 快慢指针 + 反转链表

    问题描述：
    给你一个单链表的头节点 head，请你判断该链表是否为回文链表。
    如果是，返回 true；否则，返回 false。

    核心思路：
    1. 找到链表的中间节点（快慢指针）
    2. 反转后半部分链表
    3. 比较前半部分和反转后的后半部分
    4. （可选）恢复链表

    为什么这样有效？
    回文的特点是正读反读相同。将后半部分反转后，与前半部分一一比较即可。

    时间复杂度：O(n) - 遍历链表三次（找中点、反转、比较）
    空间复杂度：O(1) - 只使用几个指针
    """

    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        """
        判断链表是否为回文链表
        """
        # 一眼双指针
        # 能不能修改原链表？尽量不要，但面试时可以询问
        # 经典题目

        if not head or not head.next:
            return True

        # 步骤 1：找到中间节点（876. 链表的中间结点）
        mid = self.middleNode(head)

        # 步骤 2：反转后半部分（206. 反转链表）
        head2 = self.reverseList(mid)

        # 保存反转后的头节点，用于恢复链表
        h2 = head2

        # 步骤 3：比较前半部分和后半部分
        result = True
        while head2:
            if head.val != head2.val:
                result = False  # 不是回文链表
                break
            head = head.next
            head2 = head2.next

        # 步骤 4：恢复链表（可选，但推荐）
        self.reverseList(h2)

        return result

    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        """
        876. 链表的中间结点

        快慢指针：快指针每次走两步，慢指针每次走一步
        当快指针到达末尾时，慢指针到达中间

        对于偶数长度链表，返回后半部分的第一个节点
        """
        slow = fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        return slow

    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        """
        206. 反转链表

        使用三指针法：pre、cur、nxt
        """
        pre, cur = None, head
        while cur:
            nxt = cur.next
            cur.next = pre
            pre = cur
            cur = nxt
        return pre


# @lc code=end



#
# @lcpr case=start
# [1,2,2,1]\n
# @lcpr case=end

# @lcpr case=start
# [1,2]\n
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

    # 测试用例 1：偶数长度回文
    head1 = create_linked_list([1, 2, 2, 1])
    result1 = sol.isPalindrome(head1)
    print(f"Test 1: isPalindrome([1,2,2,1]) = {result1}")
    assert result1 == True, f"Expected True, got {result1}"

    # 测试用例 2：非回文
    head2 = create_linked_list([1, 2])
    result2 = sol.isPalindrome(head2)
    print(f"Test 2: isPalindrome([1,2]) = {result2}")
    assert result2 == False, f"Expected False, got {result2}"

    # 测试用例 3：奇数长度回文
    head3 = create_linked_list([1, 2, 3, 2, 1])
    result3 = sol.isPalindrome(head3)
    print(f"Test 3: isPalindrome([1,2,3,2,1]) = {result3}")
    assert result3 == True, f"Expected True, got {result3}"

    # 测试用例 4：单节点
    head4 = create_linked_list([1])
    result4 = sol.isPalindrome(head4)
    print(f"Test 4: isPalindrome([1]) = {result4}")
    assert result4 == True, f"Expected True, got {result4}"

    # 测试用例 5：空链表
    head5 = create_linked_list([])
    result5 = sol.isPalindrome(head5)
    print(f"Test 5: isPalindrome([]) = {result5}")
    assert result5 == True, f"Expected True, got {result5}"

    # 测试用例 6：长回文
    head6 = create_linked_list([1, 2, 3, 4, 5, 4, 3, 2, 1])
    result6 = sol.isPalindrome(head6)
    print(f"Test 6: isPalindrome([1,2,3,4,5,4,3,2,1]) = {result6}")
    assert result6 == True, f"Expected True, got {result6}"

    print("\nAll tests passed!")
