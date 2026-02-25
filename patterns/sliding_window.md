---
title: 滑动窗口模式
category: 算法模式
difficulty: 中等
applicable_to:
  - 数组
  - 字符串
  - 子数组/子串问题
last_updated: 2026-02-25
---

# 滑动窗口模式

## 模式概述

滑动窗口是双指针的一种特殊形式，维护一个窗口在数组或字符串上滑动，用于解决连续子数组/子串问题。

## 适用场景

1. **最长/最短子数组**满足某条件
2. **子串问题**（最长不重复、最小覆盖等）
3. **固定/可变窗口大小**的问题

## 基本模板

### 可变窗口

```python
def sliding_window(arr):
    left = 0
    window = {}  # 或其他数据结构
    result = 0
    
    for right in range(len(arr)):
        # 1. 扩大窗口：加入 arr[right]
        window[arr[right]] = window.get(arr[right], 0) + 1
        
        # 2. 收缩窗口：当不满足条件时
        while not valid(window):
            # 移除 arr[left]
            window[arr[left]] -= 1
            if window[arr[left]] == 0:
                del window[arr[left]]
            left += 1
        
        # 3. 更新结果
        result = max(result, right - left + 1)
    
    return result
```

### 固定窗口

```python
def fixed_window(arr, k):
    window_sum = 0
    result = 0
    
    # 初始化窗口
    for i in range(k):
        window_sum += arr[i]
    result = window_sum
    
    # 滑动窗口
    for i in range(k, len(arr)):
        window_sum += arr[i] - arr[i - k]  # 滑动
        result = max(result, window_sum)
    
    return result
```

## 实战案例

### 案例 1：最长不含重复字符的子串

```python
def lengthOfLongestSubstring(s):
    window = {}
    left = 0
    max_len = 0
    
    for right, char in enumerate(s):
        # 扩大窗口
        window[char] = window.get(char, 0) + 1
        
        # 收缩窗口：当有重复字符时
        while window[char] > 1:
            window[s[left]] -= 1
            left += 1
        
        # 更新结果
        max_len = max(max_len, right - left + 1)
    
    return max_len
```

### 案例 2：最小覆盖子串

```python
from collections import Counter

def minWindow(s, t):
    need = Counter(t)
    window = {}
    left = 0
    valid = 0  # 已匹配的字符种类数
    start, min_len = 0, float('inf')
    
    for right, char in enumerate(s):
        # 扩大窗口
        if char in need:
            window[char] = window.get(char, 0) + 1
            if window[char] == need[char]:
                valid += 1
        
        # 收缩窗口
        while valid == len(need):
            # 更新最小长度
            if right - left + 1 < min_len:
                start = left
                min_len = right - left + 1
            
            # 移除 s[left]
            if s[left] in need:
                if window[s[left]] == need[s[left]]:
                    valid -= 1
                window[s[left]] -= 1
            left += 1
    
    return s[start:start + min_len] if min_len != float('inf') else ""
```

### 案例 3：固定长度子数组的最大和

```python
def maxSubarraySum(arr, k):
    window_sum = sum(arr[:k])
    max_sum = window_sum
    
    for i in range(k, len(arr)):
        # 滑出左边，滑入右边
        window_sum += arr[i] - arr[i - k]
        max_sum = max(max_sum, window_sum)
    
    return max_sum
```

## 解题步骤

1. **确定窗口类型**
   - 固定窗口：窗口大小已知
   - 可变窗口：窗口大小动态变化

2. **初始化变量**
   - `left`：左指针
   - `right`：右指针（通常用循环遍历）
   - `window`：窗口内的数据（哈希表、计数器等）
   - `result`：结果变量

3. **扩大窗口**
   - 将 `arr[right]` 加入窗口
   - 更新窗口状态

4. **收缩窗口**
   - 当窗口不满足条件时
   - 移除 `arr[left]`
   - `left++`

5. **更新结果**
   - 在合适的位置更新答案

## 窗口类型

### 1. 固定窗口

窗口大小固定为 k。

**特点：**
- 简单的滑动
- 不需要收缩逻辑

**示例：**
- 长度为 k 的子数组最大和
- 长度为 k 的子串

### 2. 可变窗口（求最大）

找满足条件的最长子数组/子串。

**特点：**
- 先扩大窗口（right++）
- 当不满足条件时收缩（left++）
- 在满足条件时更新结果

**示例：**
- 最长不重复子串
- 最长连续子数组

### 3. 可变窗口（求最小）

找满足条件的最短子数组/子串。

**特点：**
- 先扩大窗口
- 当满足条件时收缩并更新结果
- 继续扩大寻找下一个满足条件的窗口

**示例：**
- 最小覆盖子串
- 长度最小的子数组

## 常见变体

### 变体 1：至多 K 个不同元素

```python
def lengthOfLongestSubstringKDistinct(s, k):
    window = {}
    left = 0
    max_len = 0
    
    for right, char in enumerate(s):
        window[char] = window.get(char, 0) + 1
        
        # 窗口内不同字符超过 k 个
        while len(window) > k:
            window[s[left]] -= 1
            if window[s[left]] == 0:
                del window[s[left]]
            left += 1
        
        max_len = max(max_len, right - left + 1)
    
    return max_len
```

### 变体 2：恰好 K 个不同元素

技巧：至多 K 个 - 至多 K-1 个

```python
def exactly_k_distinct(s, k):
    return at_most_k(s, k) - at_most_k(s, k - 1)
```

## 时间与空间复杂度

- **时间复杂度**：O(n)，每个元素最多被访问两次（left 和 right）
- **空间复杂度**：O(k)，k 是窗口内不同元素的数量

## 滑动窗口 vs 双指针

| 特性 | 滑动窗口 | 一般双指针 |
|------|----------|-----------|
| 方向 | 同向移动 | 可对撞 |
| 窗口 | 维护连续区间 | 不一定连续 |
| 应用 | 子数组/子串 | 配对、去重 |

## 相关知识点

- [数组](../topics/array.md)
- [字符串](../topics/string.md)
- [双指针](two_pointers.md)
- [哈希表](../topics/hash_table.md)

## 练习题目

**简单：**
- 长度为 K 的子数组最大和

**中等：**
- 无重复字符的最长子串
- 找到字符串中所有字母异位词
- 水果成篮

**困难：**
- 最小覆盖子串
- 滑动窗口最大值

## 要点总结

- ✅ 滑动窗口 = 特殊的双指针
- ✅ 适合连续子数组/子串问题
- ✅ 时间复杂度 O(n)，高效
- ✅ 关键是确定窗口何时扩大、何时收缩
- ✅ 使用哈希表维护窗口状态
