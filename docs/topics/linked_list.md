---
title: 链表
category: 数据结构
difficulty_range: [简单, 中等]
last_updated: 2026-03-05
---

# 链表

## 知识点概述

链表通过指针连接节点，支持高效插入删除，但随机访问较慢。

### Python中的链表操作

在Python中，对链表的所有操作本质都是对**引用（指针）**的操作。只有`ListNode()`构造函数的调用才会创建新节点。

```python
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
```

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
