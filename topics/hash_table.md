---
title: 哈希表
category: 数据结构
difficulty_range: [简单, 中等]
last_updated: 2026-02-25
---

# 哈希表

## 知识点概述

哈希表（Hash Table）是根据键（Key）直接访问值（Value）的数据结构。通过哈希函数将键映射到表中的位置来访问记录。

### 核心特性

- **快速查找**：平均 O(1) 时间复杂度
- **键值对存储**：每个键对应一个值
- **无序性**：大多数实现不保证顺序
- **唯一键**：键必须唯一

### 时间复杂度

| 操作 | 平均 | 最坏 |
|------|------|------|
| 查找 | O(1) | O(n) |
| 插入 | O(1) | O(n) |
| 删除 | O(1) | O(n) |

## 常见题型

### 1. 查找与计数

- 两数之和
- 统计字符频率
- 数组交集

**相关题目：**
- [1. 两数之和](../problems/lc/0001_two_sum.md)

### 2. 去重

- 判断重复元素
- 找出唯一元素

### 3. 映射关系

- 字符串映射
- 索引映射

## 解题技巧

### 技巧 1：空间换时间

使用哈希表存储中间结果，将 O(n²) 优化到 O(n)。

```python
# 示例：查找问题
hashmap = {}
for item in items:
    if target - item in hashmap:
        return True
    hashmap[item] = True
```

### 技巧 2：计数器模式

```python
from collections import Counter

# 统计频率
counter = Counter(arr)
```

### 技巧 3：索引映射

记录元素与索引的对应关系。

```python
# 元素 -> 索引
index_map = {val: idx for idx, val in enumerate(arr)}
```

## 常用实现

### Python

- `dict`：基本字典
- `collections.defaultdict`：带默认值的字典
- `collections.Counter`：计数器

### C++

- `unordered_map`：哈希表
- `unordered_set`：哈希集合
- `map`：有序映射（红黑树）

## 相关知识点

- [数组](array.md)
- [字符串](string.md)
- [哈希映射模式](../patterns/hash_map.md)

## 题目列表

**简单：**
- [1. 两数之和](../problems/lc/0001_two_sum.md)

**中等：**
- TBD

## 注意事项

- 哈希冲突的处理
- 选择合适的哈希函数
- 空间复杂度权衡
