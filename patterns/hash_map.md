---
title: 哈希映射模式
category: 算法模式
difficulty: 简单-中等
applicable_to:
  - 数组
  - 字符串
  - 查找问题
last_updated: 2026-02-25
---

# 哈希映射模式

## 模式概述

使用哈希表存储数据，实现 O(1) 时间的查找、插入和删除。

## 核心思想

**空间换时间**：用额外的空间存储信息，将查找时间从 O(n) 降到 O(1)。

## 适用场景

1. **快速查找**：判断元素是否存在
2. **配对问题**：找到满足条件的两个元素
3. **频率统计**：计数、去重
4. **映射关系**：建立元素间的对应关系

## 基本模板

### 存在性判断

```python
def contains(arr, target):
    seen = set()
    
    for num in arr:
        if target - num in seen:
            return True
        seen.add(num)
    
    return False
```

### 频率统计

```python
from collections import Counter

def count_frequency(arr):
    # 方法 1：使用 Counter
    counter = Counter(arr)
    
    # 方法 2：手动统计
    freq = {}
    for item in arr:
        freq[item] = freq.get(item, 0) + 1
    
    return freq
```

### 索引映射

```python
def index_map(arr):
    # 元素 -> 索引
    index_dict = {val: idx for idx, val in enumerate(arr)}
    return index_dict
```

### 分组映射

```python
from collections import defaultdict

def group_by(arr, key_func):
    groups = defaultdict(list)
    
    for item in arr:
        key = key_func(item)
        groups[key].append(item)
    
    return groups
```

## 实战案例

### 案例 1：两数之和

使用哈希表存储已遍历的元素。

```python
def twoSum(nums, target):
    hashmap = {}
    
    for i, num in enumerate(nums):
        complement = target - num
        
        if complement in hashmap:
            return [hashmap[complement], i]
        
        hashmap[num] = i
    
    return []
```

**相关题目：**
- [1. 两数之和](../problems/lc/0001_two_sum.md)

### 案例 2：字母异位词分组

```python
from collections import defaultdict

def groupAnagrams(strs):
    groups = defaultdict(list)
    
    for s in strs:
        # 使用排序后的字符串作为键
        key = ''.join(sorted(s))
        groups[key].append(s)
    
    return list(groups.values())
```

### 案例 3：最长连续序列

```python
def longestConsecutive(nums):
    num_set = set(nums)
    max_length = 0
    
    for num in num_set:
        # 只从序列起点开始计数
        if num - 1 not in num_set:
            current = num
            length = 1
            
            while current + 1 in num_set:
                current += 1
                length += 1
            
            max_length = max(max_length, length)
    
    return max_length
```

## 常见数据结构

### Python

```python
# 基本字典
d = {}
d = dict()

# 带默认值的字典
from collections import defaultdict
d = defaultdict(int)    # 默认值为 0
d = defaultdict(list)   # 默认值为 []
d = defaultdict(set)    # 默认值为 set()

# 计数器
from collections import Counter
counter = Counter([1, 2, 2, 3, 3, 3])
# Counter({3: 3, 2: 2, 1: 1})

# 集合
s = set()
s = {1, 2, 3}
```

### C++

```cpp
// 哈希表
#include <unordered_map>
unordered_map<int, int> hashmap;

// 哈希集合
#include <unordered_set>
unordered_set<int> hashset;

// 有序映射（红黑树）
#include <map>
map<int, int> ordered_map;
```

## 解题模式

### 模式 1：查找配对

```python
# 在数组中找两个元素满足条件
hashmap = {}
for item in arr:
    if target - item in hashmap:
        # 找到配对
        return [hashmap[target - item], item]
    hashmap[item] = index
```

### 模式 2：计数去重

```python
# 统计并去重
from collections import Counter
counter = Counter(arr)
unique_items = [k for k, v in counter.items() if v == 1]
```

### 模式 3：前缀和 + 哈希

```python
# 统计和为 k 的子数组个数
prefix_sum = 0
sum_count = {0: 1}  # 前缀和 -> 出现次数

for num in nums:
    prefix_sum += num
    
    if prefix_sum - k in sum_count:
        result += sum_count[prefix_sum - k]
    
    sum_count[prefix_sum] = sum_count.get(prefix_sum, 0) + 1
```

### 模式 4：滑动窗口 + 哈希

```python
# 最长不含重复字符的子串
window = {}
left = 0
max_len = 0

for right, char in enumerate(s):
    if char in window:
        left = max(left, window[char] + 1)
    
    window[char] = right
    max_len = max(max_len, right - left + 1)
```

## 时间与空间复杂度

| 操作 | 平均 | 最坏 |
|------|------|------|
| 查找 | O(1) | O(n) |
| 插入 | O(1) | O(n) |
| 删除 | O(1) | O(n) |

**空间复杂度**：O(n)

## 优缺点

### 优点

- ✅ 查找速度快 O(1)
- ✅ 灵活的键值对应
- ✅ 方便计数和去重

### 缺点

- ❌ 需要额外空间
- ❌ 不保证顺序（普通哈希表）
- ❌ 哈希冲突可能影响性能

## 相关知识点

- [数组](../topics/array.md)
- [哈希表](../topics/hash_table.md)
- [双指针](two_pointers.md)
- [滑动窗口](sliding_window.md)

## 练习题目

**简单：**
- [1. 两数之和](../problems/lc/0001_two_sum.md)
- 有效的字母异位词
- 两个数组的交集

**中等：**
- 字母异位词分组
- 最长连续序列
- 和为 K 的子数组

**困难：**
- 最小覆盖子串

## 要点总结

- ✅ 哈希表是空间换时间的典型
- ✅ 适合查找、计数、映射问题
- ✅ Python 中优先使用 Counter 和 defaultdict
- ✅ 注意处理哈希冲突
