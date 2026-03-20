---
title: 盛最多水的容器
platform: LeetCode
difficulty: 中等
id: 11
url: https://leetcode.cn/problems/container-with-most-water/
tags:
  - 数组
  - 双指针
  - 贪心
topics:
  - ../../topics/array.md
patterns:
  - ../../patterns/two_pointers.md
date_added: 2026-03-20
date_reviewed: []
---

# 11. 盛最多水的容器

## 题目描述

给定一个长度为 n 的整数数组 height。有 n 条垂线，第 i 条线的两个端点是 `(i, 0)` 和 `(i, height[i])`。

找出其中的两条线，使得它们与 x 轴共同构成的容器可以容纳最多的水。返回容器可以储存的最大水量。

**注意：** 你不能倾斜容器。

**示例：**
- 输入：height = [1, 8, 6, 2, 5, 4, 8, 3, 7]，输出：49
- 输入：height = [1, 1]，输出：1

---

## 解题思路

### 第一步：理解问题本质

容器的容积由两个因素决定：
- **宽度**：两条线之间的距离，即 `right - left`
- **高度**：两条线中**较短**的那条，因为水会从短的一边溢出

所以：`容积 = (right - left) × min(height[left], height[right])`

目标：从所有可能的线对中，找出让这个乘积最大的一对。

**问题规模：** 若有 n 条线，共有 n×(n-1)/2 种选法，暴力枚举时间复杂度为 O(n²)。

### 第二步：暴力解法

枚举所有可能的线对 (i, j)，计算每种情况下的容积，取最大值。

```python
class Solution:
    def maxArea(self, height: List[int]) -> int:
        n = len(height)
        max_area = 0
        for i in range(n):
            for j in range(i + 1, n):
                width = j - i
                current_height = min(height[i], height[j])
                max_area = max(max_area, width * current_height)
        return max_area
```

**为什么不够好：**

两层循环导致时间复杂度为 O(n²)。当 n = 10000 时，需要约 5000 万次运算，会超时。我们需要找到一种方式，每次可以排除大量无效候选，把复杂度降到 O(n)。

### 第三步：最优解法——双指针（贪心思想）

**关键洞察：** 从两端开始，每次移动较短的那条线，才有可能让容积增大。

**为什么移动较短的那条线？**

假设当前左指针为 left，右指针为 right，且 `height[left] < height[right]`。

此时容积为 `(right - left) × height[left]`。

如果我们移动右指针（right 向左），宽度一定变小，而高度最多等于 `height[left]`（因为高度取两者中较小值，已经被 left 限制了）。所以移动右指针，容积只会更小或持平，绝不会变大。

因此，**移动右指针不可能找到更大的容积**，应该放弃当前右指针，改为移动左指针（left 向右），寻找更高的左边界。

这个过程就是贪心：每次丢弃"绝对无法贡献更大容积"的选项。

**双指针过程：**
1. 初始化 left = 0，right = n - 1（从两端开始，宽度最大）
2. 计算当前容积，更新最大值
3. 将较短的那条线对应的指针向中间移动一步
4. 重复直到 left >= right

```python
class Solution:
    def maxArea(self, height: List[int]) -> int:
        left = 0
        right = len(height) - 1
        max_area = 0
        while left < right:
            width = right - left
            current_height = min(height[left], height[right])
            max_area = max(max_area, width * current_height)
            if height[left] < height[right]:
                left += 1   # 左边更短，移动左指针
            else:
                right -= 1  # 右边更短（或相等），移动右指针
        return max_area
```

**为什么这样做不会漏掉最优解？**

双指针从最宽的状态开始，每次移动一步，丢弃的是"被证明不可能更优"的线对。具体来说：

- 当 `height[left] < height[right]` 时，对于当前 left，所有以它为左边界、右边界在 right 左侧的组合，宽度更小且高度不超过 `height[left]`，容积只会更小。所以这些组合全部不需要检查，直接让 left 右移。
- 反之同理。

每次操作都保证丢弃的组合不含最优解，所以最终一定能找到最优解。

---

## 完整代码实现

```python
from typing import List

class Solution:
    def maxArea(self, height: List[int]) -> int:
        left = 0
        right = len(height) - 1
        max_area = 0
        while left < right:
            width = right - left
            current_height = min(height[left], height[right])
            max_area = max(max_area, width * current_height)
            if height[left] < height[right]:
                left += 1   # 左边更短，移动左指针寻找更高的左边界
            else:
                right -= 1  # 右边更短或相等，移动右指针
        return max_area
```

---

## 示例推演

以 height = [1, 8, 6, 2, 5, 4, 8, 3, 7] 为例，期望输出 49。

```
初始：left=0, right=8, max_area=0

第1步：
  width = 8-0 = 8
  height[0]=1, height[8]=7，min=1
  面积 = 8×1 = 8，max_area=8
  height[left]=1 < height[right]=7，left 右移 → left=1

第2步：
  width = 8-1 = 7
  height[1]=8, height[8]=7，min=7
  面积 = 7×7 = 49，max_area=49
  height[left]=8 > height[right]=7，right 左移 → right=7

第3步：
  width = 7-1 = 6
  height[1]=8, height[7]=3，min=3
  面积 = 6×3 = 18，max_area=49
  height[left]=8 > height[right]=3，right 左移 → right=6

第4步：
  width = 6-1 = 5
  height[1]=8, height[6]=8，min=8
  面积 = 5×8 = 40，max_area=49
  height[left]=8 == height[right]=8，right 左移 → right=5

第5步：
  width = 5-1 = 4
  height[1]=8, height[5]=4，min=4
  面积 = 4×4 = 16，max_area=49
  height[left]=8 > height[right]=4，right 左移 → right=4

第6步：
  width = 4-1 = 3
  height[1]=8, height[4]=5，min=5
  面积 = 3×5 = 15，max_area=49
  height[left]=8 > height[right]=5，right 左移 → right=3

第7步：
  width = 3-1 = 2
  height[1]=8, height[3]=2，min=2
  面积 = 2×2 = 4，max_area=49
  height[left]=8 > height[right]=2，right 左移 → right=2

第8步：
  width = 2-1 = 1
  height[1]=8, height[2]=6，min=6
  面积 = 1×6 = 6，max_area=49
  height[left]=8 > height[right]=6，right 左移 → right=1

left=1 == right=1，循环结束

返回 max_area = 49
```

---

## 复杂度分析

| 解法 | 时间复杂度 | 空间复杂度 | 说明 |
|------|-----------|-----------|------|
| 暴力枚举 | O(n²) | O(1) | 两层循环枚举所有线对 |
| 双指针 | O(n) | O(1) | 两指针各移动至多 n 步，合计 O(n) |

---

## 易错点总结

- **高度取较小值**：容积的高度是两条线中较短的那条，不是较长的，水会从短的一侧溢出。
- **移动较短的指针**：应该移动高度较小的那侧指针。移动较高的那侧只会让宽度缩小且高度不增，一定不优。
- **相等时移动哪边都可以**：当 `height[left] == height[right]` 时，移动任意一侧都不影响正确性（两侧都可能有更高的线）。代码中用 `else` 统一处理 `>=` 的情况，移动右指针，这是正确的。
- **不要在循环内提前退出**：双指针需要遍历所有可能的情况才能保证最优，不能在找到某个"看起来大"的值后就提前停止。

---

## 扩展思考

**相关题目：**
- LeetCode 42. 接雨水：同样是竖线与水，但规则不同——此题是单个容器，接雨水是多个凹槽。接雨水的每个位置的水量由左右两侧最高线共同决定，解法更复杂。

**双指针适用场景：**

双指针常用于数组问题中，当"移动某一侧指针可以被证明绝对无益"时，就可以应用。这道题的关键是证明"移动较高侧的指针一定不会得到更大结果"，这个证明是双指针正确性的核心。

不同于暴力法需要"验证所有组合"，双指针基于贪心推理"丢弃不必要的组合"，本质上是一种有方向的搜索。
