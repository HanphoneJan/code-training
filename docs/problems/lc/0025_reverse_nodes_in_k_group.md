---
title: K 个一组翻转链表
platform: LeetCode
difficulty: 困难
id: 25
url: https://leetcode.cn/problems/reverse-nodes-in-k-group/
tags:
  - 链表
  - 递归
  - 迭代
topics:
  - ../../topics/linked_list.md
patterns:
  - ../../patterns/linked_list_reversal.md
date_added: 2026-03-23
date_reviewed: []
---

# 0025. K 个一组翻转链表

## 题目描述

给你链表的头节点 `head` ，每 `k` 个节点一组进行翻转，请你返回修改后的链表。

`k` 是一个正整数，它的值小于或等于链表的长度。如果节点总数不是 `k` 的整数倍，那么请将最后剩余的节点保持原有顺序。

你不能只是单纯的改变节点内部的值，而是需要实际进行节点交换。

## 示例

**示例 1：**
```
输入：head = [1,2,3,4,5], k = 2
输出：[2,1,4,3,5]
```

**示例 2：**
```
输入：head = [1,2,3,4,5], k = 3
输出：[3,2,1,4,5]
```

---

## 解题思路

### 第一步：理解问题本质

核心操作：**链表的局部翻转**

- 不是翻转整个链表，而是每 k 个节点为一组进行翻转
- 组与组之间需要正确连接
- 最后一组不足 k 个时不翻转

### 第二步：暴力解法思路

递归思路：
1. 先遍历 k 个节点，检查是否够 k 个
2. 翻转这 k 个节点
3. 递归处理后面的链表
4. 连接翻转后的尾部和递归结果

```python
def reverseKGroup(head, k):
    # 检查是否有 k 个节点
    curr = head
    for _ in range(k):
        if not curr:
            return head  # 不足 k 个，不翻转
        curr = curr.next

    # 翻转前 k 个节点
    prev, curr = None, head
    for _ in range(k):
        next_temp = curr.next
        curr.next = prev
        prev = curr
        curr = next_temp

    # head 现在是翻转后的尾部，连接递归结果
    head.next = reverseKGroup(curr, k)
    return prev  # 返回新的头部
```

### 第三步：迭代解法（更优）

递归解法虽然简洁，但对于很长的链表可能导致栈溢出。迭代解法更稳健：

**核心思想**：
- 用虚拟头节点简化边界处理
- 维护 `group_prev` 指向当前组的前一个节点
- 每次检查是否有 k 个节点，然后进行翻转

---

## 完整代码实现

```python
from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        """
        K个一组翻转链表 - 迭代解法

        核心思想：分段翻转，用虚拟头节点简化边界处理
        """
        if not head or k <= 1:
            return head

        # 创建虚拟头节点
        dummy = ListNode(0)
        dummy.next = head
        group_prev = dummy  # 当前组的前一个节点

        while True:
            # 检查是否还有k个节点
            ktail = group_prev
            for _ in range(k):
                ktail = ktail.next
                if not ktail:
                    return dummy.next  # 不足k个，直接返回

            # 记录下一组的起始节点
            group_next = ktail.next

            # 翻转当前组 [group_prev.next, ktail]
            prev = ktail.next  # 翻转后的尾部指向下一组的头
            curr = group_prev.next  # 当前组的第一个节点

            # 标准链表翻转
            while curr != group_next:
                next_temp = curr.next
                curr.next = prev
                prev = curr
                curr = next_temp

            # 更新连接
            temp = group_prev.next  # 原来的头（现在的尾）
            group_prev.next = ktail  # 连接到新的头
            group_prev = temp  # 移动到下一组的前一个位置
```

---

## 示例推演

**示例**：`head = [1,2,3,4,5], k = 2`

**初始化**：
- `dummy -> 1 -> 2 -> 3 -> 4 -> 5`
- `group_prev = dummy`

**第一组处理**（节点 1, 2）：
1. 检查：`ktail` 经过 2 步到达节点 2，存在
2. `group_next = 3`（下一组的头）
3. 翻转 1->2：变成 `2 -> 1 -> 3`
4. 更新连接：`dummy -> 2`，`1 -> 3`
5. `group_prev` 移动到节点 1

**第二组处理**（节点 3, 4）：
1. 检查：`ktail` 经过 2 步到达节点 4，存在
2. `group_next = 5`（下一组的头）
3. 翻转 3->4：变成 `4 -> 3 -> 5`
4. 更新连接：`1 -> 4`，`3 -> 5`
5. `group_prev` 移动到节点 3

**第三组检查**（从节点 5 开始）：
- 检查是否有 2 个节点，只有节点 5，不足 k 个
- 直接返回 `dummy.next = [2,1,4,3,5]`

**结果**：`[2,1,4,3,5]`

---

## 复杂度分析

| 解法 | 时间复杂度 | 空间复杂度 | 说明 |
|------|-----------|-----------|------|
| 递归 | O(n) | O(n/k) - 递归栈 | 代码简洁，有栈溢出风险 |
| 迭代 | O(n) | O(1) | **推荐**，空间更优 |

---

## 易错点总结

### 1. 虚拟头节点的使用

```python
dummy = ListNode(0)
dummy.next = head
```
统一处理头节点翻转的情况，避免特殊判断。

### 2. 翻转边界处理

```python
prev = ktail.next  # 翻转后的尾部要连接到下一组
```
注意翻转后当前组的尾部（原来的头）要连接到 `group_next`。

### 3. 指针更新顺序

```python
temp = group_prev.next    # 先保存原来的头
group_prev.next = ktail   # 再更新连接
group_prev = temp         # 最后移动 group_prev
```
顺序很重要，先保存再更新。

### 4. 循环终止条件

```python
while True:
    # 检查是否还有k个节点
    for _ in range(k):
        ktail = ktail.next
        if not ktail:
            return dummy.next
```
当不足 k 个节点时立即返回，这是终止条件。

---

## 扩展思考

### 1. 如果要求保留不足 k 个的组也要翻转？

在返回前添加一段代码翻转剩余部分即可。

### 2. 链表翻转的通用模板

```python
prev, curr = None, head
while curr:
    next_temp = curr.next
    curr.next = prev
    prev = curr
    curr = next_temp
return prev  # 新的头节点
```

### 3. 如何反转从位置 m 到 n 的链表？

类似的思想：找到 m 的前一个节点，翻转 m 到 n 的部分，再连接。

---

## 相关题目

- [206. 反转链表](https://leetcode.cn/problems/reverse-linked-list/)
- [92. 反转链表 II](https://leetcode.cn/problems/reverse-linked-list-ii/)
- [24. 两两交换链表中的节点](https://leetcode.cn/problems/swap-nodes-in-pairs/)
