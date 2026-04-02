---
title: 在排序数组中查找元素的第一个和最后一个位置
platform: LeetCode
difficulty: Medium
id: 34
url: https://leetcode.cn/problems/find-first-and-last-position-of-element-in-sorted-array/
tags:
  - 数组
  - 二分查找
date_added: 2026-03-25
---

# 34. 在排序数组中查找元素的第一个和最后一个位置

## 题目描述

给你一个按照非递减顺序排列的整数数组 `nums`，和一个目标值 `target`。请你找出给定目标值在数组中的开始位置和结束位置。

如果数组中不存在目标值 `target`，返回 `[-1, -1]`。

你必须设计并实现时间复杂度为 `O(log n)` 的算法解决此问题。

## 示例

**示例 1：**
```
输入：nums = [5,7,7,8,8,10], target = 8
输出：[3,4]
```

**示例 2：**
```
输入：nums = [5,7,7,8,8,10], target = 6
输出：[-1,-1]
```

**示例 3：**
```
输入：nums = [], target = 0
输出：[-1,-1]
```

---

## 解题思路

### 第一步：理解问题本质

这是一个**二分查找的变体**问题。普通的二分查找找到一个目标值就返回，但这里需要找到目标值的范围（第一个和最后一个位置）。

### 第二步：暴力解法

**思路**：先找到任意一个 target 的位置，然后向两边扩展。

```python
class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        # 找到任意一个 target
        try:
            idx = nums.index(target)
        except ValueError:
            return [-1, -1]

        # 向两边扩展
        left = right = idx
        while left > 0 and nums[left - 1] == target:
            left -= 1
        while right < len(nums) - 1 and nums[right + 1] == target:
            right += 1

        return [left, right]
```

**缺点**：
- `index()` 方法是 O(n)
- 向两边扩展最坏也是 O(n)
- 整体时间复杂度不满足 O(log n) 的要求

### 第三步：最优解法 —— 两次二分查找

**核心洞察**：
- 找左边界：当 `nums[mid] == target` 时，不立即返回，而是收缩右边界，继续向左查找
- 找右边界：当 `nums[mid] == target` 时，收缩左边界，继续向右查找

**算法步骤**：
1. 第一次二分查找：找左边界
   - `nums[mid] == target`：记录位置，继续向左找（`right = mid`）
   - `nums[mid] < target`：目标在右半区（`left = mid + 1`）
   - `nums[mid] > target`：目标在左半区（`right = mid`）

2. 第二次二分查找：找右边界
   - `nums[mid] == target`：记录位置，继续向右找（`left = mid + 1`）
   - `nums[mid] < target`：目标在右半区（`left = mid + 1`）
   - `nums[mid] > target`：目标在左半区（`right = mid`）

**为什么正确**：
- 每次找到 target 时不立即返回，而是继续向一边查找，确保找到的是最左/最右的位置
- 两次二分查找都是 O(log n)，满足题目要求

---

## 完整代码实现

```python
from typing import List

class Solution:
    """
    在排序数组中查找元素的第一个和最后一个位置 - 二分查找

    核心思想：
    排序数组中找 target 的范围，等价于找 target 的左边界和右边界。
    用两次二分查找分别定位左边界和右边界。

    找左边界的技巧：
    当 nums[mid] == target 时，不立即返回，而是收缩右边界（right = mid - 1），
    继续向左查找，看是否还有更小的索引也是 target。

    找右边界的技巧：
    当 nums[mid] == target 时，收缩左边界（left = mid + 1），
    继续向右查找，看是否还有更大的索引也是 target。

    时间复杂度：O(log n)，两次二分查找
    空间复杂度：O(1)
    """

    def searchRange(self, nums: List[int], target: int) -> List[int]:
        n = len(nums)
        result_left, result_right = -1, -1

        # 第一次二分：找左边界
        left, right = 0, n  # 左闭右开区间
        while left < right:  # 不使用 <=：左闭右开写法更统一
            mid = left + (right - left) // 2
            if nums[mid] == target:
                result_left = mid   # 记录当前位置
                right = mid         # 继续向左查找
            elif nums[mid] < target:
                left = mid + 1      # 目标在右半区
            else:
                right = mid         # 目标在左半区

        # 第二次二分：找右边界
        left, right = 0, n
        while left < right:  # 不使用 <=：左闭右开写法更统一
            mid = left + (right - left) // 2
            if nums[mid] == target:
                result_right = mid  # 记录当前位置
                left = mid + 1      # 继续向右查找
            elif nums[mid] > target:
                right = mid
            else:
                left = mid + 1

        return [result_left, result_right]
```

---

## 示例推演

以 `nums = [5,7,7,8,8,10], target = 8` 为例：

**找左边界**：

| 步骤 | left | right | mid | nums[mid] | 操作 |
|------|------|-------|-----|-----------|------|
| 1 | 0 | 5 | 2 | 7 | 7 < 8，left = 3 |
| 2 | 3 | 5 | 4 | 8 | 找到！result_left=4，继续向左，right=3 |
| 3 | 3 | 3 | 3 | 8 | 找到！result_left=3，继续向左，right=2 |
| 4 | 3 | 2 | - | - | left > right，结束 |

左边界 = 3

**找右边界**：

| 步骤 | left | right | mid | nums[mid] | 操作 |
|------|------|-------|-----|-----------|------|
| 1 | 0 | 5 | 2 | 7 | 7 < 8，left = 3 |
| 2 | 3 | 5 | 4 | 8 | 找到！result_right=4，继续向右，left=5 |
| 3 | 5 | 5 | 5 | 10 | 10 > 8，right = 4 |
| 4 | 5 | 4 | - | - | left > right，结束 |

右边界 = 4

**结果**：[3, 4]

---

## 复杂度分析

| 解法 | 时间复杂度 | 空间复杂度 | 说明 |
|------|-----------|-----------|------|
| 暴力 | O(n) | O(1) | 线性查找 |
| **两次二分（最优）** | **O(log n)** | **O(1)** | 满足题目要求 |

---

## 易错点总结

### 1. 找左边界时，找到后还要向左找

```python
if nums[mid] == target:
    result_left = mid      # 记录
    right = mid - 1        # 继续向左！
```

不要直接返回，要继续向左查找是否有更小的索引也是 target。

### 2. 两次二分查找要独立进行

不能在一次二分中同时找左右边界，因为找到目标后的搜索方向不同。

### 3. mid 的计算要防溢出

```python
mid = left + (right - left) // 2  # 正确
mid = (left + right) // 2         # 可能溢出
```

---

## 扩展思考

### 1. 如果只需要找第一个 >= target 的位置？

这就是 lower_bound，是找左边界问题的简化版。

### 2. 如果只需要找第一个 > target 的位置？

这就是 upper_bound，可以在找右边界的基础上稍作修改。

### 3. 二分查找的通用模板

```python
def binary_search(nums, target):
    left, right = 0, len(nums)  # 左闭右开区间
    while left < right:  # 不使用 <=：左闭右开写法更统一
        mid = left + (right - left) // 2
        if nums[mid] == target:
            return mid
        elif nums[mid] < target:
            left = mid + 1
        else:
            right = mid  # 收缩右边界到 mid
    return -1 if left >= len(nums) or nums[left] != target else left
```

---

## 相关题目

- [35. 搜索插入位置](https://leetcode.cn/problems/search-insert-position/)
- [33. 搜索旋转排序数组](https://leetcode.cn/problems/search-in-rotated-sorted-array/)
- [704. 二分查找](https://leetcode.cn/problems/binary-search/)
- [278. 第一个错误的版本](https://leetcode.cn/problems/first-bad-version/)
