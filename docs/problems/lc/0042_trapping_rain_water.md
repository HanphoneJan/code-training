---
title: 接雨水
platform: LeetCode
difficulty: 困难
id: 42
url: https://leetcode.cn/problems/trapping-rain-water/
tags:
  - 数组
  - 双指针
  - 动态规划
  - 单调栈
topics:
  - ../../topics/array.md
  - ../../topics/dynamic_programming.md
  - ../../topics/stack_queue_heap_unionfind.md
patterns:
  - ../../patterns/two_pointers.md
date_added: 2026-03-20
date_reviewed: []
---

# 42. 接雨水

## 题目描述

给定 `n` 个非负整数表示每个宽度为 `1` 的柱子的高度图，计算按此排列的柱子，下雨之后能接多少雨水。

**示例 1：**
```
输入：height = [0,1,0,2,1,0,1,3,2,1,2,1]
输出：6
```

**示例 2：**
```
输入：height = [4,2,0,3,2,5]
输出：9
```

**提示：**
- `n == height.length`
- `1 <= n <= 2 * 10^4`
- `0 <= height[i] <= 10^5`

---

## 解题思路

### 第一步：理解问题本质

接雨水问题的核心在于：**某个位置能接多少水，取决于它左边最高的柱子和右边最高的柱子**。

具体来说，对于下标 `i` 的位置：
- 设左侧最大高度为 `left_max`，右侧最大高度为 `right_max`
- 该位置能"蓄住"水的高度上限是 `min(left_max, right_max)`（木桶效应，取决于较矮的那侧）
- 减去柱子本身的高度 `height[i]`，就是该位置实际存水量

$$\text{water}[i] = \max(0,\ \min(\text{left\_max}[i],\ \text{right\_max}[i]) - \text{height}[i])$$

把每个位置的存水量加起来，就是总存水量。

---

### 第二步：暴力解法

对每个位置 `i`，分别向左和向右扫描，找出左侧最大高度和右侧最大高度，然后计算该位置的存水量。

```python
class Solution:
    def trap(self, height: List[int]) -> int:
        n = len(height)
        ans = 0
        for i in range(n):
            left_max = max(height[:i+1])   # 左侧（含自身）最大值
            right_max = max(height[i:])    # 右侧（含自身）最大值
            ans += min(left_max, right_max) - height[i]
        return ans
```

- 时间复杂度：O(n²)（外层循环 n 次，每次内层求最大值需 O(n)）
- 空间复杂度：O(1)

**为什么不够好**：对于长度 2×10^4 的数组，O(n²) 需要执行约 4×10^8 次操作，会超时。每个位置都重新扫描一遍左右两侧，做了大量重复计算。

---

### 第三步：优化解法（预处理数组）

暴力解法的瓶颈是"重复求最大值"。可以提前用两次遍历，把每个位置的左侧最大值和右侧最大值全部算好，存到两个数组里。

```python
class Solution:
    def trap(self, height: List[int]) -> int:
        n = len(height)
        pre_max = [0] * n   # pre_max[i] = height[0..i] 的最大值
        suf_max = [0] * n   # suf_max[i] = height[i..n-1] 的最大值

        # 从左到右，计算每个位置的前缀最大值
        pre_max[0] = height[0]
        for i in range(1, n):
            pre_max[i] = max(pre_max[i-1], height[i])

        # 从右到左，计算每个位置的后缀最大值
        suf_max[n-1] = height[n-1]
        for i in range(n-2, -1, -1):
            suf_max[i] = max(suf_max[i+1], height[i])

        # 计算每个位置的存水量
        ans = 0
        for i in range(n):
            ans += min(pre_max[i], suf_max[i]) - height[i]
        return ans
```

- 时间复杂度：O(n)（三次线性遍历）
- 空间复杂度：O(n)（两个辅助数组）

这已经满足时间要求，但用了额外的 O(n) 空间。能否进一步把空间也优化到 O(1)？

---

### 第四步：最优解法（相向双指针）

**核心洞察**：不需要提前把所有位置的左右最大值全部算出来，只需要在移动过程中实时维护"当前已知的左侧最大值"和"当前已知的右侧最大值"。

设两个指针 `left` 和 `right` 分别从左右两端向中间移动，同时维护：
- `pre_max`：`left` 指针走过的所有位置中的最大高度（左侧墙）
- `suf_max`：`right` 指针走过的所有位置中的最大高度（右侧墙）

**关键判断**：当 `pre_max < suf_max` 时，可以安全地计算 `left` 位置的存水量。

为什么？因为 `left` 位置的真实右侧最大值一定 `>= suf_max`（右指针还没走到的部分可能更高），而 `suf_max > pre_max`，所以真实右侧最大值也一定大于 `pre_max`。因此 `left` 位置的存水量由 `pre_max` 决定（较矮的左侧墙是瓶颈），可以直接计算：`pre_max - height[left]`。

对称地，当 `pre_max >= suf_max` 时，`right` 位置的存水量由 `suf_max` 决定，计算 `suf_max - height[right]`。

```python
class Solution:
    def trap(self, height: List[int]) -> int:
        ans = pre_max = suf_max = 0
        left, right = 0, len(height) - 1
        while left < right:
            pre_max = max(pre_max, height[left])
            suf_max = max(suf_max, height[right])
            if pre_max < suf_max:
                ans += pre_max - height[left]
                left += 1
            else:
                ans += suf_max - height[right]
                right -= 1
        return ans
```

- 时间复杂度：O(n)
- 空间复杂度：O(1)

---

## 完整代码实现

```python
from typing import List

class Solution:
    def trap(self, height: List[int]) -> int:
        ans = pre_max = suf_max = 0
        left, right = 0, len(height) - 1

        while left < right:
            # 更新左侧已走过范围的最大高度
            pre_max = max(pre_max, height[left])
            # 更新右侧已走过范围的最大高度
            suf_max = max(suf_max, height[right])

            if pre_max < suf_max:
                # 左侧是瓶颈，left 处的积水量由 pre_max 决定
                ans += pre_max - height[left]
                left += 1
            else:
                # 右侧是瓶颈，right 处的积水量由 suf_max 决定
                ans += suf_max - height[right]
                right -= 1

        return ans
```

---

## 示例推演

以 `height = [4, 2, 0, 3, 2, 5]` 为例，逐步展示双指针的执行过程。

初始状态：
- `left = 0`，`right = 5`
- `pre_max = 0`，`suf_max = 0`
- `ans = 0`

---

**第 1 轮：left=0, right=5**

- 更新：`pre_max = max(0, height[0]) = max(0, 4) = 4`
- 更新：`suf_max = max(0, height[5]) = max(0, 5) = 5`
- 判断：`pre_max(4) < suf_max(5)`，左侧是瓶颈
- 计算 left=0 处积水：`4 - height[0] = 4 - 4 = 0`（柱子本身高度等于左侧最大，无积水）
- `ans = 0`，`left` 移动到 1

---

**第 2 轮：left=1, right=5**

- 更新：`pre_max = max(4, height[1]) = max(4, 2) = 4`
- 更新：`suf_max = max(5, height[5]) = max(5, 5) = 5`
- 判断：`pre_max(4) < suf_max(5)`，左侧是瓶颈
- 计算 left=1 处积水：`4 - height[1] = 4 - 2 = 2`
- `ans = 2`，`left` 移动到 2

---

**第 3 轮：left=2, right=5**

- 更新：`pre_max = max(4, height[2]) = max(4, 0) = 4`
- 更新：`suf_max = max(5, height[5]) = max(5, 5) = 5`
- 判断：`pre_max(4) < suf_max(5)`，左侧是瓶颈
- 计算 left=2 处积水：`4 - height[2] = 4 - 0 = 4`
- `ans = 6`，`left` 移动到 3

---

**第 4 轮：left=3, right=5**

- 更新：`pre_max = max(4, height[3]) = max(4, 3) = 4`
- 更新：`suf_max = max(5, height[5]) = max(5, 5) = 5`
- 判断：`pre_max(4) < suf_max(5)`，左侧是瓶颈
- 计算 left=3 处积水：`4 - height[3] = 4 - 3 = 1`
- `ans = 7`，`left` 移动到 4

---

**第 5 轮：left=4, right=5**

- 更新：`pre_max = max(4, height[4]) = max(4, 2) = 4`
- 更新：`suf_max = max(5, height[5]) = max(5, 5) = 5`
- 判断：`pre_max(4) < suf_max(5)`，左侧是瓶颈
- 计算 left=4 处积水：`4 - height[4] = 4 - 2 = 2`
- `ans = 9`，`left` 移动到 5

---

**第 6 轮：left=5 == right=5，循环结束**

最终 `ans = 9`，与预期输出一致。

**各位置积水量汇总**：

| 下标 | 高度 | 左侧最大 | 右侧最大 | min | 积水量 |
|------|------|---------|---------|-----|--------|
| 0    | 4    | 4       | 5       | 4   | 0      |
| 1    | 2    | 4       | 5       | 4   | 2      |
| 2    | 0    | 4       | 5       | 4   | 4      |
| 3    | 3    | 4       | 5       | 4   | 1      |
| 4    | 2    | 4       | 5       | 4   | 2      |
| 5    | 5    | 5       | 5       | 5   | 0      |

总积水量 = 0 + 2 + 4 + 1 + 2 + 0 = **9**

---

## 复杂度分析

| 解法 | 时间复杂度 | 空间复杂度 | 说明 |
|------|-----------|-----------|------|
| 暴力 | O(n²) | O(1) | 每个位置都重新扫描左右两侧，大量重复计算 |
| 预处理数组 | O(n) | O(n) | 三次线性遍历，用两个数组缓存左右最大值 |
| 相向双指针 | O(n) | O(1) | 一次遍历，实时维护左右最大值，无额外空间 |

---

## 易错点总结

1. **pre_max 和 suf_max 的更新时机**：一定要在判断之前先更新两个最大值，这样 `pre_max` 包含了当前 `left` 位置本身，`suf_max` 包含了当前 `right` 位置本身。若顺序颠倒，会漏掉当前位置对最大值的贡献。

2. **积水量可能为负的担忧**：`pre_max - height[left]` 不会为负。因为 `pre_max` 是 `height[0..left]` 的最大值，必然 `>= height[left]`，所以差值 `>= 0`。

3. **为什么 left < right 而不是 left <= right**：当 `left == right` 时两个指针指向同一个位置，这个位置同时被 `pre_max` 和 `suf_max` 统计，不需要计算积水（或者说，积水量恰好为 0，因为 `min(pre_max, suf_max) - height[left]` 可以归入前面的计算中）。实际上循环结束时所有位置都已被处理完毕。

4. **双指针正确性的直觉**：以 `pre_max < suf_max` 为例，虽然 `right` 还没走到最右边，但无论右边还有多高的柱子，`pre_max` 已经确定是左侧瓶颈。因此 `left` 处积水量的计算结果是确定的，不受右侧未知部分影响。

---

## 扩展思考

**相关题目**：
- LeetCode 11：盛最多水的容器（同样用双指针，但不考虑中间柱子）
- LeetCode 84：柱状图中最大的矩形（单调栈经典题，与接雨水互为"镜像"问题）

**单调栈解法**：本题还有一种单调栈解法，思路是按"横向"而非"纵向"计算积水量——维护一个单调递减栈，每当遇到比栈顶更高的柱子时，弹出栈顶并计算一层横向的积水面积。时间和空间复杂度均为 O(n)，但代码略复杂，适合进一步挑战。

**算法本质**：相向双指针能成立的根本原因在于，两个指针同时向中间收缩，每次移动"较矮一侧"的指针。较矮一侧的最大值已经确定是瓶颈，不需要等另一侧的信息就能安全计算，这种"确定性"让我们可以用 O(1) 的空间替代 O(n) 的预处理数组。
