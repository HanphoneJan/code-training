---
title: 链表
category: 数据结构
difficulty_range: [简单, 中等]
last_updated: 2026-03-23
---

# 链表

> [几道常见的链表算法题 | JavaGuide](https://javaguide.cn/cs-basics/algorithms/linkedlist-algorithm-problems.html)

## 知识点概述

链表通过指针连接节点，支持高效插入删除，但随机访问较慢。

**链表（LinkedList）** 虽然是一种线性表，但是并不会按线性的顺序存储数据，使用的不是连续的内存空间来存储数据。链表的插入和删除操作的复杂度为 O(1)，只需要知道目标位置元素的上一个元素即可。但是，在查找一个节点或者访问特定位置的节点的时候复杂度为 O(n)。

使用链表结构可以克服数组需要预先知道数据大小的缺点，链表结构可以充分利用计算机内存空间，实现灵活的内存动态管理。但链表不会节省空间，相比于数组会占用更多的空间，因为链表中每个节点存放的还有指向其他节点的指针。除此之外，链表不具有数组随机读取的优点。

### Python中的链表操作

在Python中，对链表的所有操作本质都是对**引用（指针）**的操作。只有`ListNode()`构造函数的调用才会创建新节点。

```python
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
```

### 时间复杂度

| 操作 | 时间复杂度 | 说明 |
|------|-----------|------|
| 访问 | O(n) | 访问特定位置的元素需要遍历 |
| 插入删除 | O(1) | 必须知道插入元素的位置，无需移动其他元素 |

## 链表分类

1. **单链表**：每个节点只包含指向下一个节点的指针
2. **双向链表**：每个节点包含指向前驱和后继的指针
3. **循环链表**：尾节点指向头节点，形成环
4. **双向循环链表**：双向链表 + 循环结构

## 循环条件选择

链表遍历的循环条件选择：

| 循环条件 | 能访问到的节点 | 核心目标 | 适用场景 | 安全前提 |
|---------|--------------|---------|---------|---------|
| `while node` | 所有节点（含最后一个） | 处理每个节点本身 | 遍历打印、统计节点数、查找目标值 | 无需额外校验 |
| `while node.next` | 仅到倒数第二个节点 | 处理节点的后继 | 找尾节点、尾部插入、删除最后一个节点 | 需先校验`if not node` |
| `while node.next.next` | 仅到倒数第三个节点 | 处理节点的后继的后继 | 快慢指针判环/找中点、删除倒数第二个节点 | 需先校验`node and node.next` |

## 常见考点

- 快慢指针
- 反转与合并
- 环检测

## 核心操作

### 反转链表

```python
# 反转整个链表
def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
    cur = head
    pre = None
    while cur:
        tmp = cur.next
        cur.next = pre
        pre = cur
        cur = tmp
    return pre

# 反转链表的中间部分（第left到right个节点）
def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
    p0 = dummy = ListNode(next=head)
    # 移动p0到left的前一个节点
    for _ in range(left - 1):
        p0 = p0.next

    pre = None
    cur = p0.next
    # 反转区间内的节点
    for _ in range(right - left + 1):
        nxt = cur.next
        cur.next = pre
        pre = cur
        cur = nxt

    # 连接反转后的链表
    p0.next.next = cur
    p0.next = pre
    return dummy.next
```

### 链表相加

```python
def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode], carry=0) -> Optional[ListNode]:
    if l1 is None and l2 is None:
        return ListNode(carry) if carry else None
    if l1 is None:
        l1, l2 = l2, l1  # 保证l1非空，简化代码
    carry += l1.val + (l2.val if l2 else 0)
    l1.val = carry % 10
    l1.next = self.addTwoNumbers(l1.next, l2.next if l2 else None, carry // 10)
    return l1
```

### 归并排序

```python
def sortList(self, head: ListNode) -> ListNode:
    if not head or not head.next:
        return head

    # 找到中点（快慢指针）
    def find_mid(head):
        slow, fast = head, head.next
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        return slow

    # 拆分链表
    mid = find_mid(head)
    right_head = mid.next
    mid.next = None

    # 递归排序
    left = self.sortList(head)
    right = self.sortList(right_head)

    # 合并两个有序链表
    return self.merge(left, right)

def merge(self, l1: ListNode, l2: ListNode) -> ListNode:
    dummy = ListNode(0)
    cur = dummy
    while l1 and l2:
        if l1.val < l2.val:
            cur.next = l1
            l1 = l1.next
        else:
            cur.next = l2
            l2 = l2.next
        cur = cur.next
    cur.next = l1 if l1 else l2
    return dummy.next
```

### 双指针技巧

```python
# 找链表中点（用于归并排序）
def find_middle(head):
    slow = fast = head
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
    return slow

# 找倒数第n个节点
def find_kth_from_end(head, n):
    fast = slow = head
    for _ in range(n):
        fast = fast.next
    while fast:
        slow = slow.next
        fast = fast.next
    return slow
```

## 如何区分链表 vs 数组

**本质区别是内存是否连续分配，以及是否需要指针拼接。**

链表相对数组的主要优势是**内存的动态利用**，所以尽量不要用数组辅助去做链表题。

| 特性 | 数组 | 链表 |
|------|-----|------|
| 内存分配 | 连续 | 非连续 |
| 随机访问 | O(1) | O(n) |
| 插入删除 | O(n) | O(1) |
| 适用场景 | 频繁访问 | 频繁增删 |
