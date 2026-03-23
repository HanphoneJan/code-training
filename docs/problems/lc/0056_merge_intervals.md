---
title: 合并区间
platform: LeetCode
difficulty: 中等
id: 56
url: https://leetcode.cn/problems/merge-intervals/
tags:
  - 数组
  - 排序
  - 贪心
topics:
  - ../../topics/array.md
  - ../../topics/sorting.md
  - ../../topics/greedy.md
patterns:
  - ../../patterns/interval_problems.md
date_added: 2026-03-23
date_reviewed: []
---

# 0056. 合并区间

## 题目描述

以数组 `intervals` 表示若干个区间的集合，其中单个区间为 `intervals[i] = [starti, endi]` 。请你合并所有重叠的区间，并返回一个不重叠的区间数组，该数组需恰好覆盖输入中的所有区间。

## 示例

**示例 1：**
```
输入：intervals = [[1,3],[2,6],[8,10],[15,18]]
输出：[[1,6],[8,10],[15,18]]
解释：区间 [1,3] 和 [2,6] 重叠, 将它们合并为 [1,6]。
```

**示例 2：**
```
输入：intervals = [[1,4],[4,5]]
输出：[[1,5]]
解释：区间 [1,4] 和 [4,5] 可被视为重叠区间。
```

---

## 解题思路

### 第一步：理解问题本质

**区间重叠的条件**：
两个区间 `[a, b]` 和 `[c, d]` 重叠，当且仅当 `c <= b` 且 `a <= d`。

简化：按左端点排序后，只需要检查 `curr[0] <= prev[1]`。

**为什么排序？**
按左端点排序后，所有可能重叠的区间都会相邻，只需线性扫描即可。

### 第二步：贪心算法

**核心思想**：
1. 按左端点排序
2. 维护一个"当前合并区间"
3. 遍历排序后的区间：
   - 如果与当前区间重叠，扩展合并区间
   - 如果不重叠，保存当前区间，开始新区间

**合并操作**：
```
[1, 3] 和 [2, 6] 重叠
合并后：[1, max(3, 6)] = [1, 6]
```

---

## 完整代码实现

```python
from typing import List

class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        """
        合并区间 - 贪心算法

        核心思想：按左端点排序，维护当前合并区间
        """
        # 按左端点排序（关键步骤）
        intervals.sort(key=lambda x: x[0])
        n = len(intervals)

        if n <= 1:
            return intervals

        merged = [intervals[0]]  # 初始化 merged 为第一个区间

        for curr in intervals[1:]:
            prev = merged[-1]  # 上一个合并后的区间

            # 检查是否重叠：当前区间的左端点 <= 上一个区间的右端点
            if curr[0] <= prev[1]:
                # 重叠，合并区间：更新右端点为两者的最大值
                prev[1] = max(prev[1], curr[1])
            else:
                # 不重叠，添加新区间
                merged.append(curr)

        return merged
```

---

## 示例推演

**示例**：`intervals = [[1,3],[2,6],[8,10],[15,18]]`

**第一步：排序**（已按左端点排序）

**遍历过程**：

| 步骤 | curr | prev | curr[0] <= prev[1]? | 操作 | merged |
|------|------|------|---------------------|------|--------|
| 初始化 | - | - | - | - | [[1,3]] |
| 1 | [2,6] | [1,3] | 2 <= 3 ✓ | 合并为 [1,6] | [[1,6]] |
| 2 | [8,10] | [1,6] | 8 <= 6 ✗ | 添加新区间 | [[1,6],[8,10]] |
| 3 | [15,18] | [8,10] | 15 <= 10 ✗ | 添加新区间 | [[1,6],[8,10],[15,18]] |

**结果**：`[[1,6],[8,10],[15,18]]`

---

## 复杂度分析

| 指标 | 复杂度 | 说明 |
|------|--------|------|
| 时间 | O(n log n) | 排序 dominates |
| 空间 | O(log n) ~ O(n) | 排序栈空间或输出数组 |

---

## 易错点总结

### 1. 排序键函数

```python
intervals.sort(key=lambda x: x[0])  # 按左端点排序
```

不要写成 `sort()`，默认按第一个元素排序也可以，但显式指定更清晰。

### 2. 合并时的右端点

```python
prev[1] = max(prev[1], curr[1])  # 不是直接赋值 curr[1]
```

例如 `[1, 5]` 和 `[2, 3]`，合并后应该是 `[1, 5]` 而不是 `[1, 3]`。

### 3. 重叠条件

```python
if curr[0] <= prev[1]:  # 不是 <
```

端点相接触也算重叠，如 `[1,4]` 和 `[4,5]` 应该合并为 `[1,5]`。

### 4. 空数组处理

```python
if n <= 1:
    return intervals
```

0 个或 1 个区间直接返回。

---

## 扩展思考

### 1. 区间插入

给定一个区间，插入到已有区间集合中并合并。可以先添加再合并，或者找到位置后合并。

### 2. 区间删除/裁剪

给定一个区间，从集合中删除该区域，返回剩余的区间。

### 3. 区间交集

求两个区间集合的交集，需要双指针遍历两个集合。

---

## 相关题目

- [57. 插入区间](https://leetcode.cn/problems/insert-interval/)
- [435. 无重叠区间](https://leetcode.cn/problems/non-overlapping-intervals/)
- [452. 用最少数量的箭引爆气球](https://leetcode.cn/problems/minimum-number-of-arrows-to-burst-balloons/)
- [253. 会议室 II](https://leetcode.cn/problems/meeting-rooms-ii/)
