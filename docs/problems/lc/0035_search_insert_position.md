---
title: 搜索插入位置
platform: LeetCode
difficulty: Easy
id: 35
url: https://leetcode.cn/problems/search-insert-position/
tags:
  - 数组
  - 二分查找
date_added: 2026-03-25
---

# 35. 搜索插入位置

## 题目描述

给定一个排序数组和一个目标值，在数组中找到目标值，并返回其索引。如果目标值不存在于数组中，返回它将会被按顺序插入的位置。

请必须使用时间复杂度为 `O(log n)` 的算法。

## 示例

**示例 1：**
```
输入：nums = [1,3,5,6], target = 5
输出：2
```

**示例 2：**
```
输入：nums = [1,3,5,6], target = 2
输出：1
```

**示例 3：**
```
输入：nums = [1,3,5,6], target = 7
输出：4
```

---

## 解题思路

### 第一步：理解问题本质

这是一个二分查找的变体问题。需要找到：
1. 如果 target 存在，返回其索引
2. 如果 target 不存在，返回它应该被插入的位置（第一个大于 target 的位置）

### 第二步：暴力解法

**思路**：线性扫描数组，找到 target 或第一个大于 target 的元素。

```python
class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        for i in range(len(nums)):
            if nums[i] >= target:
                return i
        return len(nums)
```

**缺点**：时间复杂度 O(n)，不满足 O(log n) 的要求。

### 第三步：最优解法 —— 二分查找

**核心洞察**：
- 如果找到 target，返回其索引
- 如果没找到，循环结束时 `left` 指向的位置就是插入位置

**为什么返回 left？**
- 循环不变式：`nums[0..left-1] < target`，`nums[right+1..n-1] >= target`
- 当循环结束时，`left = right + 1`
- `left` 就是第一个大于等于 target 的位置

**算法步骤**：
1. 初始化 `left = 0, right = n`
2. 循环条件 `left < right`：
   - `nums[mid] >= target`：target 在左半区（或已找到），`right = mid`
   - `nums[mid] < target`：target 在右半区，`left = mid + 1`
3. 循环结束 `left == right`，返回 left

---

## 完整代码实现

```python
from typing import List

class Solution:
    """
    搜索插入位置 - 二分查找

    核心思想：
    在有序数组中找 target 的插入位置，使得插入后数组仍然有序。
    这等价于找第一个大于等于 target 的元素位置。

    二分查找的变体：
    - 如果找到 target，返回其索引
    - 如果没找到，left 指向的位置就是应该插入的位置
      （因为循环结束时，left 是第一个大于 target 的位置）

    为什么返回 left？
    循环不变式：nums[0..left-1] < target，nums[right+1..n-1] >= target
    当循环结束时，left = right + 1，left 就是插入位置

    时间复杂度：O(log n)
    空间复杂度：O(1)
    """

    def searchInsert(self, nums: List[int], target: int) -> int:
        n = len(nums)
        left, right = 0, n  # 右边界设为 n，左闭右开区间

        while left < right:  # 不使用 <=：左闭右开写法更统一，循环结束时 left == right 即为答案
            mid = left + (right - left) // 2
            if nums[mid] >= target:
                right = mid       # 收缩右边界到 mid
            else:
                left = mid + 1    # target 在右半区

        return left
```

---

## 示例推演

以 `nums = [1,3,5,6], target = 2` 为例：

| 步骤 | left | right | mid | nums[mid] | 操作 |
|------|------|-------|-----|-----------|------|
| 1 | 0 | 3 | 1 | 3 | 3 > 2，right = 0 |
| 2 | 0 | 0 | 0 | 1 | 1 < 2，left = 1 |
| 3 | 1 | 0 | - | - | left > right，结束 |

返回 `left = 1`

解释：2 应该插入到索引 1 的位置，结果数组为 `[1,2,3,5,6]`

再以 `nums = [1,3,5,6], target = 7` 为例：

| 步骤 | left | right | mid | nums[mid] | 操作 |
|------|------|-------|-----|-----------|------|
| 1 | 0 | 3 | 1 | 3 | 3 < 7，left = 2 |
| 2 | 2 | 3 | 2 | 5 | 5 < 7，left = 3 |
| 3 | 3 | 3 | 3 | 6 | 6 < 7，left = 4 |
| 4 | 4 | 3 | - | - | left > right，结束 |

返回 `left = 4`

解释：7 应该插入到数组末尾，索引为 4

---

## 复杂度分析

| 解法 | 时间复杂度 | 空间复杂度 | 说明 |
|------|-----------|-----------|------|
| 暴力 | O(n) | O(1) | 线性查找 |
| **二分查找（最优）** | **O(log n)** | **O(1)** | 满足题目要求 |

---

## 易错点总结

### 1. 循环结束时返回 left，不是 right

```python
return left  # 正确
return right # 错误
```

因为循环结束时 `left = right + 1`，`left` 才是第一个大于 target 的位置。

### 2. 注意边界条件

- `target` 比所有元素都小：返回 0
- `target` 比所有元素都大：返回 `len(nums)`
- `target` 等于某个元素：返回该元素的索引

### 3. mid 的计算

```python
mid = left + (right - left) // 2  # 防止溢出
```

---

## 扩展思考

### 1. lower_bound 和 upper_bound

- lower_bound：第一个 >= target 的位置（本题）
- upper_bound：第一个 > target 的位置

### 2. 如果数组中有重复元素？

本题返回任意一个 target 的位置都可以，如果要返回最左/最右的位置，需要修改二分查找逻辑。

---

## 相关题目

- [34. 在排序数组中查找元素的第一个和最后一个位置](https://leetcode.cn/problems/find-first-and-last-position-of-element-in-sorted-array/)
- [704. 二分查找](https://leetcode.cn/problems/binary-search/)
- [33. 搜索旋转排序数组](https://leetcode.cn/problems/search-in-rotated-sorted-array/)
