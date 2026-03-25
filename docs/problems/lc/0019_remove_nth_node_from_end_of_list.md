---
title: 删除链表的倒数第 N 个结点
platform: LeetCode
difficulty: Medium
id: 19
url: https://leetcode.cn/problems/remove-nth-node-from-end-of-list/
tags:
  - 链表
  - 双指针
date_added: 2026-03-25
---

# 19. 删除链表的倒数第 N 个结点

## 题目描述

给你一个链表，删除链表的倒数第 `n` 个结点，并且返回链表的头结点。

## 示例

**示例 1：**
```
输入：head = [1,2,3,4,5], n = 2
输出：[1,2,3,5]
```

**示例 2：**
```
输入：head = [1], n = 1
输出：[]
```

**示例 3：**
```
输入：head = [1,2], n = 1
输出：[1]
```

---

## 解题思路

### 第一步：理解问题本质

问题的核心是：**如何快速找到倒数第 n 个节点？**

如果知道链表长度 L，那么倒数第 n 个节点就是正数第 (L - n + 1) 个节点。但这需要遍历两次链表。

### 第二步：暴力解法

**思路**：先遍历一遍计算链表长度，再遍历到目标位置删除。

```python
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        # 计算链表长度
        length = 0
        cur = head
        while cur:
            length += 1
            cur = cur.next

        # 找到要删除节点的前一个位置
        dummy = ListNode(0, head)
        cur = dummy
        for i in range(length - n):
            cur = cur.next

        # 删除节点
        cur.next = cur.next.next
        return dummy.next
```

**缺点**：需要遍历两次链表。

### 第三步：最优解法 —— 双指针（快慢指针）

**核心洞察**：
- 让快指针先走 n 步，此时快指针和慢指针之间相隔 n 个节点
- 然后快慢指针同时走，当快指针到达链表末尾时，慢指针正好在倒数第 n+1 个位置
- 使用 dummy 节点统一处理删除头节点的情况

**为什么正确**：
- 假设链表长度为 L，快指针先走 n 步后，还剩 L-n 步到末尾
- 快慢指针一起走 L-n 步后，快指针到达末尾（走了 n + L-n = L 步）
- 慢指针从 dummy 开始走了 L-n 步，到达第 L-n 个节点，即倒数第 n+1 个节点

---

## 完整代码实现

```python
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

from typing import Optional

class Solution:
    """
    删除链表的倒数第 N 个结点 - 双指针（快慢指针）

    核心思想：
    使用两个指针，让快指针先走 n 步，然后快慢指针一起走。
    当快指针到达末尾时，慢指针正好在倒数第 n+1 个位置（即要删除节点的前一个）。

    为什么用 dummy 节点？
    如果删除的是头节点，需要特殊处理。使用 dummy 节点可以统一逻辑，
    让 slow 最终停在要删除节点的前一个位置。

    时间复杂度：O(L)，L 是链表长度，只遍历一次
    空间复杂度：O(1)
    """

    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        # 创建 dummy 节点，简化边界处理
        dummy = ListNode(0, head)

        # first 先走 n 步
        first = head
        for i in range(n):
            first = first.next

        # second 从 dummy 开始，最终停在要删除节点的前一个
        second = dummy

        # first 和 second 同时走，直到 first 到达末尾
        while first:
            first = first.next
            second = second.next

        # 删除倒数第 n 个节点
        second.next = second.next.next

        return dummy.next
```

---

## 示例推演

以 `head = [1,2,3,4,5], n = 2` 为例：

**初始状态**：
```
dummy -> 1 -> 2 -> 3 -> 4 -> 5
first指向1，second指向dummy
```

**Step 1**：first 先走 2 步
```
dummy -> 1 -> 2 -> 3 -> 4 -> 5
         ^        ^
       first    (first走了2步，现在指向3)
```

**Step 2**：first 和 second 同时走
| 步骤 | first | second | 说明 |
|------|-------|--------|------|
| 初始 | 3 | dummy | - |
| 1 | 4 | 1 | 同时前进一步 |
| 2 | 5 | 2 | 同时前进一步 |
| 3 | None | 3 | first到达末尾，second指向3 |

**Step 3**：删除 second.next（节点 4）
```
dummy -> 1 -> 2 -> 3 -> 5
```

返回 `dummy.next`，即 `[1,2,3,5]`

---

## 复杂度分析

| 解法 | 时间复杂度 | 空间复杂度 | 说明 |
|------|-----------|-----------|------|
| 暴力 | O(L) | O(1) | 需要遍历两次链表 |
| **双指针（最优）** | **O(L)** | **O(1)** | 只需遍历一次链表 |

---

## 易错点总结

### 1. 必须使用 dummy 节点

如果不使用 dummy 节点，当需要删除头节点时（如 `head = [1], n = 1`），需要特殊处理。

```python
# 不使用 dummy 的错误处理
def removeNthFromEnd(self, head, n):
    # ... 双指针逻辑 ...
    # 当 n = 链表长度时，second 会停在 head 前面
    # 但 head 前面没有节点，无法删除！
```

### 2. 快指针先走 n 步，不是 n+1 步

快指针先走 n 步，这样当 fast 到达末尾时，slow 正好在倒数第 n+1 个位置（要删除节点的前一个）。

### 3. 删除操作是 `second.next = second.next.next`

不是 `second = second.next`，那样只是移动了指针，没有真正删除节点。

---

## 扩展思考

### 1. 如何找到链表的中间节点？

同样使用快慢指针，快指针每次走 2 步，慢指针每次走 1 步，当快指针到达末尾时，慢指针就在中间。

### 2. 如何检测链表是否有环？

快慢指针，快指针每次走 2 步，慢指针每次走 1 步，如果相遇则有环。

### 3. 如果要求删除倒数第 n 个节点并返回被删除的值？

在删除前保存 `second.next.val`，然后再删除。

---

## 相关题目

- [876. 链表的中间结点](https://leetcode.cn/problems/middle-of-the-linked-list/)
- [141. 环形链表](https://leetcode.cn/problems/linked-list-cycle/)
- [142. 环形链表 II](https://leetcode.cn/problems/linked-list-cycle-ii/)
- [21. 合并两个有序链表](https://leetcode.cn/problems/merge-two-sorted-lists/)
