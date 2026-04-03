---
title: 排序链表
platform: LeetCode
difficulty: 中等
id: 148
url: https://leetcode.cn/problems/sort-list/
tags:
  - 链表
  - 双指针
  - 分治
  - 排序
  - 归并排序
topics:
  - ../../topics/linked_list.md
  - ../../topics/divide_and_conquer.md
  - ../../topics/sorting.md
patterns:
  - ../../patterns/merge_sort.md
date_added: 2026-04-03
date_reviewed: []
---

# 0148. 排序链表

## 题目描述

给你链表的头结点 `head` ，请将其按 **升序** 排列并返回 **排序后的链表** 。

**进阶：** 你可以在 `O(n log n)` 时间复杂度和常数级空间复杂度下，对链表进行排序吗？

## 示例

**示例 1：**
```
输入：head = [4,2,1,3]
输出：[1,2,3,4]
```

**示例 2：**
```
输入：head = [-1,5,3,4,0]
输出：[-1,0,3,4,5]
```

**示例 3：**
```
输入：head = []
输出：[]
```

---

## 解题思路

### 第一步：分析限制

- 时间复杂度要求 `O(n log n)`：排除冒泡、插入等 `O(n²)` 排序
- 空间复杂度要求 `O(1)`：排除递归的快速排序和归并排序

对于链表来说，**自底向上的归并排序**可以满足这两个要求。

### 第二步：暴力解法

把链表值存入数组，排序后再重建链表：

```python
def sortList(head):
    vals = []
    cur = head
    while cur:
        vals.append(cur.val)
        cur = cur.next
    vals.sort()
    dummy = ListNode()
    cur = dummy
    for v in vals:
        cur.next = ListNode(v)
        cur = cur.next
    return dummy.next
```

- 时间复杂度：`O(n log n)`
- 空间复杂度：`O(n)`（数组 + 新节点）

### 第三步：递归归并排序

利用快慢指针找到链表中点，分成两半，递归排序后合并：

- 时间复杂度：`O(n log n)`
- 空间复杂度：`O(log n)`（递归栈深度）

这种写法很经典，但空间不满足进阶要求。

### 第四步：最优解法 - 自底向上迭代归并

不用递归，而是用迭代的方式：
1. 先计算链表长度 `n`
2. 从 `step = 1` 开始，每次将长度为 `step` 的有序段两两合并
3. `step` 每次翻倍：`1, 2, 4, 8, ...`
4. 直到 `step >= n`

这样就避免了递归栈，空间复杂度为 `O(1)`。

---

## 完整代码实现

```python
from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    """
    148. 排序链表 - 自底向上归并排序（迭代法）

    核心思想：
    按步长 step = 1, 2, 4, 8... 将链表分段合并，
    每轮合并后有序段长度翻倍，直到整个链表有序。

    时间复杂度：O(n log n)
    空间复杂度：O(1)
    """

    def getListLength(self, head: Optional[ListNode]) -> int:
        length = 0
        while head:
            length += 1
            head = head.next
        return length

    def splitList(self, head: Optional[ListNode], size: int):
        cur = head
        for _ in range(size - 1):
            if cur is None:
                break
            cur = cur.next
        if cur is None or cur.next is None:
            return None
        next_head = cur.next
        cur.next = None
        return next_head

    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]):
        cur = dummy = ListNode()
        while list1 and list2:
            if list1.val < list2.val:
                cur.next = list1
                list1 = list1.next
            else:
                cur.next = list2
                list2 = list2.next
            cur = cur.next
        cur.next = list1 or list2
        while cur.next:
            cur = cur.next
        return dummy.next, cur

    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        length = self.getListLength(head)
        dummy = ListNode(next=head)
        step = 1

        while step < length:
            new_list_tail = dummy
            cur = dummy.next
            while cur:
                head1 = cur
                head2 = self.splitList(head1, step)
                cur = self.splitList(head2, step)
                head, tail = self.mergeTwoLists(head1, head2)
                new_list_tail.next = head
                new_list_tail = tail
            step *= 2

        return dummy.next
```

---

## 示例推演

以 `head = [4, 2, 1, 3]` 为例，长度 `n = 4`。

**step = 1**：把每 1 个节点当作一段，两两合并
- 段1：`[4]`, 段2：`[2]` -> 合并为 `[2, 4]`
- 段3：`[1]`, 段4：`[3]` -> 合并为 `[1, 3]`

链表变为：`[2, 4, 1, 3]` -> 不对，实际上合并后链表是 `[2, 4, 1, 3]` 按段排列。

准确地说，合并后是：`2 -> 4 -> 1 -> 3`

**step = 2**：把每 2 个节点当作一段，两两合并
- 段1：`[2, 4]`, 段2：`[1, 3]` -> 合并为 `[1, 2, 3, 4]`

链表变为：`1 -> 2 -> 3 -> 4`

**step = 4**：`step >= length`，结束。

最终答案：`[1, 2, 3, 4]`

---

## 复杂度分析

| 解法 | 时间复杂度 | 空间复杂度 | 说明 |
|------|-----------|-----------|------|
| 数组排序 | O(n log n) | O(n) | 不符合空间要求 |
| 递归归并 | O(n log n) | O(log n) | 有递归栈开销 |
| 迭代归并 | O(n log n) | O(1) | **最优解** |

---

## 易错点总结

### 1. splitList 的断开操作

`cur.next = None` 必须做，否则两段链表还是连在一起的，合并时会出问题。

### 2. 返回尾节点

`mergeTwoLists` 不仅要返回新头节点，还要返回尾节点，以便下一轮快速拼接。

### 3. 空链表和单节点

`getListLength` 返回 0 时，`step = 1 < 0` 不成立，直接返回 `dummy.next`（即 `None`）。单节点时同理，无需排序。

---

## 扩展思考

### 链表归并 vs 数组归并

数组归并需要额外 `O(n)` 辅助空间，但链表不需要，因为只需要修改指针即可原地合并。这是链表排序相比数组排序的最大优势。

### 快速排序能做吗？

链表的快速排序实现起来比归并排序复杂，且最坏情况下时间复杂度会退化到 `O(n²)`。归并排序是链表排序的首选。

## 相关题目

- [21. 合并两个有序链表](https://leetcode.cn/problems/merge-two-sorted-lists/)
- [23. 合并K个升序链表](https://leetcode.cn/problems/merge-k-sorted-lists/)
- [147. 对链表进行插入排序](https://leetcode.cn/problems/insertion-sort-list/)
