---
title: 柱状图中最大的矩形
platform: LeetCode
difficulty: Hard
id: 84
url: https://leetcode.cn/problems/largest-rectangle-in-histogram/
tags:
  - 数组
  - 栈
  - 单调栈
date_added: 2026-03-25
---

# 84. 柱状图中最大的矩形

## 题目描述

给定 n 个非负整数，用来表示柱状图中各个柱子的高度。每个柱子彼此相邻，且宽度为 1 。

求在该柱状图中，能够勾勒出来的矩形的最大面积。

## 示例

**示例 1：**
```
输入：heights = [2,1,5,6,2,3]
输出：10
解释：最大的矩形为图中红色区域，面积为 10
```

**示例 2：**
```
输入：heights = [2,4]
输出：4
```

---

## 解题思路

### 第一步：理解问题本质

对于每个柱子 `heights[i]`，如果能知道：
- 左侧第一个比它矮的位置 `left[i]`
- 右侧第一个比它矮的位置 `right[i]`

那么以 `heights[i]` 为高的最大矩形宽度就是 `right[i] - left[i] - 1`。

### 第二步：最优解法 —— 单调栈

**核心洞察**：
- 使用单调递增栈，栈中存储柱子的索引
- 当遇到比栈顶矮的柱子时，栈顶柱子的右边界就确定了
- 使用哨兵简化边界处理

---

## 完整代码实现

```python
from typing import List

class Solution:
    """
    柱状图中最大的矩形 - 单调栈

    核心思想：
    对于每个柱子 heights[i]，如果能快速知道左侧第一个比它矮的位置 left[i]
    和右侧第一个比它矮的位置 right[i]，那么以 heights[i] 为高的最大矩形宽度
    就是 right[i] - left[i] - 1。

    单调栈的作用：
    维护一个单调递增的栈，栈中存储柱子的索引。
    当遇到比栈顶矮的柱子时，栈顶柱子的右边界就确定了。

    哨兵技巧：
    在数组首尾添加高度为0的哨兵，确保所有柱子都能被处理，且栈永不为空。

    与接雨水的区别：
    - 接雨水找两边第一个比它高的，用递减栈
    - 最大矩形找两边第一个比它矮的，用递增栈

    时间复杂度：O(n)
    空间复杂度：O(n)
    """

    def largestRectangleArea(self, heights: List[int]) -> int:
        # 首尾加哨兵0，确保所有柱子都能被处理，且栈永不为空
        heights = [0] + heights + [0]
        stack = []
        max_area = 0

        for i in range(len(heights)):
            # 当前柱子比栈顶矮，栈顶柱子的右边界确定
            while stack and heights[stack[-1]] > heights[i]:
                h = heights[stack.pop()]  # 栈顶柱子的高度
                # 此时栈顶是左边第一个小于h的柱子索引
                width = i - stack[-1] - 1
                max_area = max(max_area, h * width)
            stack.append(i)

        return max_area
```

---

## 复杂度分析

| 解法 | 时间复杂度 | 空间复杂度 |
|------|-----------|-----------|
| 暴力 | O(n²) | O(1) |
| **单调栈（最优）** | **O(n)** | **O(n)** |

---

## 相关题目

- [42. 接雨水](https://leetcode.cn/problems/trapping-rain-water/)
