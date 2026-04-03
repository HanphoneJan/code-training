---
title: 寻找旋转排序数组中的最小值
platform: LeetCode
difficulty: 中等
id: 153
url: https://leetcode.cn/problems/find-minimum-in-rotated-sorted-array/
tags:
  - 数组
  - 二分查找
topics:
  - ../../topics/array.md
  - ../../topics/binary_search.md
patterns:
  - ../../patterns/binary_search.md
date_added: 2026-04-03
date_reviewed: []
---

# 0153. 寻找旋转排序数组中的最小值

## 题目描述

已知一个长度为 `n` 的数组，预先按照升序排列，经由 `1` 到 `n` 次 **旋转** 后，得到输入数组。例如，原数组 `nums = [0,1,2,4,5,6,7]` 在变化后可能得到：
- 若旋转 `4` 次，则可以得到 `[4,5,6,7,0,1,2]`
- 若旋转 `7` 次，则可以得到 `[0,1,2,4,5,6,7]`

**注意**，数组 `[a[0], a[1], a[2], ..., a[n-1]]` **旋转一次** 的结果为数组 `[a[n-1], a[0], a[1], a[2], ..., a[n-2]]` 。

给你一个元素值 **互不相同** 的数组 `nums` ，它原来是一个升序排列的数组，并按上述情形进行了多次旋转。请你找出并返回数组中的 **最小元素** 。

你必须设计一个时间复杂度为 `O(log n)` 的算法解决此问题。

## 示例

**示例 1：**
```
输入：nums = [3,4,5,1,2]
输出：1
解释：原数组为 [1,2,3,4,5] ，旋转 3 次得到输入数组。
```

**示例 2：**
```
输入：nums = [4,5,6,7,0,1,2]
输出：0
解释：原数组为 [0,1,2,4,5,6,7] ，旋转 4 次得到输入数组。
```

**示例 3：**
```
输入：nums = [11,13,15,17]
输出：11
解释：原数组为 [11,13,15,17] ，没有旋转。
```

---

## 解题思路

### 第一步：旋转数组的特性

旋转后的数组由两段升序子数组组成：
- 左半段：都大于等于 `nums[0]`（或首元素）
- 右半段：都小于等于 `nums[-1]`（或尾元素）

最小值就是右半段的第一个元素，也就是两段的分界点。

### 第二步：暴力解法

线性扫描找最小值：

```python
def findMin(nums):
    return min(nums)
```

- 时间复杂度：`O(n)`
- 空间复杂度：`O(1)`

### 第三步：最优解法 - 二分查找

因为数组部分有序，可以用二分查找定位最小值。

关键判断：比较 `nums[mid]` 和 `nums[right]`
- 如果 `nums[mid] > nums[right]`：最小值一定在 `mid` 右侧，`left = mid + 1`
- 如果 `nums[mid] < nums[right]`：最小值在 `mid` 左侧（包括 `mid`），`right = mid`

为什么和 `right` 比较？
- 因为右半段一定是有序的或包含最小值
- 和 `right` 比较可以更快缩小范围

循环条件用 `left < right`，最终 `left == right` 时就是答案。

---

## 完整代码实现

```python
from typing import List

class Solution:
    """
    153. 寻找旋转排序数组中的最小值 - 二分查找

    核心思想：
    旋转数组由两段升序子数组组成，最小值就是分界点。
    通过比较 mid 和 right 的元素，可以判断最小值在哪一半。

    时间复杂度：O(log n)
    空间复杂度：O(1)
    """

    def findMin(self, nums: List[int]) -> int:
        left, right = 0, len(nums) - 1

        while left < right:
            mid = (left + right) // 2
            if nums[mid] > nums[right]:
                # 最小值在 mid 右侧
                left = mid + 1
            else:
                # nums[mid] < nums[right]，最小值在 mid 左侧（含 mid）
                # 本题元素互不相同，不可能相等
                right = mid

        return nums[left]
```

---

## 示例推演

以 `nums = [4, 5, 6, 7, 0, 1, 2]` 为例：

**初始**：left = 0, right = 6

**第1轮**：mid = 3, `nums[3] = 7`
- `7 > nums[6] = 2`，最小值在右侧
- left = 4

**第2轮**：mid = 5, `nums[5] = 1`
- `1 < nums[6] = 2`，最小值在左侧（含 mid）
- right = 5

**第3轮**：left = 4, right = 5, mid = 4, `nums[4] = 0`
- `0 < nums[5] = 1`
- right = 4

循环结束，left = right = 4，答案 `nums[4] = 0`。

---

## 复杂度分析

| 解法 | 时间复杂度 | 空间复杂度 | 说明 |
|------|-----------|-----------|------|
| 暴力 | O(n) | O(1) | 线性扫描 |
| 二分 | O(log n) | O(1) | **最优解** |

---

## 易错点总结

### 1. 和 right 比较 vs 和 left 比较

推荐和 `right` 比较，这样右半段有序的特性更明确。如果和 `left` 比较，需要额外处理未旋转的情况。

### 2. 循环条件

使用 `left < right` 而不是 `left <= right`。当 `left == right` 时就是答案，不需要继续循环。

### 3. 边界更新

`nums[mid] > nums[right]` 时，`left = mid + 1`（最小值不可能在 mid）。
`nums[mid] < nums[right]` 时，`right = mid`（最小值可能在 mid）。

### 4. 元素可重复的情况

这是 [154. 寻找旋转排序数组中的最小值 II](https://leetcode.cn/problems/find-minimum-in-rotated-sorted-array-ii/)，当 `nums[mid] == nums[right]` 时，无法判断，只能 `right -= 1`。

---

## 扩展思考

### 本题和 33 题的关系

[33. 搜索旋转排序数组](https://leetcode.cn/problems/search-in-rotated-sorted-array/) 是在旋转数组中查找特定元素，核心思路也是二分，但需要同时判断目标值在哪一半。

## 相关题目

- [33. 搜索旋转排序数组](https://leetcode.cn/problems/search-in-rotated-sorted-array/)
- [154. 寻找旋转排序数组中的最小值 II](https://leetcode.cn/problems/find-minimum-in-rotated-sorted-array-ii/)
- [81. 搜索旋转排序数组 II](https://leetcode.cn/problems/search-in-rotated-sorted-array-ii/)
