---
title: LRU 缓存
platform: LeetCode
difficulty: 中等
id: 146
url: https://leetcode.cn/problems/lru-cache/
tags:
  - 设计
  - 哈希表
  - 双向链表
  - 链表
topics:
  - ../../topics/hash_table.md
  - ../../topics/linked_list.md
patterns:
  - ../../patterns/lru_cache.md
date_added: 2026-03-23
date_reviewed: []
---

# 0146. LRU 缓存

## 题目描述

请你设计并实现一个满足 **LRU (最近最少使用) 缓存** 约束的数据结构。

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

### 第一步：理解 LRU 机制

**LRU (Least Recently Used)**：最近最少使用淘汰策略。

**核心操作**：
1. `get`：访问某个 key，该 key 变为"最近使用"
2. `put`：
   - key 已存在：更新 value，变为"最近使用"
   - key 不存在：插入新 key
     - 如果容量已满，淘汰"最久未使用"的 key
     - 新 key 变为"最近使用"

### 第二步：数据结构选择

**需求分析**：
- `get` 需要 O(1) 查找 → 哈希表
- `put` 需要 O(1) 插入/删除 → 哈希表
- 需要维护使用顺序，并快速移动节点 → 双向链表

**组合方案**：
- **哈希表**：`key -> ListNode`，O(1) 查找
- **双向链表**：维护访问顺序，头部是最近使用，尾部是最久未使用

**为什么用双向链表？**
- 删除节点时知道前驱节点（有 prev 指针），O(1) 删除
- 头部/尾部插入删除都是 O(1)

### 第三步：操作流程

**get(key)**：
1. key 不在哈希表：返回 -1
2. key 在哈希表：
   - 从链表当前位置删除该节点
   - 插入到链表头部
   - 返回 value

**put(key, value)**：
1. key 已存在：
   - 更新节点 value
   - 移到链表头部
2. key 不存在：
   - 创建新节点，插入链表头部和哈希表
   - 如果超出容量：删除链表尾部节点，同时删除哈希表对应项

---

## 完整代码实现

```python
class LRUCache:
    """
    LRU (Least Recently Used) 缓存机制

    核心思想：哈希表 + 双向链表
    - 哈希表 O(1) 查找
    - 双向链表维护访问顺序，支持 O(1) 插入删除
    """

    class DLinkedNode:
        """双向链表节点"""
        def __init__(self, key: int = 0, value: int = 0):
            self.key = key
            self.value = value
            self.prev = None
            self.next = None

    def __init__(self, capacity: int):
        self.cache = {}  # 哈希表：key -> DLinkedNode
        self.capacity = capacity
        self.size = 0

        # 使用伪头部和伪尾部节点，简化边界处理
        self.head = self.DLinkedNode()
        self.tail = self.DLinkedNode()
        self.head.next = self.tail
        self.tail.prev = self.head

    def _remove_node(self, node: 'LRUCache.DLinkedNode') -> None:
        """从双向链表中移除指定节点"""
        node.prev.next = node.next
        node.next.prev = node.prev

    def _add_to_head(self, node: 'LRUCache.DLinkedNode') -> None:
        """将节点添加到头部（最近使用）"""
        node.prev = self.head
        node.next = self.head.next
        self.head.next.prev = node
        self.head.next = node

    def _move_to_head(self, node: 'LRUCache.DLinkedNode') -> None:
        """将节点移到头部（标记为最近使用）"""
        self._remove_node(node)
        self._add_to_head(node)

    def _pop_tail(self) -> 'LRUCache.DLinkedNode':
        """移除尾部节点（最久未使用），返回该节点"""
        node = self.tail.prev
        self._remove_node(node)
        return node

    def get(self, key: int) -> int:
        """获取key对应的值，并将节点移到头部"""
        if key not in self.cache:
            return -1

        node = self.cache[key]
        self._move_to_head(node)  # 标记为最近使用
        return node.value

    def put(self, key: int, value: int) -> None:
        """插入或更新key-value"""
        if key in self.cache:
            # 更新已有节点
            node = self.cache[key]
            node.value = value
            self._move_to_head(node)
        else:
            # 创建新节点
            new_node = self.DLinkedNode(key, value)
            self.cache[key] = new_node
            self._add_to_head(new_node)
            self.size += 1

            # 检查容量，超出则淘汰最久未使用的节点
            if self.size > self.capacity:
                tail_node = self._pop_tail()
                del self.cache[tail_node.key]
                self.size -= 1
```

---

## 示例推演

**示例**：`capacity = 2`

**操作序列推演**：

| 操作 | 缓存状态 | 链表状态（头->尾） | 说明 |
|------|----------|-------------------|------|
| put(1,1) | {1:1} | 1 | 插入1 |
| put(2,2) | {1:1,2:2} | 2->1 | 插入2到头部 |
| get(1) | {1:1,2:2} | 1->2 | 访问1，移到头部 |
| put(3,3) | {1:1,3:3} | 3->1 | 容量满，淘汰2，插入3 |
| get(2) | {1:1,3:3} | 3->1 | 2不存在，返回-1 |
| put(4,4) | {3:3,4:4} | 4->3 | 容量满，淘汰1，插入4 |
| get(1) | {3:3,4:4} | 4->3 | 1不存在，返回-1 |
| get(3) | {3:3,4:4} | 3->4 | 访问3，移到头部 |
| get(4) | {3:3,4:4} | 4->3 | 访问4，移到头部 |

---

## 复杂度分析

| 操作 | 时间复杂度 | 空间复杂度 |
|------|-----------|-----------|
| get | O(1) | O(capacity) |
| put | O(1) | O(capacity) |

---

## 易错点总结

### 1. 伪头部和伪尾部

```python
self.head = self.DLinkedNode()  # 伪头部
self.tail = self.DLinkedNode()  # 伪尾部
self.head.next = self.tail
self.tail.prev = self.head
```

使用伪节点可以统一处理边界，避免大量 if-else。

### 2. 删除节点时同时删除哈希表

```python
tail_node = self._pop_tail()
del self.cache[tail_node.key]  # 别忘了删除哈希表
```

### 3. 更新操作也要移动节点

```python
if key in self.cache:
    node = self.cache[key]
    node.value = value
    self._move_to_head(node)  # 别忘了移到头部
```

### 4. size 的维护

```python
self.size += 1  # 插入时
self.size -= 1  # 淘汰时
```

也可以不维护 size，直接用 `len(self.cache)`。

---

## 扩展思考

### 1. Python 的 OrderedDict

```python
from collections import OrderedDict

class LRUCache:
    def __init__(self, capacity: int):
        self.cache = OrderedDict()
        self.capacity = capacity

    def get(self, key: int) -> int:
        if key not in self.cache:
            return -1
        self.cache.move_to_end(key)  # 移到末尾（最近使用）
        return self.cache[key]

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            self.cache.move_to_end(key)
        self.cache[key] = value
        if len(self.cache) > self.capacity:
            self.cache.popitem(last=False)  # 弹出最前面的（最久未使用）
```

### 2. LFU (Least Frequently Used) 缓存

淘汰访问次数最少的元素，需要额外维护访问次数。

### 3. 线程安全的 LRU 缓存

需要加锁保护共享状态。

---

## 相关题目

- [460. LFU 缓存](https://leetcode.cn/problems/lfu-cache/)
- [432. 全 O(1) 的数据结构](https://leetcode.cn/problems/all-oone-data-structure/)
