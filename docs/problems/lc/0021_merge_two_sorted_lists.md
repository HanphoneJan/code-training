---
title: 合并两个有序链表
platform: LeetCode
difficulty: 简单
id: 21
url: https://leetcode.cn/problems/merge-two-sorted-lists/
tags:
  - 链表
  - 递归
topics:
  - ../../topics/linked_list.md
patterns:
  - ../../patterns/recursion.md
date_added: 2026-03-20
date_reviewed: []
---

# 21. 合并两个有序链表

## 题目描述

将两个升序链表合并为一个新的升序链表并返回。新链表是通过拼接给定的两个链表的所有节点组成的。

**示例：**
```
输入：list1 = [1,2,4], list2 = [1,3,4]
输出：[1,1,2,3,4,4]

输入：list1 = [], list2 = []
输出：[]

输入：list1 = [], list2 = [0]
输出：[0]
```

**约束：**
- 两个链表的节点数目范围是 `[0, 50]`
- `-100 <= Node.val <= 100`
- `list1` 和 `list2` 均按非递减顺序排列

---

## 解题思路

### 第一步：理解问题本质

两个链表都已经是有序的，目标是把它们合并成一个有序链表。

关键洞察：由于两个链表已经各自有序，我们不需要对所有元素重新排序。只需要每次从两个链表的当前头部，挑出较小的那个接到结果链表末尾，就能保证结果有序。这就是"归并"思想的核心。

### 第二步：暴力解法

**思路：** 把两个链表的所有节点值收集到一个数组，排序后重建链表。

```python
class Solution:
    def mergeTwoLists(self, list1, list2):
        vals = []
        while list1:
            vals.append(list1.val)
            list1 = list1.next
        while list2:
            vals.append(list2.val)
            list2 = list2.next
        vals.sort()
        dummy = ListNode(0)
        cur = dummy
        for v in vals:
            cur.next = ListNode(v)
            cur = cur.next
        return dummy.next
```

**为什么不够好：**
- 时间复杂度 O((n+m) log(n+m))：排序操作浪费了原有的有序信息
- 空间复杂度 O(n+m)：额外开辟了数组，并新建了所有节点
- 两个链表本来就有序，排序是多余的工作

### 第三步：优化解法（递归）

**思路：** 每次比较两个链表头节点，选较小的那个，然后递归处理剩余部分。

递归的直觉：`merge(list1, list2)` 的结果，是较小头节点 + `merge(剩余, 另一链表)` 的结果。

```python
class Solution:
    def mergeTwoLists(self, list1, list2):
        if not list1:
            return list2
        if not list2:
            return list1
        if list1.val <= list2.val:
            list1.next = self.mergeTwoLists(list1.next, list2)
            return list1
        else:
            list2.next = self.mergeTwoLists(list1, list2.next)
            return list2
```

**特点：**
- 时间复杂度 O(n+m)，利用了有序性
- 空间复杂度 O(n+m)：递归调用栈深度等于节点总数
- 代码简洁，但有栈溢出风险（节点很多时）

### 第四步：最优解法（迭代双指针）

**思路：** 用一个"哑节点"（dummy node）作为结果链表的虚拟头，再用一个 `cur` 指针指向结果链表末尾。每次比较 `list1` 和 `list2` 的头节点，把较小的接到 `cur` 后面，然后推进对应链表和 `cur`。

**为什么用哑节点：** 真实链表的头节点也需要被处理，如果不用哑节点，就需要单独处理第一个节点。哑节点让所有节点的处理逻辑统一，避免特判。

**当一个链表遍历完后：** 另一个链表剩余部分已经有序，直接接到 `cur` 后面即可，无需逐个处理。

---

## 完整代码实现

```python
from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        # 哑节点：统一处理头节点，避免特判
        dummy = ListNode(0)
        cur = dummy

        while list1 and list2:
            if list1.val <= list2.val:
                cur.next = list1        # 将 list1 的当前节点接入结果
                list1 = list1.next      # list1 指针后移
            else:
                cur.next = list2        # 将 list2 的当前节点接入结果
                list2 = list2.next      # list2 指针后移
            cur = cur.next              # 结果链表末尾后移

        # 某一链表已空，将另一链表剩余部分直接接上
        cur.next = list1 if list1 else list2

        return dummy.next  # 哑节点的下一个才是真实头节点
```

---

## 示例推演

以 `list1 = [1, 2, 4]`，`list2 = [1, 3, 4]` 为例，逐步追踪：

**初始状态：**
```
dummy -> (空)
cur = dummy
list1: 1 -> 2 -> 4
list2: 1 -> 3 -> 4
```

**第 1 次循环：** `list1.val=1`，`list2.val=1`，1 <= 1，选 list1
```
dummy -> 1
cur 移到 1
list1: 2 -> 4
list2: 1 -> 3 -> 4
```

**第 2 次循环：** `list1.val=2`，`list2.val=1`，2 > 1，选 list2
```
dummy -> 1 -> 1
cur 移到第二个 1
list1: 2 -> 4
list2: 3 -> 4
```

**第 3 次循环：** `list1.val=2`，`list2.val=3`，2 <= 3，选 list1
```
dummy -> 1 -> 1 -> 2
cur 移到 2
list1: 4
list2: 3 -> 4
```

**第 4 次循环：** `list1.val=4`，`list2.val=3`，4 > 3，选 list2
```
dummy -> 1 -> 1 -> 2 -> 3
cur 移到 3
list1: 4
list2: 4
```

**第 5 次循环：** `list1.val=4`，`list2.val=4`，4 <= 4，选 list1
```
dummy -> 1 -> 1 -> 2 -> 3 -> 4
cur 移到第一个 4
list1: (空)
list2: 4
```

**退出循环：** list1 为空，将 list2 剩余部分（节点 4）接上
```
dummy -> 1 -> 1 -> 2 -> 3 -> 4 -> 4
```

返回 `dummy.next`，得到 `[1, 1, 2, 3, 4, 4]`，正确。

---

## 复杂度分析

| 解法 | 时间复杂度 | 空间复杂度 | 说明 |
|------|-----------|-----------|------|
| 暴力（收集排序重建） | O((n+m) log(n+m)) | O(n+m) | 排序浪费了有序信息，新建节点占用额外空间 |
| 递归 | O(n+m) | O(n+m) | 利用有序性，但递归栈深度等于总节点数 |
| 迭代双指针（最优） | O(n+m) | O(1) | 原地修改指针，无额外空间开销 |

其中 n、m 分别为两个链表的节点数。

---

## 易错点总结

- **哑节点忘记返回 `dummy.next`：** `dummy` 本身是虚拟节点，返回它的 `next` 才是真实链表头。
- **循环结束后忘记接尾：** 当一个链表先为空，另一个链表可能还有剩余节点，必须用 `cur.next = list1 if list1 else list2` 接上，不能漏掉。
- **递归解法的栈溢出：** 节点数很多时，递归深度 = 总节点数，可能导致栈溢出。生产环境推荐用迭代解法。
- **两个链表值相等时取哪个：** 取哪个都不影响正确性，但代码中 `<=` 保证了稳定性（list1 的节点优先）。

---

## 扩展思考

- **题目 23（合并 K 个升序链表）** 是本题的扩展：将 K 个有序链表合并，可以用分治（两两调用本题的合并函数）或最小堆实现。
- **归并排序的 Merge 步骤** 和本题完全一致：归并排序的合并阶段，就是把两个有序数组（或链表）合并成一个有序序列。
- **迭代 vs 递归：** 递归代码更简洁，迭代代码更高效（无栈开销）。理解两种写法，可以加深对链表操作和递归思维的认识。
