---
title: 环形链表 II
platform: LeetCode
difficulty: 中等
id: 142
url: https://leetcode.cn/problems/linked-list-cycle-ii/
tags:
  - 链表
  - 双指针
  - 数学
topics:
  - ../../topics/linked_list.md
  - ../../topics/two_pointers.md
  - ../../topics/math.md
patterns:
  - ../../patterns/floyd_cycle_detection.md
date_added: 2026-04-03
date_reviewed: []
---

# 0142. 环形链表 II

## 题目描述

给定一个链表的头节点 `head`，返回链表开始入环的第一个节点。如果链表无环，则返回 `null`。

如果链表中有某个节点，可以通过连续跟踪 `next` 指针再次到达，则链表中存在环。为了表示给定链表中的环，评测系统内部使用整数 `pos` 来表示链表尾连接到链表中的位置（索引从 0 开始）。如果 `pos` 是 `-1`，则在该链表中没有环。注意：`pos` 不作为参数进行传递，仅仅是为了标识链表的实际情况。

**不允许修改** 链表。

## 示例

**示例 1：**
```
输入：head = [3,2,0,-4], pos = 1
输出：指数为 1 的节点
解释：链表中有一个环，其尾部连接到第二个节点。
```

**示例 2：**
```
输入：head = [1,2], pos = 0
输出：指数为 0 的节点
解释：链表中有一个环，其尾部连接到第一个节点。
```

**示例 3：**
```
输入：head = [1], pos = -1
输出：no cycle
解释：链表中没有环。
```

---

## 解题思路

### 第一步：找环的入口

这道题比 141 更进一步：不仅判断是否有环，还要找到环的入口节点。

### 第二步：哈希表解法

遍历链表，把节点存入集合，第一个重复出现的节点就是环入口。

- 时间复杂度：`O(n)`
- 空间复杂度：`O(n)`

### 第三步：最优解法 - Floyd 判圈算法

分为两步：
1. **判断是否有环**：快慢指针找到相遇点
2. **找环入口**：从相遇点开始，一个指针从 head 出发，另一个从相遇点出发，都以速度 1 前进，再次相遇点就是环入口

**数学证明**：
设 head 到环入口距离为 `a`，环入口到相遇点距离为 `b`，相遇点到环入口距离为 `c`。
- 慢指针走的距离：`a + b`
- 快指针走的距离：`a + b + n(b + c) = 2(a + b)`
- 化简得：`a = c + (n-1)(b + c)`

这意味着：从 head 走 `a` 步，和从相遇点走 `c` 步（再走 `n-1` 整圈），会同时到达环入口。

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
    142. 环形链表 II - Floyd 判圈算法

    核心思想：
    1. 快慢指针找到相遇点
    2. 再用两个指针分别从 head 和相遇点同步前进，相遇点即环入口

    时间复杂度：O(n)
    空间复杂度：O(1)
    """

    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        slow = fast = head

        # 步骤1：找相遇点
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if fast is slow:  # 相遇
                # 步骤2：找环入口
                while slow is not head:
                    slow = slow.next
                    head = head.next
                return slow

        return None
```

---

## 示例推演

以 `head = [3, 2, 0, -4]`（pos = 1）为例：

链表结构：`3 -> 2 -> 0 -> -4 -> 2（循环）`

**步骤1 - 找相遇点**：
- slow：3 -> 2 -> 0 -> -4
- fast：3 -> 0 -> -4 -> 0 -> -4（实际上更快到达）

实际上：
- 起始：slow=3, fast=3
- 第1轮：slow=2, fast=0
- 第2轮：slow=0, fast=2（fast 从 0 走两步：-> -4 -> 2）
- 第3轮：slow=-4, fast=-4

在节点 `-4` 相遇。

**步骤2 - 找入口**：
- `a = 1`（head 到入口 "2" 的距离是 1 步）
- 从 head 出发：3 -> **2**（1步）
- 从相遇点 -4 出发：-4 -> 2（`c = 1` 步）

两者在节点 **2** 相遇，即环入口。

---

## 复杂度分析

| 解法 | 时间复杂度 | 空间复杂度 | 说明 |
|------|-----------|-----------|------|
| 哈希表 | O(n) | O(n) | 直观但占用空间 |
| Floyd | O(n) | O(1) | **最优解** |

---

## 易错点总结

### 1. 比较用 `is` 而非 `==`

判断相遇时应该用 `fast is slow`，虽然在 Python 中对于同一对象两者等价，但语义上 `is` 更明确是在比较引用。

### 2. 无环时的处理

如果 fast 能走到末尾（fast 为 None 或 fast.next 为 None），说明无环，返回 None。

### 3. 为什么走 a 步就相遇？

数学等式 `a = c + (n-1)(b+c)` 是关键。这意味着从 head 出发的指针走 `a` 步到达入口时，从相遇点出发的指针刚好走完了 `c` 步加若干整圈，也正好到达入口。

---

## 扩展思考

### 如果要求环的长度？

找到相遇点后，让其中一个指针继续走一圈，统计步数即可。

### 和 141 题的关系

141 只要求判断是否有环，142 要求找到入口。 Floyd 算法是链表环问题的通用解法。

## 相关题目

- [141. 环形链表](https://leetcode.cn/problems/linked-list-cycle/)
- [287. 寻找重复数](https://leetcode.cn/problems/find-the-duplicate-number/)
