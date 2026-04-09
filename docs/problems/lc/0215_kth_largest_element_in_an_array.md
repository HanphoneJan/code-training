---
title: 数组中的第K个最大元素
platform: LeetCode
difficulty: Medium
id: 215
url: https://leetcode.cn/problems/kth-largest-element-in-an-array/
tags:
  - 数组
  - 分治
  - 快速选择
  - 排序
  - 堆（优先队列）
topics:
  - ../../topics/quickselect.md
  - ../../topics/heap.md
patterns:
  - ../../patterns/divide-and-conquer.md
date_added: 2026-04-09
date_reviewed: []
---

# 215. 数组中的第K个最大元素

## 题目描述

给定整数数组 `nums` 和整数 `k`，请返回数组中第 `k` 个最大的元素。

请注意，你需要找的是数组排序后的第 `k` 个最大的元素，而不是第 `k` 个不同的元素。

## 示例

**示例 1：**
```
输入: [3,2,1,5,6,4], k = 2
输出: 5
```

**示例 2：**
```
输入: [3,2,3,1,2,4,5,5,6], k = 4
输出: 4
```

---

## 解题思路

### 第一步：理解问题本质

第 k 大元素 = 升序排序后下标为 `n-k` 的元素。

例如：`[1,2,3,4,5]`，第 2 大 = 4，升序下标为 `5-2=3`。

### 第二步：暴力解法 - 完全排序

```python
def findKthLargest(self, nums: List[int], k: int) -> int:
    nums.sort()
    return nums[len(nums) - k]
```

**为什么不够好**：时间复杂度 O(n log n)，没有利用"只需要第 k 大"这个信息。

### 第三步：优化解法 - 最小堆

维护一个大小为 k 的最小堆，堆顶就是第 k 大的元素。

```python
def findKthLargest(self, nums: List[int], k: int) -> int:
    min_heap = []
    for num in nums:
        heapq.heappush(min_heap, num)
        if len(min_heap) > k:
            heapq.heappop(min_heap)
    return min_heap[0]
```

**分析**：时间 O(n log k)，空间 O(k)。

### 第四步：最优解法 - 快速选择

快速排序的变种，平均 O(n) 时间找到第 k 大元素。

---

## 完整代码实现

```python
from typing import List
from random import randint

class Solution:
    """
    数组中的第K个最大元素 - 快速选择算法

    核心思路：
    快速选择算法是快速排序的变种，利用 partition 操作在平均 O(n) 时间内找到第 k 大元素。

    时间复杂度：平均 O(n)，最坏 O(n²)
    空间复杂度：O(1)
    """

    def partition(self, nums: List[int], left: int, right: int) -> int:
        """划分函数，返回 pivot 的最终位置"""
        # 随机选择 pivot
        i = randint(left, right)
        pivot = nums[i]
        nums[i], nums[left] = nums[left], nums[i]

        # 双指针划分
        i, j = left + 1, right
        while True:
            while i <= j and nums[i] < pivot:
                i += 1
            while i <= j and nums[j] > pivot:
                j -= 1
            if i >= j:
                break
            nums[i], nums[j] = nums[j], nums[i]
            i += 1
            j -= 1

        nums[left], nums[j] = nums[j], nums[left]
        return j

    def findKthLargest(self, nums: List[int], k: int) -> int:
        n = len(nums)
        target_index = n - k  # 第 k 大在升序中的下标
        left, right = 0, n - 1

        while True:
            i = self.partition(nums, left, right)
            if i == target_index:
                return nums[i]
            if i > target_index:
                right = i - 1
            else:
                left = i + 1
```

---

## 示例推演

以 `nums = [3,2,1,5,6,4], k = 2` 为例：

**目标**：找第 2 大 = 升序下标 `6-2=4` 的元素。

**第1轮 partition**（假设 pivot = 4）：
```
初始: [3,2,1,5,6,4]
交换 pivot 到首位: [4,2,1,5,6,3]
划分后: [3,2,1,4,6,5]
pivot 位置: 3
```

`3 < 4`（target_index），在右半部分继续。

**第2轮 partition**（在 [6,5] 中，假设 pivot = 6）：
```
[6,5] -> 划分后 [5,6]
pivot 位置: 5（相对于原数组是 5）
```

`5 == 4`？不对，相对于当前子数组。实际位置是 5，大于 4，在左半部分。

**第3轮 partition**（在 [5] 中）：
```
pivot = 5，位置: 4
```

`4 == 4`，找到！返回 `nums[4] = 5`。

---

## 复杂度分析

| 解法 | 时间复杂度 | 空间复杂度 | 说明 |
|------|-----------|-----------|------|
| 完全排序 | O(n log n) | O(1) 或 O(n) | 取决于排序算法 |
| 最小堆 | O(n log k) | O(k) | 适合 k 较小的情况 |
| 快速选择 | 平均 O(n)，最坏 O(n²) | O(1) | 最优解法 |

**快速选择平均 O(n) 的证明**：

T(n) = n + n/2 + n/4 + ... = 2n = O(n)

---

## 易错点总结

### 1. target_index 计算

**错误**：`target_index = k - 1`

**正确**：`target_index = n - k`（第 k 大 = 升序下标 n-k）

### 2. partition 后的判断

```python
if i == target_index:
    return nums[i]
if i > target_index:  # 注意是 > 不是 <
    right = i - 1
else:
    left = i + 1
```

### 3. 随机 pivot 的重要性

如果不随机选择 pivot，在已排序数组上会退化到 O(n²)。

---

## 扩展思考

### 1. 找中位数

k = n/2，本题特例。

### 2. 找前 k 大元素

[347. 前 K 个高频元素](https://leetcode.cn/problems/top-k-frequent-elements/)，类似思路。

### 3. 相关题目

- [215. 数组中的第K个最大元素](https://leetcode.cn/problems/kth-largest-element-in-an-array/)
- [347. 前 K 个高频元素](https://leetcode.cn/problems/top-k-frequent-elements/)
- [414. 第三大的数](https://leetcode.cn/problems/third-maximum-number/)
- [703. 数据流中的第 K 大元素](https://leetcode.cn/problems/kth-largest-element-in-a-stream/)

---

## 相关题目

- [347. 前 K 个高频元素](https://leetcode.cn/problems/top-k-frequent-elements/)
- [414. 第三大的数](https://leetcode.cn/problems/third-maximum-number/)
- [703. 数据流中的第 K 大元素](https://leetcode.cn/problems/kth-largest-element-in-a-stream/)
- [973. 最接近原点的 K 个点](https://leetcode.cn/problems/k-closest-points-to-origin/)
