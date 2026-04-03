---
title: 最长连续序列
platform: LeetCode
difficulty: 中等
id: 128
url: https://leetcode.cn/problems/longest-consecutive-sequence/
tags:
  - 数组
  - 哈希表
  - 并查集
topics:
  - ../../topics/array.md
  - ../../topics/hash_table.md
patterns:
  - ../../patterns/hash_table.md
date_added: 2026-04-03
date_reviewed: []
---

# 0128. 最长连续序列

## 题目描述

给定一个未排序的整数数组 `nums`，找出 **数字连续的最长序列**（不要求序列元素在原数组中连续）的长度。

**示例 1：**
```
输入：nums = [100,4,200,1,3,2]
输出：4
解释：最长数字连续序列是 [1, 2, 3, 4]。它的长度为 4。
```

**示例 2：**
```
输入：nums = [0,3,7,2,5,8,4,6,0,1]
输出：9
解释：最长数字连续序列是 [0,1,2,3,4,5,6,7,8]。它的长度为 9。
```

---

## 解题思路

### 第一步：理解问题

要找的是值连续的序列，不是数组中位置连续的子数组。

比如 `[100, 4, 200, 1, 3, 2]`，数值连续的序列有 `[100]`、`[200]`、`[1, 2, 3, 4]`。

### 第二步：暴力解法

先排序，然后遍历找最长连续段：

```python
def longestConsecutive(nums):
    if not nums:
        return 0
    nums = sorted(set(nums))
    ans = 1
    cur = 1
    for i in range(1, len(nums)):
        if nums[i] == nums[i-1] + 1:
            cur += 1
            ans = max(ans, cur)
        else:
            cur = 1
    return ans
```

- 时间复杂度：`O(n log n)`（排序）
- 空间复杂度：`O(n)`（去重）

### 第三步：优化解法

题目要求 `O(n)` 时间复杂度，不能用排序。那只能通过哈希集合的 `O(1)` 查找来加速。

朴素想法：对每个数字，向右逐个查找 `num+1, num+2, ...` 是否在集合中。

```python
def longestConsecutive(nums):
    st = set(nums)
    ans = 0
    for x in st:
        y = x + 1
        while y in st:
            y += 1
        ans = max(ans, y - x)
    return ans
```

但这可能会退化到 `O(n²)`，因为如果一个数字是很多连续序列的内部元素，它会被重复计算。

### 第四步：最优解法 - 只从序列起点开始

优化：只从**序列的起点**（即 `x-1` 不在集合中的数字 `x`）开始向右扩展。

这样每个数字最多被访问两次：一次作为其他序列的内部元素被跳过，一次作为起点被遍历。

时间复杂度严格为 `O(n)`。

---

## 完整代码实现

```python
from typing import List

class Solution:
    """
    128. 最长连续序列 - 哈希表

    核心思想：
    利用哈希集合 O(1) 查找的特性，只从序列起点开始向右扩展连续序列。

    时间复杂度：O(n)
    空间复杂度：O(n)，哈希集合
    """

    def longestConsecutive(self, nums: List[int]) -> int:
        st = set(nums)
        ans = 0

        for x in st:
            if x - 1 in st:
                continue

            y = x + 1
            while y in st:
                y += 1

            ans = max(ans, y - x)

        return ans
```

---

## 示例推演

以 `nums = [100, 4, 200, 1, 3, 2]` 为例。

集合 `st = {1, 2, 3, 4, 100, 200}`

**x = 1**：`0` 不在集合中，是起点。
- `y = 2` 在， `y = 3` 在， `y = 4` 在， `y = 5` 不在
- 序列长度 = 5 - 1 = 4，`ans = 4`

**x = 2**：`1` 在集合中，跳过（不是起点）

**x = 3**：`2` 在集合中，跳过

**x = 4**：`3` 在集合中，跳过

**x = 100**：`99` 不在，是起点。
- `y = 101` 不在
- 序列长度 = 1，`ans = 4`

**x = 200**：`199` 不在，是起点。
- `y = 201` 不在
- 序列长度 = 1，`ans = 4`

最终答案：`4`

---

## 复杂度分析

| 解法 | 时间复杂度 | 空间复杂度 | 说明 |
|------|-----------|-----------|------|
| 暴力排序 | O(n log n) | O(n) | 先排序再扫描 |
| 朴素哈希 | O(n²) | O(n) | 每个数字都作为起点 |
| 优化哈希 | O(n) | O(n) | **最优解** |

---

## 易错点总结

### 1. 为什么要跳过 `x-1` 在集合中的数字？

这是最关键的一步。如果不跳过，内部元素会被重复遍历，退化为 `O(n²)`。

### 2. 序列长度的计算

`y` 最终停在第一个不在集合中的数，所以序列长度是 `y - x`，不是 `y - x + 1`。

### 3. 空数组

`nums` 为空时，集合为空，循环不执行，返回 `0`。

---

## 扩展思考

### 并查集做法

也可以把所有相邻的数字用并查集合并，最后统计每个连通块的大小。时间复杂度也是 `O(n)`，但常数较大，不推荐。

### 如果要求返回具体的序列？

只需要在遍历时记录起点和终点即可。

## 相关题目

- [217. 存在重复元素](https://leetcode.cn/problems/contains-duplicate/)
- [219. 存在重复元素 II](https://leetcode.cn/problems/contains-duplicate-ii/)
