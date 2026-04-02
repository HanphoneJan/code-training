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

---

## 解题思路

### 第一步：理解中位数的本质

中位数的核心作用：**将一个有序集合分成左右两部分，使得左半部分的所有元素 ≤ 右半部分的所有元素**。

- 如果总长为奇数：左半部分比右半部分多一个元素，中位数就是左半部分的最大值
- 如果总长为偶数：左右两部分元素个数相同，中位数是 (左半部分最大值 + 右半部分最小值) / 2

### 第二步：为什么暴力解法不够好？

**解法一：合并数组后排序**

```python
def findMedianSortedArrays(nums1, nums2):
    merged = sorted(nums1 + nums2)  # 或手动归并
    n = len(merged)
    if n % 2 == 1:
        return merged[n // 2]
    else:
        return (merged[n // 2 - 1] + merged[n // 2]) / 2
```

- 时间复杂度：O((m+n)log(m+n))，使用 sorted；如果手动归并是 O(m+n)
- 空间复杂度：O(m+n)

**问题**：没有利用"两个数组已经有序"这个条件，浪费了信息。

---

### 第三步：优化——不真合并，只找中位数

**解法二：双指针遍历**

既然数组已经有序，我们可以用双指针"虚拟合并"，只需要遍历到中位数位置即可。

```python
def findMedianSortedArrays(nums1, nums2):
    m, n = len(nums1), len(nums2)
    total = m + n

    # 需要遍历到第 target 个元素
    # 奇数：target = total // 2（第 target 个就是中位数）
    # 偶数：target = total // 2（需要第 target-1 和 target 个）
    target = total // 2

    i = j = 0          # 两个指针
    prev = curr = 0    # 保存上一个和当前的值

    for _ in range(target + 1):
        prev = curr
        # 选择较小的那个移动
        if i < m and (j >= n or nums1[i] <= nums2[j]):
            curr = nums1[i]
            i += 1
        else:
            curr = nums2[j]
            j += 1

    if total % 2 == 1:
        return curr
    else:
        return (prev + curr) / 2
```

**关键技巧**：
- 用 `prev` 和 `curr` 两个变量，奇数时返回 `curr`，偶数时返回 `(prev + curr) / 2`
- 统一处理奇偶：都遍历 `target + 1` 次，奇数时 `prev` 其实没用上

- 时间复杂度：O(m+n)，最坏情况要遍历完一个数组
- 空间复杂度：O(1)

**还能优化吗？** 题目要求 O(log(m+n))，提示我们要用二分查找。

---

### 第四步：最优解法——二分划分

**核心思想**：不逐个遍历，而是直接"切"在正确的位置。

#### 4.1 如何理解"划分"？

想象把两个数组分别切成左右两部分：

```
nums1: [1, 3, 5, | 7, 9]    在位置 i=3 切分
              ↑
            nums1[i-1]=5  nums1[i]=7

nums2: [2, 4, | 6, 8, 10]   在位置 j=2 切分
              ↑
            nums2[j-1]=4  nums2[j]=6
```

**左半部分** = `[1, 3, 5]` + `[2, 4]` = `[1, 2, 3, 4, 5]`（最大值是 5）
**右半部分** = `[7, 9]` + `[6, 8, 10]` = `[6, 7, 8, 9, 10]`（最小值是 6）

如果满足：**左半部分的最大值 ≤ 右半部分的最小值**，那么中位数就能从这个划分中算出来。

#### 4.2 划分的条件

设 `nums1` 在位置 `i` 切分（`i` 可以是 0 到 m，共 m+1 种选择），`nums2` 在位置 `j` 切分。

为了让左右两部分长度相等（或左半部分多一个）：
```
i + j = (m + n + 1) // 2   # 使用 // 是整数除法
```
这样 `j` 就被 `i` 决定了：`j = (m + n + 1) // 2 - i`

**正确的划分必须满足**：
1. `nums1[i-1] <= nums2[j]`（nums1的左 ≤ nums2的右）
2. `nums2[j-1] <= nums1[i]`（nums2的左 ≤ nums1的右）

如果满足，中位数：
- 奇数：`max(nums1[i-1], nums2[j-1])`
- 偶数：`(max(nums1[i-1], nums2[j-1]) + min(nums1[i], nums2[j])) / 2`

#### 4.3 二分查找的过程

我们要在 `nums1` 中找到正确的 `i`。由于 `nums1` 有序，可以用二分：

```
初始：left=0, right=m

每次取 i = (left + right) // 2
计算 j = (m + n + 1) // 2 - i

检查划分是否正确：
- 如果 nums1[i-1] > nums2[j]：i 太大，向左找 → right = i - 1
- 如果 nums2[j-1] > nums1[i]：i 太小，向右找 → left = i + 1
- 否则：找到了！
```

**为什么选较短的数组二分？**
- 时间复杂度是 O(log(min(m,n)))
- 避免 `j` 计算出来超出范围（如果 `nums1` 比 `nums2` 长，`i` 可能很大导致 `j` 为负数）

#### 4.4 边界情况的处理

| 情况 | 含义 | 处理方式 |
|------|------|----------|
| `i == 0` | `nums1` 全部在右边 | `nums1_left = -∞` |
| `i == m` | `nums1` 全部在左边 | `nums1_right = +∞` |
| `j == 0` | `nums2` 全部在右边 | `nums2_left = -∞` |
| `j == n` | `nums2` 全部在左边 | `nums2_right = +∞` |

使用 `±∞` 可以统一代码，避免大量 if-else。

---

## 完整代码实现

```python
from typing import List

class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        # 确保 nums1 是较短的数组，降低二分范围，同时避免 j 越界
        if len(nums1) > len(nums2):
            nums1, nums2 = nums2, nums1

        m, n = len(nums1), len(nums2)
        left, right = 0, m  # 在 nums1 的 [0, m] 范围内二分

        while left < right:  # 不使用 <=：收缩到单点时自然结束，最后统一处理边界
            # i: nums1 的划分点（切在 i 前面，即左边有 i 个元素）
            # j: nums2 的划分点
            i = (left + right) // 2
            j = (m + n + 1) // 2 - i

            # 处理边界：用无穷大/无穷小表示"不存在"
            nums1_left = float('-inf') if i == 0 else nums1[i - 1]
            nums1_right = float('inf') if i == m else nums1[i]
            nums2_left = float('-inf') if j == 0 else nums2[j - 1]
            nums2_right = float('inf') if j == n else nums2[j]

            # 检查划分是否正确
            if nums1_left <= nums2_right and nums2_left <= nums1_right:
                # 找到正确划分！计算中位数
                if (m + n) % 2 == 1:
                    # 奇数：中位数是左半部分的最大值
                    return max(nums1_left, nums2_left)
                else:
                    # 偶数：(左半部分最大值 + 右半部分最小值) / 2
                    left_max = max(nums1_left, nums2_left)
                    right_min = min(nums1_right, nums2_right)
                    return (left_max + right_min) / 2

            elif nums1_left > nums2_right:
                # nums1 的左半部分太大，i 需要减小
                right = i - 1
            else:
                # nums2 的左半部分太大，意味着 i 需要增大
                left = i + 1


        # 循环结束时 left == right，处理最后一个切割点
        i = left
        j = (m + n + 1) // 2 - i
        nums1_left = float('-inf') if i == 0 else nums1[i - 1]
        nums1_right = float('inf') if i == m else nums1[i]
        nums2_left = float('-inf') if j == 0 else nums2[j - 1]
        nums2_right = float('inf') if j == n else nums2[j]

        if (m + n) % 2 == 0:
            return (max(nums1_left, nums2_left) + min(nums1_right, nums2_right)) / 2
        else:
            return max(nums1_left, nums2_left)
        # 理论上不会执行到这里，因为题目保证有解
        raise ValueError("No solution found")
```

---

## 示例推演

**示例**：`nums1 = [1, 3]`, `nums2 = [2]`

**初始化**：
- `nums1` 较短，不需要交换。`m=2, n=1`
- `left=0, right=2`，目标 `j = (2+1+1)//2 - i = 2 - i`

**第一次迭代**：`i=1, j=1`

计算各值：
- `nums1_left = nums1[0] = 1`, `nums1_right = nums1[1] = 3`
- `nums2_left = nums2[0] = 2`, `nums2_right = +∞` (j==n)

检查划分条件：
- 条件1：`nums1_left <= nums2_right` → `1 <= +∞` ✓
- 条件2：`nums2_left <= nums1_right` → `2 <= 3` ✓

两个条件都满足，找到正确划分！

计算中位数：
- 总长=3是奇数，返回 `max(nums1_left, nums2_left) = max(1, 2) = 2` ✓

**结果**：中位数为 2，与合并数组 `[1, 2, 3]` 的中位数一致。

---

## 复杂度分析

| 解法 | 时间复杂度 | 空间复杂度 | 说明 |
|------|-----------|-----------|------|
| 暴力合并 | O((m+n)log(m+n)) | O(m+n) | 没有利用有序性 |
| 双指针 | O(m+n) | O(1) | 只遍历到中位数位置 |
| 二分划分 | O(log(min(m,n))) | O(1) | **最优解** |

---

## 易错点总结

### 1. 划分点的计算

```python
j = (m + n + 1) // 2 - i
```
使用 `(m + n + 1) // 2` 而不是 `(m + n) // 2` 是为了奇数时让左半部分多一个元素。

### 2. 边界条件的判断

注意是 `<=` 而不是 `<`，因为数组中可能有重复元素：
```python
nums1_left <= nums2_right  # 不是 <
```

### 3. 无穷边界的使用

```python
float('-inf')  # 负无穷
float('inf')   # 正无穷
```
这样可以统一处理边界，避免大量的 if-else 分支。

### 4. 确保 nums1 是较短的数组

```python
if len(nums1) > len(nums2):
    nums1, nums2 = nums2, nums1
```
这保证了 `j` 不会计算出负数，同时优化了时间复杂度。

---

## 扩展思考

### 1. 如果题目改为"找第 k 小的元素"？

可以用类似的二分思路，只是终止条件变成"左半部分有 k 个元素"。

### 2. 二分查找的本质是什么？

不只是用来"查找元素"，更是一种**划分策略**。只要问题具有单调性（满足某条件的左边都不满足，右边都满足），就可以用二分。

### 3. 为什么这道题目要求 O(log(m+n))？

这是对算法能力的考察——能否想到用二分来优化。如果允许 O(m+n)，双指针解法已经足够好。

---

## 相关题目

- [215. 数组中的第K个最大元素](https://leetcode.cn/problems/kth-largest-element-in-an-array/)
- [23. 合并K个升序链表](https://leetcode.cn/problems/merge-k-sorted-lists/)
- [33. 搜索旋转排序数组](https://leetcode.cn/problems/search-in-rotated-sorted-array/)（二分变形）
