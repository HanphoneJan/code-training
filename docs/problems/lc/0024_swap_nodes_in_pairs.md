---
title: 两两交换链表中的节点
platform: LeetCode
difficulty: 中等
id: 24
url: https://leetcode.cn/problems/swap-nodes-in-pairs/
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

# 24. 两两交换链表中的节点

## 题目描述

给你一个链表，两两交换其中相邻的节点，并返回交换后链表的头节点。你必须在不修改节点内部的值的情况下完成本题（即，只能进行节点交换）。

**示例：**
```
输入：head = [1,2,3,4]
输出：[2,1,4,3]

输入：head = []
输出：[]

输入：head = [1]
输出：[1]
```

**约束：**
- 链表中节点的数目在范围 `[0, 100]` 内
- `0 <= Node.val <= 100`

---

## 解题思路

### 第一步：理解问题本质

题目要求把相邻的两个节点互换位置，不能修改节点的值，只能改变指针指向。

以 `1 -> 2 -> 3 -> 4` 为例，目标是 `2 -> 1 -> 4 -> 3`。

观察规律：节点 1 和 2 互换，节点 3 和 4 互换，每对之间的关系相同。因此，关键在于**如何正确地交换一对节点，同时维护好前后连接**。

### 第二步：暴力解法（修改值）

如果允许修改节点值（本题不允许），可以直接遍历，每次交换相邻两个节点的 val：

```python
# 注意：本题不允许此做法，仅作对比说明
class Solution:
    def swapPairs(self, head):
        cur = head
        while cur and cur.next:
            cur.val, cur.next.val = cur.next.val, cur.val  # 禁止！
            cur = cur.next.next
```

**为什么不符合题意：** 题目明确要求只能交换节点本身（修改指针），不能修改节点的值。这是因为在实际场景中，节点可能存储的是复杂对象的引用，值交换会带来语义问题。

### 第三步：优化解法（递归）

**递归的直觉：** `swapPairs(head)` 的结果，是将 `head` 和 `head.next` 交换，然后 `head.next` 接上 `swapPairs(head.next.next)` 的结果。

```python
class Solution:
    def swapPairs(self, head):
        # 递归终止：不足两个节点，无法交换
        if not head or not head.next:
            return head
        new_head = head.next          # 新的头是第二个节点
        head.next = self.swapPairs(new_head.next)  # 第一个节点接上后续交换结果
        new_head.next = head          # 第二个节点指向第一个节点
        return new_head               # 返回新头
```

**特点：**
- 时间复杂度 O(n)，空间复杂度 O(n)（递归栈深度 n/2）
- 代码简洁优雅，但有栈开销

### 第四步：最优解法（迭代）

**思路：** 用哑节点作为虚拟头，`cur` 指针指向每对节点的"前一个节点"。每次循环处理 `cur` 后面的一对节点（`first` 和 `second`），完成交换后让 `cur` 跳过这一对，指向下一对的前驱。

**交换一对节点的三步操作（以 `cur -> first -> second -> 后续` 为例）：**

1. `cur.next = second`：让 `cur` 直接指向 `second`（second 成为这对的新头）
2. `first.next = second.next`：让 `first` 指向 `second` 原来的下一个节点
3. `second.next = first`：让 `second` 指向 `first`（完成交换）

操作完成后，结构变为：`cur -> second -> first -> 后续`，然后 `cur = first`（first 是这对的末尾，也是下一对的前驱）。

**为什么用哑节点：** 链表头节点也需要参与交换，如果没有哑节点，处理头节点时需要特殊逻辑。哑节点让所有对的处理逻辑统一。

---

## 完整代码实现

```python
from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(0, head)  # 哑节点，next 指向链表头
        cur = dummy

        while cur.next and cur.next.next:
            first = cur.next        # 这一对的第一个节点
            second = cur.next.next  # 这一对的第二个节点

            # 三步完成交换
            cur.next = second           # step 1: cur 指向 second
            first.next = second.next    # step 2: first 接上 second 后面的节点
            second.next = first         # step 3: second 指向 first

            # cur 移到下一对的前驱位置（first 是交换后这对的末尾）
            cur = first

        return dummy.next  # 哑节点的 next 才是真实头节点
```

---

## 示例推演

以 `head = [1, 2, 3, 4]` 为例，逐步追踪：

**初始状态：**
```
dummy(0) -> 1 -> 2 -> 3 -> 4
cur = dummy
```

**第 1 次循环：** `cur.next=1`，`cur.next.next=2`，均非空，进入循环
```
first = 节点1，second = 节点2

step 1: cur.next = second     → dummy -> 2 -> ...
step 2: first.next = second.next = 节点3  → 1 -> 3 -> 4
step 3: second.next = first   → 2 -> 1 -> 3 -> 4

完整链表：dummy -> 2 -> 1 -> 3 -> 4
cur = first = 节点1
```

**第 2 次循环：** `cur.next=3`，`cur.next.next=4`，均非空，进入循环
```
first = 节点3，second = 节点4

step 1: cur.next = second     → 节点1 -> 4 -> ...
step 2: first.next = second.next = None  → 3 -> None
step 3: second.next = first   → 4 -> 3 -> None

完整链表：dummy -> 2 -> 1 -> 4 -> 3 -> None
cur = first = 节点3
```

**第 3 次检查：** `cur.next=None`，退出循环

返回 `dummy.next`，得到 `[2, 1, 4, 3]`，正确。

**指针变化可视化（第 1 次循环前后）：**
```
交换前：dummy -> [1] -> [2] -> [3] -> [4]
                  ↑      ↑
               first  second

交换后：dummy -> [2] -> [1] -> [3] -> [4]
                         ↑
                        cur（下一对的前驱）
```

---

## 复杂度分析

| 解法 | 时间复杂度 | 空间复杂度 | 说明 |
|------|-----------|-----------|------|
| 修改值（不符合题意） | O(n) | O(1) | 违反题目约束，不可用 |
| 递归 | O(n) | O(n) | 递归栈深度为 n/2，每次递归处理一对节点 |
| 迭代（最优） | O(n) | O(1) | 原地修改指针，无额外空间开销 |

---

## 易错点总结

- **三步指针操作的顺序不能颠倒：** 必须先 `cur.next = second`，再 `first.next = second.next`，最后 `second.next = first`。如果先执行 `second.next = first`，则 `second.next` 已经变成 `first`，`second.next`（即原来 `second` 后面的节点）就丢失了。正确做法是先保存好 `second.next`，或按上述顺序操作。
- **cur 移动到 `first` 而非 `second`：** 交换后 `second -> first -> 下一对`，`first` 是这对的末尾，也是下一对两个节点的前驱，所以 `cur = first`，而不是 `cur = second`。
- **哑节点忘记传入 head：** `ListNode(0, head)` 让哑节点的 `next` 直接指向 `head`，省去了 `dummy.next = head` 这一步，不要漏掉初始连接。
- **链表节点数为奇数时：** 最后一个节点无法配对，循环条件 `cur.next and cur.next.next` 会在 `cur.next.next` 为 `None` 时退出，最后那个节点保持原位，不需要额外处理。

---

## 扩展思考

- **K 个一组翻转链表（LeetCode 25）** 是本题的扩展：将每 K 个节点为一组进行翻转，而不是每 2 个。本题是 K=2 的特例。掌握本题的迭代思路，有助于理解题目 25 的通用做法。
- **递归 vs 迭代：** 递归写法简洁，体现了"问题分解"的思想；迭代写法高效，体现了"原地操作"的思想。两种思维方式在链表题中都非常重要，建议两种都能熟练写出。
- **哑节点（Dummy Node）技巧：** 本题和题目 21、23 都用到了哑节点。这是链表题的通用技巧：当头节点可能发生变化时（比如头节点参与交换、删除），引入哑节点可以统一处理逻辑，避免对头节点的特殊判断。
