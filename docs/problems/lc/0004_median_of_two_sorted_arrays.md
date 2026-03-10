---
title: 寻找两个正序数组的中位数
platform: LeetCode
difficulty: 困难
id: 4
url: https://leetcode.cn/problems/median-of-two-sorted-arrays/
tags:
  - 数组
  - 二分查找
  - 分治
topics:
  - ../../topics/array.md
  - ../../topics/binary_search.md
patterns:
  - ../../patterns/binary_search.md
date_added: 2026-03-10
date_reviewed: []
---

# 0004. 寻找两个正序数组的中位数

## 题目描述

给定两个大小分别为 `m` 和 `n` 的正序（从小到大）数组 `nums1` 和 `nums2`。请你找出并返回这两个正序数组的 **中位数** 。

算法的时间复杂度应该为 `O(log(m+n))`。

## 示例

**示例 1：**
```
输入：nums1 = [1,3], nums2 = [2]
输出：2.00000
解释：合并数组 = [1,2,3] ，中位数 2
```

**示例 2：**
```
输入：nums1 = [1,2], nums2 = [3,4]
输出：2.50000
解释：合并数组 = [1,2,3,4] ，中位数 (2 + 3) / 2 = 2.5
```

## 解题思路

### 核心思想：二分查找划分

这道题的关键是理解**中位数的本质**：将一个集合划分为左右两个长度相等的部分，且左半部分的所有元素 ≤ 右半部分的所有元素。

对于两个有序数组，我们需要找到一个划分点，使得：
- 左半部分元素总数 = 右半部分（或差1）
- 左半部分的所有元素 ≤ 右半部分的所有元素

### 为什么选较短的数组进行二分？

在较短的数组上进行二分查找，可以保证：
- 时间复杂度为 O(log(min(m,n)))
- 避免在较长数组上二分时的越界问题

### 划分条件

设我们在 `nums1` 的位置 `i` 和 `nums2` 的位置 `j` 进行划分：

```
nums1: [ ..., nums1[i-1] | nums1[i], ... ]
nums2: [ ..., nums2[j-1] | nums2[j], ... ]
             左半部分    |    右半部分
```

正确的划分需要满足：
- `nums1[i-1] <= nums2[j]` （nums1的左 ≤ nums2的右）
- `nums2[j-1] <= nums1[i]` （nums2的左 ≤ nums1的右）

### 边界处理

使用 `±inf` 处理数组边界情况：
- `i == 0` 时，`nums1_left = -inf`
- `i == m` 时，`nums1_right = +inf`

### 中位数计算

- **总长为奇数**：中位数 = max(左半部分的最大值)
- **总长为偶数**：中位数 = (max(左半部分) + min(右半部分)) / 2

## 代码实现

### Python

```python
class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        # 确保 nums1 是较短的数组，降低二分范围
        if len(nums1) > len(nums2):
            nums1, nums2 = nums2, nums1

        m, n = len(nums1), len(nums2)
        left, right = 0, m

        while left <= right:
            # i: nums1 的划分点，j: nums2 的划分点
            i = (left + right) // 2
            j = (m + n + 1) // 2 - i

            nums1_left = float('-inf') if i == 0 else nums1[i - 1]
            nums1_right = float('inf') if i == m else nums1[i]
            nums2_left = float('-inf') if j == 0 else nums2[j - 1]
            nums2_right = float('inf') if j == n else nums2[j]

            # 检查划分是否正确
            if nums1_left <= nums2_right and nums2_left <= nums1_right:
                # 找到正确划分
                if (m + n) % 2 == 0:
                    return (max(nums1_left, nums2_left) + min(nums1_right, nums2_right)) / 2
                else:
                    return max(nums1_left, nums2_left)

            elif nums1_left > nums2_right:
                # nums1 的左半部分太大，向左移动
                right = i - 1
            else:
                # nums1 的左半部分太小，向右移动
                left = i + 1
```

## 复杂度分析

| 指标 | 复杂度 | 说明 |
|------|--------|------|
| 时间复杂度 | O(log(min(m,n))) | 在较短的数组上进行二分查找 |
| 空间复杂度 | O(1) | 只使用常数额外空间 |

## 易错点分析

### 1. 划分点的计算

```python
j = (m + n + 1) // 2 - i
```

使用 `(m + n + 1) // 2` 是为了在总长为奇数时，让左半部分多一个元素，这样中位数就是左半部分的最大值。

### 2. 边界条件的判断

注意是 `nums1_left <= nums2_right` 而不是 `<`，因为数组中可能有重复元素。

### 3. 无穷边界的使用

使用 `float('-inf')` 和 `float('inf')` 可以简化边界处理，避免大量的 if-else 判断。

## 相关题目

- [215. 数组中的第K个最大元素](https://leetcode.cn/problems/kth-largest-element-in-an-array/)
- [23. 合并K个升序链表](https://leetcode.cn/problems/merge-k-sorted-lists/)

## 笔记

### 为什么暴力解法不够好？

暴力解法是合并两个数组后排序，时间复杂度 O((m+n)log(m+n))，不满足题目要求的 O(log(m+n))。

### 二分的本质

二分查找不只是用来"查找元素"，更是一种**划分策略**。只要问题具有单调性（或可以构造出单调性），就可以考虑使用二分。

### 扩展思考

如果题目改为"找第 k 小的元素"，也可以用类似的二分思路，只是终止条件和中位数计算方式不同。
