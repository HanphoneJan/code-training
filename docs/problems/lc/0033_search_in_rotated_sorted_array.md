---
title: 搜索旋转排序数组
platform: LeetCode
difficulty: 中等
id: 33
url: https://leetcode.cn/problems/search-in-rotated-sorted-array/
tags:
  - 数组
  - 二分查找
topics:
  - ../../topics/array.md
  - ../../topics/binary_search.md
patterns: []
date_added: 2026-03-20
date_reviewed: []
---

# 0033. 搜索旋转排序数组

## 题目描述

整数数组 `nums` 按升序排列，数组中的值**互不相同**。

在传递给函数之前，`nums` 在预先未知的某个下标 `k`（`0 <= k < nums.length`）上进行了**旋转**，使数组变为 `[nums[k], nums[k+1], ..., nums[n-1], nums[0], nums[1], ..., nums[k-1]]`（下标从 0 开始计数）。例如，`[0,1,2,4,5,6,7]` 在下标 `3` 处经旋转后可能变为 `[4,5,6,7,0,1,2]`。

给你旋转后的数组 `nums` 和一个整数 `target`，如果 `nums` 中存在这个目标值 `target`，则返回它的下标，否则返回 `-1`。

你必须设计一个时间复杂度为 `O(log n)` 的算法解决此问题。

**示例 1：**
```
输入：nums = [4,5,6,7,0,1,2], target = 0
输出：4
```

**示例 2：**
```
输入：nums = [4,5,6,7,0,1,2], target = 3
输出：-1
```

**示例 3：**
```
输入：nums = [1], target = 0
输出：-1
```

---

## 解题思路

### 第一步：理解问题本质

旋转排序数组是把一段升序数组从某个位置"切断"，然后把后半段挪到前面。比如 `[0,1,2,4,5,6,7]` 在下标 3 处旋转后变成 `[4,5,6,7,0,1,2]`。

旋转后，数组**整体不再有序**，但有一个关键性质：**以任意位置 mid 为界，左半段 `[left, mid]` 或右半段 `[mid, right]` 中，必有一段是严格有序的**。

这是因为旋转点只有一个，mid 要么在旋转点左侧（左半段完整有序），要么在旋转点右侧（右半段完整有序）。

利用这个性质，我们仍然可以使用二分查找，每次缩小一半搜索范围。

### 第二步：暴力解法

直接线性扫描整个数组。

```python
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        for i in range(len(nums)):
            if nums[i] == target:
                return i
        return -1
```

**为什么不够好**：时间复杂度 O(n)，没有利用数组的有序性。题目明确要求 O(log n)，线性扫描不符合要求。

### 第三步：最优解法——改进的二分查找

**标准二分查找**的前提是数组完全有序。旋转后数组不完全有序，但每次取 mid 时，总有一侧是有序的。

**判断哪侧有序**：比较 `nums[left]` 和 `nums[mid]`：
- 若 `nums[left] <= nums[mid]`：左半段 `[left, mid]` 是有序的。
- 否则：右半段 `[mid, right]` 是有序的。

**在有序段内判断 target 是否落入**：对于有序段，可以直接比较 target 是否在范围内：
- 若 target 在有序段内：将搜索范围缩小到有序段（舍弃另一侧）。
- 若 target 不在有序段内：将搜索范围缩小到另一侧（舍弃有序段）。

**为什么每次都能缩小一半**：每次我们都能明确地排除一半元素（要么 target 在有序的左半，要么在右半），这正是二分查找的精髓。

### 第四步：边界条件处理

**左边界的判断用 `<=`**：`nums[left] <= nums[mid]` 使用 `<=` 而非 `<`，是为了处理 `left == mid` 时（数组长度为 1 或 2）的情况，此时左半段只有一个元素，仍视为有序。

**target 在有序左半段的判断**：`nums[left] <= target < nums[mid]`，两端均需覆盖 `nums[left]`（target 可能等于 left 处的值）。

---

## 完整代码实现

```python
from typing import List

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left, right = 0, len(nums) - 1

        while left <= right:
            mid = (left + right) // 2

            if nums[mid] == target:
                return mid

            if nums[left] <= nums[mid]:  # 左半段 [left, mid] 有序
                if nums[left] <= target < nums[mid]:
                    right = mid - 1      # target 在左半段内，舍弃右半
                else:
                    left = mid + 1       # target 不在左半段，搜索右半
            else:                        # 右半段 [mid, right] 有序
                if nums[mid] < target <= nums[right]:
                    left = mid + 1       # target 在右半段内，舍弃左半
                else:
                    right = mid - 1      # target 不在右半段，搜索左半

        return -1
```

---

## 示例推演

以 `nums = [4, 5, 6, 7, 0, 1, 2]`，`target = 0` 为例：

初始：`left = 0`，`right = 6`

**第一轮**：
- `mid = (0+6)//2 = 3`，`nums[3] = 7`，不等于 target=0
- 判断有序段：`nums[0]=4 <= nums[3]=7`，左半段 `[4,5,6,7]` 有序
- target=0 在 `[4, 7)` 范围内吗？`4 <= 0 < 7`？否
- target 不在左半段，搜索右半：`left = 4`

**第二轮**：`left=4`，`right=6`
- `mid = (4+6)//2 = 5`，`nums[5] = 1`，不等于 target=0
- 判断有序段：`nums[4]=0 <= nums[5]=1`，左半段 `[0,1]` 有序
- target=0 在 `[0, 1)` 范围内吗？`0 <= 0 < 1`？是
- target 在左半段，搜索左半：`right = 4`

**第三轮**：`left=4`，`right=4`
- `mid = 4`，`nums[4] = 0`，等于 target=0

**返回下标 4**，正确。

---

**再看 target 不存在的情况**：`nums = [4,5,6,7,0,1,2]`，`target = 3`

**第一轮**：`left=0`，`right=6`，`mid=3`，`nums[3]=7`
- 左半段有序，`4 <= 3 < 7`？否，搜索右半：`left=4`

**第二轮**：`left=4`，`right=6`，`mid=5`，`nums[5]=1`
- 左半段有序（`nums[4]=0 <= nums[5]=1`），`0 <= 3 < 1`？否，搜索右半：`left=6`

**第三轮**：`left=6`，`right=6`，`mid=6`，`nums[6]=2`
- 左半段有序，`2 <= 3 < 2`？否，搜索右半：`left=7`

**循环结束**（`left=7 > right=6`），返回 `-1`，正确。

---

## 复杂度分析

| 解法 | 时间复杂度 | 空间复杂度 | 说明 |
|------|-----------|-----------|------|
| 暴力线性扫描 | O(n) | O(1) | 逐个比较，未利用有序性 |
| 改进二分查找 | O(log n) | O(1) | 每轮排除一半元素 |

---

## 易错点总结

- **左半段判断用 `<=`**：`nums[left] <= nums[mid]` 用等号，因为当 `left == mid` 时，单个元素的"段"视为有序。若改为 `<`，在数组长度为 2 时可能判断错误。

- **target 在有序段的范围是半开区间**：
  - 左半段有序：`nums[left] <= target < nums[mid]`（注意右端是严格小于，因为 `nums[mid]` 已在循环开头单独判断）。
  - 右半段有序：`nums[mid] < target <= nums[right]`（左端是严格大于）。

- **不要用第二次 find rotation point 再二分**：这种思路虽然正确，但实现复杂，且实际上一次二分就能解决，无需两次。

- **题目保证元素各不相同**：本题无重复元素，所以 `nums[left] == nums[mid]` 只在 `left == mid` 时出现。LeetCode 第 81 题是有重复元素的版本，需要额外处理。

---

## 扩展思考

- **LeetCode 81. 搜索旋转排序数组 II**：数组中存在重复元素，当 `nums[left] == nums[mid]` 时无法判断哪侧有序，需要 `left++` 跳过，最坏情况退化到 O(n)。

- **LeetCode 153. 寻找旋转排序数组中的最小值**：找旋转点，也是利用"总有一侧有序"的性质。

- **算法本质**：旋转数组的二分查找，关键是打破"二分必须完全有序"的思维定势。只要每次能判断 target 在哪一侧并排除另一侧，就能实现 O(log n)。"局部有序"已经足够支撑二分决策。
