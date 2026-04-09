---
title: 反转链表
platform: LeetCode
difficulty: Easy
id: 206
url: https://leetcode.cn/problems/reverse-linked-list/
tags:
  - 链表
  - 递归
topics:
  - ../../topics/linked-list.md
patterns:
  - ../../patterns/two-pointers.md
date_added: 2026-04-09
date_reviewed: []
---

# 206. 反转链表

## 题目描述

给你单链表的头节点 `head`，请你反转链表，并返回反转后的链表。

## 示例

**示例 1：**
```
输入: head = [1,2,3,4,5]
输出: [5,4,3,2,1]
```

**示例 2：**
```
输入: head = [1,2]
输出: [2,1]
```

**示例 3：**
```
输入: head = []
输出: []
```

---

## 解题思路

### 第一步：理解问题本质

反转链表意味着：
- 原来的头节点变成尾节点
- 原来的尾节点变成头节点
- 每个节点的 next 指针指向前一个节点而不是后一个

### 第二步：暴力解法 - 使用栈

遍历链表，将所有节点值存入栈，然后创建新链表。

```python
def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
    stack = []
    cur = head
    while cur:
        stack.append(cur.val)
        cur = cur.next

    dummy = ListNode(0)
    cur = dummy
    while stack:
        cur.next = ListNode(stack.pop())
        cur = cur.next

    return dummy.next
```

**为什么不够好**：需要 O(n) 额外空间，且创建了新节点而非原地反转。

### 第三步：优化解法 - 递归

递归到链表末尾，返回时反转指针。

```python
def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
    if not head or not head.next:
        return head

    new_head = self.reverseList(head.next)
    head.next.next = head
    head.next = None

    return new_head
```

**分析**：时间 O(n)，空间 O(n)（递归栈）。

### 第四步：最优解法 - 迭代（三指针法）

使用三个指针：pre、cur、nxt，遍历链表时逐个反转指针方向。

---

## 完整代码实现

```python
from typing import Optional

class Solution:
    """
    反转链表 - 迭代法

    核心思路：
    使用三个指针：pre（前一个节点）、cur（当前节点）、nxt（下一个节点）
    遍历链表，每次将 cur.next 指向 pre，实现局部反转

    时间复杂度：O(n)
    空间复杂度：O(1)
    """

    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # pre: 前一个节点（已反转部分的头节点）
        # cur: 当前处理的节点
        pre = None
        cur = head

        while cur:
            # 保存下一个节点，防止断链后找不到
            nxt = cur.next

            # 反转：将当前节点的 next 指向前一个节点
            cur.next = pre

            # 移动指针
            pre = cur
            cur = nxt

        return pre
```

---

## 示例推演

以 `[1,2,3,4,5]` 为例：

**初始状态**：
```
pre: None
cur: 1 -> 2 -> 3 -> 4 -> 5 -> None
```

**第1轮**：
```
nxt = 2
cur.next = pre = None
pre = 1 -> None
cur = 2 -> 3 -> 4 -> 5 -> None
```

**第2轮**：
```
nxt = 3
cur.next = pre = 1 -> None
pre = 2 -> 1 -> None
cur = 3 -> 4 -> 5 -> None
```

**第3轮**：
```
nxt = 4
cur.next = pre = 2 -> 1 -> None
pre = 3 -> 2 -> 1 -> None
cur = 4 -> 5 -> None
```

**第4轮**：
```
nxt = 5
cur.next = pre = 3 -> 2 -> 1 -> None
pre = 4 -> 3 -> 2 -> 1 -> None
cur = 5 -> None
```

**第5轮**：
```
nxt = None
cur.next = pre = 4 -> 3 -> 2 -> 1 -> None
pre = 5 -> 4 -> 3 -> 2 -> 1 -> None
cur = None
```

**结束**：cur 为 None，返回 pre = `[5,4,3,2,1]`

---

## 复杂度分析

| 解法 | 时间复杂度 | 空间复杂度 | 说明 |
|------|-----------|-----------|------|
| 栈 | O(n) | O(n) | 需要额外栈空间 |
| 递归 | O(n) | O(n) | 递归栈空间 |
| 迭代（三指针） | O(n) | O(1) | 最优解法 |

---

## 易错点总结

### 1. 忘记保存 next 指针

**错误**：
```python
cur.next = pre   # 断链了！
cur = cur.next   # 错误！cur.next 已经是 pre 了
```

**正确**：
```python
nxt = cur.next   # 先保存
cur.next = pre   # 再反转
cur = nxt        # 移动到保存的 next
```

### 2. 返回错误的节点

**错误**：`return cur`（cur 最后是 None）

**正确**：`return pre`（pre 指向新的头节点）

### 3. 递归法忘记断开原指针

```python
head.next.next = head
head.next = None  # 必须断开，否则形成环
```

---

## 扩展思考

### 1. 反转指定区间的链表

[92. 反转链表 II](https://leetcode.cn/problems/reverse-linked-list-ii/)：反转从位置 m 到 n 的链表。

### 2. K 个一组反转链表

[25. K 个一组翻转链表](https://leetcode.cn/problems/reverse-nodes-in-k-group/)：每 k 个节点反转一次。

### 3. 相关题目

- [206. 反转链表](https://leetcode.cn/problems/reverse-linked-list/)
- [92. 反转链表 II](https://leetcode.cn/problems/reverse-linked-list-ii/)
- [25. K 个一组翻转链表](https://leetcode.cn/problems/reverse-nodes-in-k-group/)
- [234. 回文链表](https://leetcode.cn/problems/palindrome-linked-list/)（需要反转后半部分）

---

## 相关题目

- [92. 反转链表 II](https://leetcode.cn/problems/reverse-linked-list-ii/)
- [25. K 个一组翻转链表](https://leetcode.cn/problems/reverse-nodes-in-k-group/)
- [234. 回文链表](https://leetcode.cn/problems/palindrome-linked-list/)
