---
title: 回文链表
platform: LeetCode
difficulty: Easy
id: 234
url: https://leetcode.cn/problems/palindrome-linked-list/
tags:
  - 栈
  - 递归
  - 链表
  - 双指针
topics:
  - ../../topics/linked-list.md
  - ../../topics/two-pointers.md
patterns:
  - ../../patterns/slow-fast-pointer.md
date_added: 2026-04-09
date_reviewed: []
---

# 234. 回文链表

## 题目描述

给你一个单链表的头节点 `head`，请你判断该链表是否为回文链表。如果是，返回 `true`；否则，返回 `false`。

## 示例

**示例 1：**
```
输入: head = [1,2,2,1]
输出: true
```

**示例 2：**
```
输入: head = [1,2]
输出: false
```

---

## 解题思路

### 第一步：理解问题本质

回文的特点是**正读反读相同**。对于链表，无法像数组那样直接随机访问，需要特殊处理。

### 第二步：暴力解法 - 转数组

遍历链表，将值存入数组，然后用双指针判断数组是否回文。

```python
def isPalindrome(self, head: Optional[ListNode]) -> bool:
    values = []
    while head:
        values.append(head.val)
        head = head.next

    left, right = 0, len(values) - 1
    while left < right:
        if values[left] != values[right]:
            return False
        left += 1
        right -= 1
    return True
```

**为什么不够好**：需要 O(n) 额外空间。

### 第三步：优化解法 - 递归

利用递归栈隐式地存储后半部分，与前半部分比较。

```python
def isPalindrome(self, head: Optional[ListNode]) -> bool:
    self.front = head

    def check(node):
        if not node:
            return True
        if not check(node.next):
            return False
        if self.front.val != node.val:
            return False
        self.front = self.front.next
        return True

    return check(head)
```

**分析**：时间 O(n)，空间 O(n)（递归栈）。

### 第四步：最优解法 - 快慢指针 + 反转链表

1. 找到链表中间节点（快慢指针）
2. 反转后半部分链表
3. 比较前半部分和反转后的后半部分
4. （可选）恢复链表

---

## 完整代码实现

```python
from typing import Optional

class Solution:
    """
    回文链表 - 快慢指针 + 反转链表

    核心思路：
    1. 找到链表的中间节点（快慢指针）
    2. 反转后半部分链表
    3. 比较前半部分和反转后的后半部分

    时间复杂度：O(n)
    空间复杂度：O(1)
    """

    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        if not head or not head.next:
            return True

        # 步骤 1：找到中间节点
        mid = self.middleNode(head)

        # 步骤 2：反转后半部分
        head2 = self.reverseList(mid)
        h2 = head2  # 保存用于恢复

        # 步骤 3：比较
        result = True
        while head2:
            if head.val != head2.val:
                result = False
                break
            head = head.next
            head2 = head2.next

        # 步骤 4：恢复链表
        self.reverseList(h2)

        return result

    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        """快慢指针找中间节点"""
        slow = fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        return slow

    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        """反转链表"""
        pre, cur = None, head
        while cur:
            nxt = cur.next
            cur.next = pre
            pre = cur
            cur = nxt
        return pre
```

---

## 示例推演

以 `[1,2,2,1]` 为例：

**步骤 1：找中间节点**
```
初始: slow=1, fast=1
第1轮: slow=2, fast=2
第2轮: slow=2(第二个), fast=None
中间节点: 第二个 2
```

**步骤 2：反转后半部分**
```
原链表: 1 -> 2 -> 2 -> 1 -> None
后半部分反转: 1 -> 2 -> None
```

**步骤 3：比较**
```
前半部分: 1 -> 2 -> None
后半部分: 1 -> 2 -> None

1 == 1 ✓
2 == 2 ✓
```

结果：True

---

## 复杂度分析

| 解法 | 时间复杂度 | 空间复杂度 | 说明 |
|------|-----------|-----------|------|
| 转数组 | O(n) | O(n) | 需要额外数组 |
| 递归 | O(n) | O(n) | 递归栈空间 |
| 快慢指针+反转 | O(n) | O(1) | 最优解法 |

---

## 易错点总结

### 1. 中间节点找错

**偶数长度链表**：快慢指针返回后半部分的第一个节点。

```python
while fast and fast.next:
    slow = slow.next
    fast = fast.next.next
# 对于 [1,2,2,1]，slow 指向第二个 2
```

### 2. 忘记恢复链表

```python
# 比较完后恢复链表（面试时询问是否需要）
self.reverseList(h2)
```

### 3. 空链表处理

```python
if not head or not head.next:
    return True  # 空链表或单节点都是回文
```

---

## 扩展思考

### 1. 如果要求不能修改链表？

使用递归或转数组的方法。

### 2. 相关题目

- [234. 回文链表](https://leetcode.cn/problems/palindrome-linked-list/)
- [206. 反转链表](https://leetcode.cn/problems/reverse-linked-list/)
- [876. 链表的中间结点](https://leetcode.cn/problems/middle-of-the-linked-list/)

---

## 相关题目

- [206. 反转链表](https://leetcode.cn/problems/reverse-linked-list/)
- [876. 链表的中间结点](https://leetcode.cn/problems/middle-of-the-linked-list/)
- [143. 重排链表](https://leetcode.cn/problems/reorder-list/)
