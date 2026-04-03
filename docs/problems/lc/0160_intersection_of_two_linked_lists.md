---
title: 相交链表
platform: LeetCode
difficulty: 简单
id: 160
url: https://leetcode.cn/problems/intersection-of-two-linked-lists/
tags:
  - 链表
  - 双指针
  - 哈希表
topics:
  - ../../topics/linked_list.md
  - ../../topics/two_pointers.md
patterns:
  - ../../patterns/linked_list.md
date_added: 2026-04-03
date_reviewed: []
---

# 0160. 相交链表

## 题目描述

给你两个单链表的头节点 `headA` 和 `headB`，请你找出并返回两个单链表相交的起始节点。如果两个链表不存在相交节点，返回 `null`。

图示两个链表在节点 `c1` 开始相交：

题目数据 **保证** 整个链式结构中不存在环。

**注意**，函数返回结果后，链表必须 **保持其原始结构** 。

## 示例

**示例 1：**
```
相交节点的值为 8
```

**示例 2：**
```
相交节点的值为 2
```

**示例 3：**
```
没有相交节点
```

---

## 解题思路

### 第一步：理解相交的含义

两个链表相交，意味着从某个节点开始，它们共用同一个后缀。不是值相等，而是**节点引用相同**。

### 第二步：暴力解法

对于 A 中的每个节点，遍历 B 看是否有相同节点。时间复杂度 `O(m * n)`。

### 第三步：哈希表解法

把 A 的所有节点存入集合，然后遍历 B，第一个在集合中的节点就是交点。时间复杂度 `O(m + n)`，空间复杂度 `O(m)`。

### 第四步：最优解法 - 双指针浪漫相遇

让两个指针 `p` 和 `q` 同时分别从 `headA` 和 `headB` 出发，走到末尾后跳到另一条链表的头。

走过的路径：
- p：`a + c + b`
- q：`b + c + a`

其中 `a, b` 是两条链表的非公共部分长度，`c` 是公共部分长度。

两人走的总步数相等，必在交点相遇。如果没有交点，会同时到达 `None`。

时间复杂度：`O(m + n)`，空间复杂度：`O(1)`。

---

## 完整代码实现

```python
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    """
    160. 相交链表 - 双指针法

    核心思想：
    两个指针分别遍历两条链表，走到末尾后跳到另一条链表的头。
    走过的总路程都是 a + b + c，必在交点相遇。

    时间复杂度：O(a + b)
    空间复杂度：O(1)
    """

    def getIntersectionNode(self, headA: ListNode, headB: ListNode):
        p, q = headA, headB
        while p is not q:
            p = p.next if p else headB
            q = q.next if q else headA
        return p
```

---

## 示例推演

设链表 A：`4 -> 1 -> 8 -> 4 -> 5`（a = 2，c = 3）
设链表 B：`5 -> 6 -> 1 -> 8 -> 4 -> 5`（b = 3，c = 3）

**p 的路径**：4 -> 1 -> **8** -> 4 -> 5 -> (None) -> 5 -> 6 -> 1 -> **8**
**q 的路径**：5 -> 6 -> 1 -> **8** -> 4 -> 5 -> (None) -> 4 -> 1 -> **8**

两者都在走了 8 步后在节点 **8** 相遇。

**无交点时**：
p 走 `a + b` 步后变为 None
q 走 `b + a` 步后也变为 None
同时到达 None，返回 None

---

## 复杂度分析

| 解法 | 时间复杂度 | 空间复杂度 | 说明 |
|------|-----------|-----------|------|
| 暴力 | O(m * n) | O(1) | 双重遍历 |
| 哈希表 | O(m + n) | O(m) | 空间换时间 |
| 双指针 | O(m + n) | O(1) | **最优解** |

---

## 易错点总结

### 1. 比较的是节点引用，不是值

链表相交的定义是节点引用相同，即使两个节点的值一样，如果不是同一个节点也不算相交。

### 2. 跳到另一条链表头部

`p = p.next if p else headB`，不是 headA！这样走的是 `a + c + b`。

### 3. 无交点时也正确

最终会同时变为 `None`，不会死循环。

---

## 扩展思考

### 如果链表有环怎么办？

需要先判断是否有环，以及环的位置，情况会更复杂。

### 如何只遍历一次就求出交点？

双指针法本质上已经是单次遍历的最优解法了。

## 相关题目

- [141. 环形链表](https://leetcode.cn/problems/linked-list-cycle/)
- [142. 环形链表 II](https://leetcode.cn/problems/linked-list-cycle-ii/)
- [19. 删除链表的倒数第 N 个结点](https://leetcode.cn/problems/remove-nth-node-from-end-of-list/)
