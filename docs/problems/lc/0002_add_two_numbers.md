---
title: 两数相加
platform: LeetCode
difficulty: Medium
id: 2
url: https://leetcode.cn/problems/add-two-numbers/
tags:
  - 链表
  - 递归
  - 数学
date_added: 2026-03-25
---

# 2. 两数相加

## 题目描述

给你两个非空的链表，表示两个非负的整数。它们每位数字都是按照逆序的方式存储的，并且每个节点只能存储一位数字。

请你将两个数相加，并以相同形式返回一个表示和的链表。

你可以假设除了数字 0 之外，这两个数都不会以 0 开头。

## 示例

**示例 1：**
```
输入：l1 = [2,4,3], l2 = [5,6,4]
输出：[7,0,8]
解释：342 + 465 = 807
```

**示例 2：**
```
输入：l1 = [0], l2 = [0]
输出：[0]
```

**示例 3：**
```
输入：l1 = [9,9,9,9,9,9,9], l2 = [9,9,9,9]
输出：[8,9,9,9,0,0,0,1]
```

---

## 解题思路

### 第一步：理解问题本质

这是一个模拟手工加法的过程：
1. 从个位（链表头部）开始逐位相加
2. 处理进位（和大于等于10的情况）
3. 如果最后还有进位，需要新增一个节点

### 第二步：暴力解法 —— 迭代

**思路**：用循环遍历两个链表，逐位相加，处理进位。

```python
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(0)  # 哑节点，简化头节点处理
        cur = dummy
        carry = 0  # 进位

        while l1 or l2 or carry:
            val1 = l1.val if l1 else 0
            val2 = l2.val if l2 else 0
            s = val1 + val2 + carry

            carry = s // 10
            cur.next = ListNode(s % 10)
            cur = cur.next

            if l1: l1 = l1.next
            if l2: l2 = l2.next

        return dummy.next
```

**优点**：直观易懂
**缺点**：需要额外的空间创建新节点

### 第三步：优化解法 —— 递归（原地修改）

**核心洞察**：
- 链表结构天然适合递归处理
- 可以直接修改 l1 的值，复用 l1 的节点，减少空间分配
- 当一个链表为空时，可以直接返回另一个链表（加上进位）

**算法步骤**：
1. 如果 l1 和 l2 都为空，返回进位节点（如果有）
2. 如果 l1 为空，交换 l1 和 l2（保证 l1 非空，简化代码）
3. 计算当前位的和：s = carry + l1.val + (l2.val if l2 else 0)
4. l1.val = s % 10，递归处理下一位，进位为 s // 10
5. 返回 l1

**为什么正确**：
- 每次递归处理当前位，并返回处理后的链表头部
- 由于链表是逆序存储的，递归深度与数字位数一致
- 通过修改 l1 的值，实现了原地修改，节省空间

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
    两数相加 - 链表模拟加法

    核心思想：
    模拟手工加法过程，从链表头（个位）开始逐位相加，处理进位。

    为什么选择递归？
    链表的结构天然适合递归处理，每次处理当前节点，递归处理后续节点。

    关键点：
    1. 进位 carry 的处理：s // 10 得到新的进位
    2. 边界情况：当一个链表为空时，与0相加
    3. 最终进位：如果最后还有进位，需要新增一个节点

    时间复杂度：O(max(m,n))，m和n是两个链表的长度
    空间复杂度：O(max(m,n))，递归栈的深度
    """

    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode], carry=0) -> Optional[ListNode]:
        if l1 is None and l2 is None:  # 递归边界
            return ListNode(carry) if carry else None  # 如果进位了，就额外创建一个节点
        if l1 is None:  # 如果 l1 是空的，那么此时 l2 一定不是空节点
            l1, l2 = l2, l1  # 交换 l1 与 l2，保证 l1 非空，从而简化代码
        s = carry + l1.val + (l2.val if l2 else 0)  # 节点值和进位加在一起
        l1.val = s % 10  # 每个节点保存一个数位（直接修改原链表）
        l1.next = self.addTwoNumbers(l1.next, l2.next if l2 else None, s // 10)  # 进位
        return l1
```

---

## 示例推演

以 `l1 = [2,4,3], l2 = [5,6,4]` 为例：

```
表示的数字：342 + 465 = 807
```

**递归调用过程**：

| 层级 | l1.val | l2.val | carry | s = carry+l1+l2 | l1.val = s%10 | 新carry | 说明 |
|------|--------|--------|-------|-----------------|---------------|---------|------|
| 1 | 2 | 5 | 0 | 7 | 7 | 0 | 个位相加 |
| 2 | 4 | 6 | 0 | 10 | 0 | 1 | 十位相加，有进位 |
| 3 | 3 | 4 | 1 | 8 | 8 | 0 | 百位相加 |
| 4 | None | None | 0 | 0 | - | 0 | 无进位，返回None |

**结果链表**：`[7,0,8]`

再以一个复杂例子 `l1 = [9,9,9], l2 = [9,9,9,9,9]` 为例：

| 层级 | l1.val | l2.val | carry | s | l1.val | 新carry |
|------|--------|--------|-------|---|--------|---------|
| 1 | 9 | 9 | 0 | 18 | 8 | 1 |
| 2 | 9 | 9 | 1 | 19 | 9 | 1 |
| 3 | 9 | 9 | 1 | 19 | 9 | 1 |
| 4 | None | 9 | 1 | 10 | 0 | 1 |
| 5 | None | 9 | 1 | 10 | 0 | 1 |
| 6 | None | None | 1 | 1 | 1 | 0 | 最终进位 |

**结果链表**：`[8,9,9,0,0,1]`

---

## 复杂度分析

| 解法 | 时间复杂度 | 空间复杂度 | 说明 |
|------|-----------|-----------|------|
| 迭代 | O(max(m,n)) | O(max(m,n)) | 需要创建新链表 |
| **递归（最优）** | **O(max(m,n))** | **O(max(m,n))** | 递归栈深度，原地修改 |

---

## 易错点总结

### 1. 进位的处理

进位是当前和除以10的商：`carry = s // 10`
当前位的值是和除以10的余数：`val = s % 10`

### 2. 递归边界条件

```python
if l1 is None and l2 is None:
    return ListNode(carry) if carry else None
```

如果最后还有进位，必须创建一个新节点！

### 3. 交换 l1 和 l2 的技巧

```python
if l1 is None:
    l1, l2 = l2, l1
```

这个技巧保证了 l1 永远非空，简化了后续代码。

---

## 扩展思考

### 1. 如果数字是正序存储的？

需要先反转链表，或者使用栈来逆序处理。

### 2. 如果链表很长，递归深度过深？

可以改用迭代版本，避免栈溢出。

### 3. 如何扩展为多个数相加？

可以用归并思想，两两相加，或者一次遍历所有链表。

---

## 相关题目

- [445. 两数相加 II](https://leetcode.cn/problems/add-two-numbers-ii/) - 数字正序存储
- [2. 两数相加](https://leetcode.cn/problems/add-two-numbers/)
- [415. 字符串相加](https://leetcode.cn/problems/add-strings/)
- [67. 二进制求和](https://leetcode.cn/problems/add-binary/)
