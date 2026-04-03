---
title: 随机链表的复制
platform: LeetCode
difficulty: 中等
id: 138
url: https://leetcode.cn/problems/copy-list-with-random-pointer/
tags:
  - 链表
  - 哈希表
topics:
  - ../../topics/linked_list.md
  - ../../topics/hash_table.md
patterns:
  - ../../patterns/linked_list.md
date_added: 2026-04-03
date_reviewed: []
---

# 0138. 随机链表的复制

## 题目描述

给你一个长度为 `n` 的链表，每个节点包含一个额外增加的随机指针 `random`，该指针可以指向链表中的任何节点或空节点。

构造这个链表的 **深拷贝**。深拷贝应该正好由 `n` 个 **全新** 节点组成，其中每个新节点的值都设为其对应的原节点的值。新节点的 `next` 指针和 `random` 指针也都应指向复制链表中的新节点，并使原链表和复制链表中的这些指针能够表示相同的链表状态。**复制链表中的指针都不应指向原链表中的节点**。

## 示例

**示例 1：**
```
输入：head = [[7,null],[13,0],[11,4],[10,2],[1,0]]
输出：[[7,null],[13,0],[11,4],[10,2],[1,0]]
```

**示例 2：**
```
输入：head = [[1,1],[2,1]]
输出：[[1,1],[2,1]]
```

---

## 解题思路

### 第一步：理解难点

普通链表复制很简单，但这道题的 `random` 指针可能指向后面的节点，甚至形成环。复制时没法一次确定 `random` 指向哪个新节点。

### 第二步：暴力解法

每次复制一个节点时，再遍历原链表找到 `random` 对应的新节点。时间复杂度 `O(n²)`。

### 第三步：优化解法 - 哈希表映射

第一遍遍历：创建所有新节点，并建立「原节点 -> 新节点」的映射。

第二遍遍历：通过映射表，连接新节点的 `next` 和 `random`。

- 时间复杂度：`O(n)`
- 空间复杂度：`O(n)`（哈希表）

### 第四步：最优解法 - 交错链表

利用原链表的空间作为映射：
1. 第一遍：在每个原节点后面插入它的复制节点
2. 第二遍：根据原节点的 `random`，设置复制节点的 `random`
3. 第三遍：将交错链表拆分为两个独立链表

- 时间复杂度：`O(n)`
- 空间复杂度：`O(1)`（除了结果链表外）

---

## 完整代码实现

```python
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random

class Solution:
    """
    138. 随机链表的复制 - 交错链表法

    核心思想：
    通过在原链表中插入复制节点，隐式建立原节点和复制节点的对应关系，
    无需额外哈希表即可 O(1) 空间完成复制。

    时间复杂度：O(n)
    空间复杂度：O(1)（除结果外）
    """

    def copyRandomList(self, head: 'Node') -> 'Node':
        if not head:
            return None

        # 步骤1：复制节点，插入到原节点后面
        cur = head
        while cur:
            cur.next = Node(cur.val, cur.next)
            cur = cur.next.next

        # 步骤2：设置复制节点的 random
        cur = head
        while cur:
            if cur.random:
                cur.next.random = cur.random.next
            cur = cur.next.next

        # 步骤3：分离链表
        dummy = Node(0)
        tail = dummy
        cur = head
        while cur:
            copy = cur.next
            tail.next = copy
            cur.next = copy.next
            cur = cur.next
            tail = tail.next

        return dummy.next
```

---

## 示例推演

以 `[[7,null],[13,0],[11,4],[10,2],[1,0]]` 为例。

原链表：`7 -> 13 -> 11 -> 10 -> 1`

**步骤1 - 插入复制节点后**：
`7 -> 7' -> 13 -> 13' -> 11 -> 11' -> 10 -> 10' -> 1 -> 1'`

**步骤2 - 设置 random**：
- 原节点 7 的 random 为 null，7' 的 random 也为 null
- 原节点 13 的 random 指向索引 0（即 7），13' 的 random 指向 7'
- 原节点 11 的 random 指向索引 4（即 1），11' 的 random 指向 1'
- 以此类推

**步骤3 - 分离链表**：
- 原链表恢复：`7 -> 13 -> 11 -> 10 -> 1`
- 新链表：`7' -> 13' -> 11' -> 10' -> 1'`

---

## 复杂度分析

| 解法 | 时间复杂度 | 空间复杂度 | 说明 |
|------|-----------|-----------|------|
| 暴力 | O(n²) | O(1) | 每次找 random 都遍历 |
| 哈希表 | O(n) | O(n) | 直观易懂 |
| 交错链表 | O(n) | O(1) | **最优解** |

---

## 易错点总结

### 1. 空链表判断

如果 `head` 为 `None`，直接返回 `None`。

### 2. random 为 null 的处理

在步骤2中，`cur.random` 可能为 `None`，必须加 `if` 判断，否则访问 `cur.random.next` 会报错。

### 3. 恢复原链表

步骤3中 `cur.next = copy.next` 这一步很重要，确保原链表结构不被破坏。

---

## 扩展思考

### 为什么这道题常考？

它同时考察了链表操作（插入、拆分）和复杂数据结构的复制，是链表类题目的巅峰之一。

## 相关题目

- [133. 克隆图](https://leetcode.cn/problems/clone-graph/)
- [148. 排序链表](https://leetcode.cn/problems/sort-list/)
