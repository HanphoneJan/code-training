---
title: 合并 K 个升序链表
platform: LeetCode
difficulty: 困难
id: 23
url: https://leetcode.cn/problems/merge-k-sorted-lists/
tags:
  - 链表
  - 分治
  - 堆（优先队列）
  - 归并排序
topics:
  - ../../topics/linked_list.md
  - ../../topics/stack_queue_heap_unionfind.md
patterns:
  - ../../patterns/recursion.md
date_added: 2026-03-20
date_reviewed: []
---

# 23. 合并 K 个升序链表

## 题目描述

给你一个链表数组，每个链表都已经按升序排列。请你将所有链表合并到一个升序链表中，返回合并后的链表。

**示例：**
```
输入：lists = [[1,4,5],[1,3,4],[2,6]]
输出：[1,1,2,3,4,4,5,6]
解释：三个链表如下：
1->4->5
1->3->4
2->6
合并后：1->1->2->3->4->4->5->6

输入：lists = []
输出：[]

输入：lists = [[]]
输出：[]
```

**约束：**
- `k == lists.length`，`0 <= k <= 10^4`
- `0 <= lists[i].length <= 500`
- `-10^4 <= lists[i][j] <= 10^4`
- 每个链表均按升序排列
- 所有链表节点数之和不超过 10^4

---

## 解题思路

### 第一步：理解问题本质

本题是 LeetCode 21（合并两个有序链表）的扩展。既然我们会合并两个有序链表，就需要思考如何把这个能力扩展到 K 个链表。

设 K 个链表共有 N 个节点，问题的核心在于：**每次从 K 个链表的当前头节点中找到最小值，接入结果链表**。如何高效地找到这个最小值，决定了算法的优劣。

### 第二步：暴力解法（逐一合并）

**思路：** 把 `lists[0]` 作为基础，依次与 `lists[1]`, `lists[2]`, ..., `lists[k-1]` 合并。

```python
class Solution:
    def mergeKLists(self, lists):
        if not lists:
            return None
        result = lists[0]
        for i in range(1, len(lists)):
            result = self.mergeTwoLists(result, lists[i])
        return result

    def mergeTwoLists(self, l1, l2):
        dummy = ListNode(0)
        cur = dummy
        while l1 and l2:
            if l1.val <= l2.val:
                cur.next = l1
                l1 = l1.next
            else:
                cur.next = l2
                l2 = l2.next
            cur = cur.next
        cur.next = l1 if l1 else l2
        return dummy.next
```

**为什么不够好：**

设每个链表平均有 n 个节点（总节点数 N = k·n）。

- 第 1 次合并：`result`（n 个节点）+ `lists[1]`（n 个节点）→ 遍历 2n 个节点
- 第 2 次合并：`result`（2n 个节点）+ `lists[2]`（n 个节点）→ 遍历 3n 个节点
- ...
- 第 k-1 次合并：`result`（(k-1)n 个节点）+ `lists[k-1]`（n 个节点）→ 遍历 kn 个节点

总遍历次数 = 2n + 3n + ... + kn = n·(2+3+...+k) = O(k²n) = **O(k·N)**

当 k 很大时，这是平方级别的复杂度，效率低下。

### 第三步：优化解法（分治合并）

**思路：** 不再逐一合并，改为两两配对合并，类似归并排序。

第一轮：将 K 个链表两两配对合并，得到 K/2 个链表；
第二轮：对 K/2 个链表再两两配对合并，得到 K/4 个链表；
......
直到只剩一个链表。

**为什么更好：** 每个节点在每一轮中最多被"经过"一次，共 log k 轮，总操作次数为 O(N log k)。

```python
class Solution:
    def mergeKLists(self, lists):
        if not lists:
            return None
        while len(lists) > 1:
            merged = []
            for i in range(0, len(lists), 2):
                l1 = lists[i]
                l2 = lists[i + 1] if i + 1 < len(lists) else None
                merged.append(self.mergeTwoLists(l1, l2))
            lists = merged
        return lists[0]

    def mergeTwoLists(self, l1, l2):
        dummy = ListNode(0)
        cur = dummy
        while l1 and l2:
            if l1.val <= l2.val:
                cur.next = l1; l1 = l1.next
            else:
                cur.next = l2; l2 = l2.next
            cur = cur.next
        cur.next = l1 if l1 else l2
        return dummy.next
```

### 第四步：最优解法（最小堆）

**思路：** 维护一个大小为 K 的最小堆，堆中存储每个链表的当前头节点。每次从堆顶取出最小节点接入结果，然后将该节点的 `next` 推入堆。

**为什么是最优：**
- 堆的大小始终 <= K，每次 push/pop 操作为 O(log k)
- 共处理 N 个节点，总时间复杂度 O(N log k)
- 空间复杂度只有堆本身，O(k)

**一个实现细节：** Python 的 `heapq` 对元素进行比较时，如果第一个字段相同，会比较第二个字段。`ListNode` 对象不支持比较，所以堆中存储的元组格式为 `(节点值, 链表索引, 节点对象)`，用链表索引作为第二字段，避免直接比较 `ListNode`。

---

## 完整代码实现

```python
import heapq
from typing import List, Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        heap = []
        # 将每个链表的头节点推入堆
        # 元组 (节点值, 链表索引, 节点对象)，索引用于打破值相等时的比较
        for i, node in enumerate(lists):
            if node:
                heapq.heappush(heap, (node.val, i, node))

        dummy = ListNode(0)
        cur = dummy

        while heap:
            val, i, node = heapq.heappop(heap)   # 取出当前最小节点
            cur.next = node                        # 接入结果链表
            cur = cur.next
            if node.next:                          # 将该节点的下一个节点推入堆
                heapq.heappush(heap, (node.next.val, i, node.next))

        return dummy.next
```

---

## 示例推演

以 `lists = [[1,4,5], [1,3,4], [2,6]]` 为例，共 3 个链表，用最小堆解法逐步追踪：

**初始化堆：** 将三个链表头节点推入
```
堆：[(1, 0, 节点1→4→5), (1, 1, 节点1→3→4), (2, 2, 节点2→6)]
result: dummy ->
```

**第 1 次 pop：** 取出 (1, 0, 1)，即链表0的节点1；将链表0的下一个节点4推入
```
取出：节点值=1（链表0）
推入：(4, 0, 节点4→5)
result: dummy -> 1
堆：[(1, 1, 节点1→3→4), (2, 2, 节点2→6), (4, 0, 节点4→5)]
```

**第 2 次 pop：** 取出 (1, 1, 1)，即链表1的节点1；将链表1的下一个节点3推入
```
取出：节点值=1（链表1）
推入：(3, 1, 节点3→4)
result: dummy -> 1 -> 1
堆：[(2, 2, 节点2→6), (3, 1, 节点3→4), (4, 0, 节点4→5)]
```

**第 3 次 pop：** 取出 (2, 2, 2)，即链表2的节点2；将链表2的下一个节点6推入
```
取出：节点值=2（链表2）
推入：(6, 2, 节点6)
result: dummy -> 1 -> 1 -> 2
堆：[(3, 1, 节点3→4), (4, 0, 节点4→5), (6, 2, 节点6)]
```

**第 4 次 pop：** 取出 (3, 1, 3)，节点3的下一个是4，推入
```
result: dummy -> 1 -> 1 -> 2 -> 3
堆：[(4, 0, 节点4→5), (4, 1, 节点4), (6, 2, 节点6)]
```

**第 5 次 pop：** 取出 (4, 0, 4)，节点4的下一个是5，推入
```
result: dummy -> 1 -> 1 -> 2 -> 3 -> 4
堆：[(4, 1, 节点4), (5, 0, 节点5), (6, 2, 节点6)]
```

**第 6 次 pop：** 取出 (4, 1, 4)，该节点无下一个，不推入
```
result: dummy -> 1 -> 1 -> 2 -> 3 -> 4 -> 4
堆：[(5, 0, 节点5), (6, 2, 节点6)]
```

**第 7 次 pop：** 取出 (5, 0, 5)，无下一个
```
result: dummy -> 1 -> 1 -> 2 -> 3 -> 4 -> 4 -> 5
堆：[(6, 2, 节点6)]
```

**第 8 次 pop：** 取出 (6, 2, 6)，无下一个，堆空
```
result: dummy -> 1 -> 1 -> 2 -> 3 -> 4 -> 4 -> 5 -> 6
堆：空，退出循环
```

返回 `dummy.next`，得到 `[1,1,2,3,4,4,5,6]`，正确。

---

## 复杂度分析

设 K 为链表数量，N 为所有节点总数，每个链表平均 n = N/K 个节点。

| 解法 | 时间复杂度 | 空间复杂度 | 说明 |
|------|-----------|-----------|------|
| 逐一合并（暴力） | O(k·N) | O(1) | 越靠后合并，result 链表越长，代价越高 |
| 分治合并 | O(N log k) | O(log k) | 两两配对，共 log k 轮，每轮总遍历 N 个节点 |
| 最小堆（最优） | O(N log k) | O(k) | 堆大小为 k，每次 pop/push 为 O(log k) |

分治和最小堆的时间复杂度相同，最小堆的空间复杂度略高（堆大小为 k），分治的递归栈为 O(log k)。两者在实践中性能相近，最小堆实现更直观。

---

## 易错点总结

- **堆中不能直接存 ListNode：** Python 的 `heapq` 比较元素时若第一字段相等，会比较下一字段。`ListNode` 不支持比较运算，会报错。解决方案：元组加入链表索引 `i` 作为第二字段（int 可以比较），避免触碰 `ListNode` 的比较。
- **逐一合并的效率问题：** 每次合并时 result 链表越来越长，导致后续每次合并的代价都在增加。这与从最短的链表开始逐一合并没有本质区别，总体仍是 O(k·N)。
- **分治合并的奇数处理：** 当链表数量为奇数时，最后一个链表无法配对，需要单独保留（代码中 `lists[i+1] if i+1 < len(lists) else None`）。
- **空数组与空链表的边界：** `lists = []` 时直接返回 `None`；链表数组中可能有 `None` 或空链表，推入堆前需判断 `if node`。

---

## 扩展思考

- **本题与归并排序的关系：** 分治合并的思路与归并排序完全一致。归并排序对数组两两合并，本题对链表两两合并，时间复杂度分析也完全相同：O(N log k)。
- **优先队列的通用性：** 最小堆的思路可以推广到"从 K 个有序序列中取第 m 小的元素"问题，是流式数据处理、多路归并排序的核心工具。
- **题目 21（合并两个有序链表）** 是本题的基础：掌握双指针合并两个有序链表后，本题的分治解法自然而然地建立在其上。
- **实际应用：** 数据库的外部排序、分布式系统中多节点数据合并，本质上都是本题的工程版本。
