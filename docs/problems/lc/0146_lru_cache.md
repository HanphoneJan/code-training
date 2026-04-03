---
title: LRU 缓存
platform: LeetCode
difficulty: 中等
id: 146
url: https://leetcode.cn/problems/lru-cache/
tags:
  - 设计
  - 哈希表
  - 链表
  - 双向链表
topics:
  - ../../topics/design.md
  - ../../topics/hash_table.md
  - ../../topics/linked_list.md
patterns:
  - ../../patterns/lru_cache.md
date_added: 2026-04-03
date_reviewed: []
---

# 0146. LRU 缓存

## 题目描述

请你设计并实现一个满足 [LRU (最近最少使用) 缓存](https://baike.baidu.com/item/LRU) 约束的数据结构。

实现 `LRUCache` 类：

- `LRUCache(int capacity)` 以 **正整数** 作为容量 `capacity` 初始化 LRU 缓存
- `int get(int key)` 如果关键字 `key` 存在于缓存中，则返回关键字的值，否则返回 `-1` 。
- `void put(int key, int value)` 如果关键字 `key` 已经存在，则变更其数据值 `value` ；如果不存在，则向缓存中插入该组 `key-value` 。如果插入操作导致关键字数量超过 `capacity` ，则应该 **逐出** 最久未使用的关键字。

函数 `get` 和 `put` 必须以 `O(1)` 的平均时间复杂度运行。

## 示例

**示例：**
```
输入
["LRUCache", "put", "put", "get", "put", "get", "put", "get", "get", "get"]
[[2], [1, 1], [2, 2], [1], [3, 3], [2], [4, 4], [1], [3], [4]]
输出
[null, null, null, 1, null, -1, null, -1, 3, 4]

解释
LRUCache lRUCache = new LRUCache(2);
lRUCache.put(1, 1); // 缓存是 {1=1}
lRUCache.put(2, 2); // 缓存是 {1=1, 2=2}
lRUCache.get(1);    // 返回 1
lRUCache.put(3, 3); // 该操作会使得关键字 2 作废，缓存是 {1=1, 3=3}
lRUCache.get(2);    // 返回 -1 (未找到)
lRUCache.put(4, 4); // 该操作会使得关键字 1 作废，缓存是 {4=4, 3=3}
lRUCache.get(1);    // 返回 -1 (未找到)
lRUCache.get(3);    // 返回 3
lRUCache.get(4);    // 返回 4
```

---

## 解题思路

### 第一步：分析需求

需要实现一个缓存，支持：
1. `get`：`O(1)` 查找
2. `put`：`O(1)` 插入/更新
3. 淘汰最久未使用的元素：`O(1)` 删除最久未用

单独用哈希表无法维护使用顺序，单独用链表无法 `O(1)` 查找。所以需要**哈希表 + 双向链表**的组合。

### 第二步：数据结构选择

- **哈希表**：`key -> Node`，实现 `O(1)` 查找
- **双向链表**：按使用时间排序，头部最近使用，尾部最久未使用

为什么用双向链表？因为删除节点和移动节点到头部都需要修改前驱/后继指针，双向链表都是 `O(1)`。

### 第三步：操作流程

- `get(key)`：
  1. 哈希表查找，不存在返回 -1
  2. 存在则把节点移到链表头部，返回 value

- `put(key, value)`：
  1. 如果 key 已存在，更新 value，移到头部
  2. 如果 key 不存在，创建新节点插入头部
  3. 如果超出容量，删除尾部节点，并从哈希表中移除

### 第四步：哨兵节点的妙用

使用**循环双向链表 + 哨兵节点**（dummy node），可以避免大量空指针判断，代码更加简洁优雅。

---

## 完整代码实现

```python
class Node:
    """双向链表节点"""
    __slots__ = 'prev', 'next', 'key', 'value'

    def __init__(self, key=0, value=0):
        self.key = key
        self.value = value

class LRUCache:
    """
    146. LRU 缓存 - 哈希表 + 双向链表

    核心思想：
    哈希表实现 O(1) 查找，双向链表维护使用顺序。
    头部是最新使用的，尾部是最久未使用的。

    时间复杂度：get 和 put 都是 O(1)
    空间复杂度：O(capacity)
    """

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.dummy = Node()
        self.dummy.prev = self.dummy
        self.dummy.next = self.dummy
        self.key_to_node = {}

    def get_node(self, key: int):
        if key not in self.key_to_node:
            return None
        node = self.key_to_node[key]
        self.remove(node)
        self.push_front(node)
        return node

    def get(self, key: int) -> int:
        node = self.get_node(key)
        return node.value if node else -1

    def put(self, key: int, value: int) -> None:
        node = self.get_node(key)
        if node:
            node.value = value
            return
        self.key_to_node[key] = node = Node(key, value)
        self.push_front(node)
        if len(self.key_to_node) > self.capacity:
            back_node = self.dummy.prev
            del self.key_to_node[back_node.key]
            self.remove(back_node)

    def remove(self, x: Node) -> None:
        x.prev.next = x.next
        x.next.prev = x.prev

    def push_front(self, x: Node) -> None:
        x.prev = self.dummy
        x.next = self.dummy.next
        x.prev.next = x
        x.next.prev = x
```

---

## 示例推演

容量为 2，操作序列：`put(1,1), put(2,2), get(1), put(3,3)`

链表状态（从左到右表示 dummy -> 最新 -> ... -> 最旧 -> dummy）：

1. `put(1,1)`：插入节点 1。链表：`[1]`
2. `put(2,2)`：插入节点 2。链表：`[2, 1]`（2 在头部，更最近）
3. `get(1)`：命中节点 1，移到头部。链表：`[1, 2]`
4. `put(3,3)`：容量已满，插入节点 3 前需要先淘汰最久未用的节点 2。
   链表：`[3, 1]`

最终 `get(2)` 返回 `-1`。

---

## 复杂度分析

| 操作 | 时间复杂度 | 空间复杂度 | 说明 |
|------|-----------|-----------|------|
| get | O(1) | O(capacity) | 哈希表 + 链表移动 |
| put | O(1) | O(capacity) | 哈希表 + 链表插入/删除 |

---

## 易错点总结

### 1. 节点移动顺序

`get` 命中后一定要把节点移到头部，表示最近使用。

### 2. 淘汰时的删除

淘汰尾部节点时，既要删除链表节点，也要从哈希表中删除对应的 key。

### 3. __slots__ 的作用

`__slots__` 可以限制实例属性，提高访问速度并减少内存占用。在 LRU Cache 这种高频操作中非常有用。

### 4. 哨兵节点的初始化

`dummy.prev = dummy; dummy.next = dummy` 构成自循环，这样 remove 和 push_front 操作时不需要判断 null。

---

## 扩展思考

### LFU Cache

[460. LFU 缓存](https://leetcode.cn/problems/lfu-cache/) 是 LRU 的进阶版，需要按访问频率淘汰，实现更加复杂。

### OrderedDict

Python 的 `collections.OrderedDict` 封装了类似的功能，其 `move_to_end` 和 `popitem(last=False)` 方法可以直接实现 LRU。

## 相关题目

- [460. LFU 缓存](https://leetcode.cn/problems/lfu-cache/)
- [432. 全 O(1) 的数据结构](https://leetcode.cn/problems/all-oone-data-structure/)
