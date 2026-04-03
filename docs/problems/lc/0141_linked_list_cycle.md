---
title: 环形链表
platform: LeetCode
difficulty: 简单
id: 141
url: https://leetcode.cn/problems/linked-list-cycle/
tags:
  - 链表
  - 双指针
  - 哈希表
topics:
  - ../../topics/linked_list.md
  - ../../topics/two_pointers.md
patterns:
  - ../../patterns/floyd_cycle_detection.md
date_added: 2026-04-03
date_reviewed: []
---

# 0141. 环形链表

## 题目描述

给你一个链表的头节点 `head`，判断链表中是否有环。

如果链表中有某个节点，可以通过连续跟踪 `next` 指针再次到达，则链表中存在环。为了表示给定链表中的环，评测系统内部使用整数 `pos` 来表示链表尾连接到链表中的位置（索引从 0 开始）。注意：`pos` 不作为参数进行传递。仅仅是为了标识链表的实际情况。

如果链表中存在环，则返回 `true` 。否则，返回 `false` 。

## 示例

**示例 1：**
```
输入：head = [3,2,0,-4], pos = 1
输出：true
解释：链表中有一个环，其尾部连接到第二个节点。
```

**示例 2：**
```
输入：head = [1,2], pos = 0
输出：true
解释：链表中有一个环，其尾部连接到第一个节点。
```

**示例 3：**
```
输入：head = [1], pos = -1
输出：false
解释：链表中没有环。
```

---

## 解题思路

### 第一步：理解问题

判断一个链表是否有环，最直接的思路是记录访问过的节点，如果再次访问到就说明有环。

### 第二步：暴力解法 - 哈希表

遍历链表，把每个节点存入集合，如果发现节点已经在集合中，说明有环。

```python
def hasCycle(head):
    visited = set()
    while head:
        if head in visited:
            return True
        visited.add(head)
        head = head.next
    return False
```

- 时间复杂度：`O(n)`
- 空间复杂度：`O(n)`

### 第三步：最优解法 - 快慢指针

Floyd 判圈算法的核心思想：
- 慢指针 `slow` 每次走 1 步
- 快指针 `fast` 每次走 2 步

如果链表有环，快指针最终会追上慢指针（在环内相遇）。如果没有环，快指针会先到达末尾。

为什么一定能追上？
- 假设环的长度为 `L`，当慢指针进入环时，快指针已经在环内某处。
- 快指针相对于慢指针的速度是 1 步/轮，两者距离最多 `L-1`，所以最多 `L-1` 轮后一定会相遇。

- 时间复杂度：`O(n)`
- 空间复杂度：`O(1)`

---

## 完整代码实现

```python
from typing import Optional

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    """
    141. 环形链表 - 快慢指针（Floyd 判圈算法）

    核心思想：
    快指针每次走 2 步，慢指针每次走 1 步。如果链表有环，两者一定会在环内相遇。

    时间复杂度：O(n)
    空间复杂度：O(1)
    """

    def hasCycle(self, head: Optional[ListNode]) -> bool:
        slow, fast = head, head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                return True

        return False
```

---

## 示例推演

以 `head = [3, 2, 0, -4]`（pos = 1，即尾节点连到索引 1）为例：

链表结构：`3 -> 2 -> 0 -> -4 -> 2（循环）`

| 轮次 | slow | fast |
|------|------|------|
| 起始 | 3 | 3 |
| 1 | 2 | 0 |
| 2 | 0 | 2 |
| 3 | -4 | -4 |

第 3 轮时，`slow == fast`，都有环，返回 `True`。

---

## 复杂度分析

| 解法 | 时间复杂度 | 空间复杂度 | 说明 |
|------|-----------|-----------|------|
| 哈希表 | O(n) | O(n) | 直观易懂 |
| 快慢指针 | O(n) | O(1) | **最优解** |

---

## 易错点总结

### 1. 循环条件

必须是 `while fast and fast.next`，如果写 `while fast.next` 会在空链表时报错。

### 2. 比较对象

比较的是节点对象引用（地址），不是节点的值。因为值可能重复，但引用唯一。

### 3. 为什么 fast 走 2 步？

如果 fast 只走 1 步，那快慢指针永远保持初始距离（除非 head 就是环入口），无法判断。走 2 步才能保证在有环情况下追上。

---

## 扩展思考

### 如果要求找到环的入口？

就是 [142. 环形链表 II](https://leetcode.cn/problems/linked-list-cycle-ii/)，需要快慢指针相遇后，再用一个指针从 head 出发同步走。

## 相关题目

- [142. 环形链表 II](https://leetcode.cn/problems/linked-list-cycle-ii/)
- [287. 寻找重复数](https://leetcode.cn/problems/find-the-duplicate-number/)
