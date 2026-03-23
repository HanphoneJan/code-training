---
title: 跳跃游戏 II
platform: LeetCode
difficulty: 中等
id: 45
url: https://leetcode.cn/problems/jump-game-ii/
tags:
  - 贪心
  - 数组
topics:
  - ../../topics/array.md
  - ../../topics/greedy.md
patterns:
  - ../../patterns/greedy_range.md
date_added: 2026-03-23
date_reviewed: []
---

# 0045. 跳跃游戏 II

## 题目描述

给定一个长度为 `n` 的 **0 索引**整数数组 `nums`。初始位置为 `nums[0]`。

每个元素 `nums[i]` 表示从索引 `i` 向前跳转的最大长度。换句话说，如果你在 `nums[i]` 处，你可以跳转到任意 `nums[i + j]` 处:

- `0 <= j <= nums[i]`
- `i + j < n`

返回到达 `nums[n - 1]` 的最小跳跃次数。题目保证可以到达 `nums[n - 1]`。

## 示例

**示例 1：**
```
输入: nums = [2,3,1,1,4]
输出: 2
解释: 跳到最后一个位置的最小跳跃数是 2。
     从下标为 0 跳到下标为 1 的位置，跳 1 步，然后跳 3 步到达最后一个位置。
```

**示例 2：**
```
输入: nums = [2,3,0,1,4]
输出: 2
```

---

## 解题思路

### 第一步：理解问题本质

关键信息：
1. 可以跳 1 到 `nums[i]` 的任意长度
2. 要求**最少**跳跃次数
3. 题目保证一定能到达终点

这不是简单的"能不能到达"，而是"怎样跳次数最少"。

### 第二步：暴力解法——DFS/BFS

**BFS思路**：
- 把每个位置看作一个节点
- 从位置 i 可以到达 `[i+1, i+nums[i]]` 范围内的所有位置
- 用BFS找最短路径

```python
from collections import deque

def jump(nums):
    n = len(nums)
    if n <= 1:
        return 0

    queue = deque([(0, 0)])  # (位置, 步数)
    visited = [False] * n
    visited[0] = True

    while queue:
        pos, steps = queue.popleft()
        # 尝试所有可能的跳跃
        for next_pos in range(pos + 1, min(pos + nums[pos] + 1, n)):
            if next_pos == n - 1:
                return steps + 1
            if not visited[next_pos]:
                visited[next_pos] = True
                queue.append((next_pos, steps + 1))
    return -1
```

时间复杂度：O(n²) - 每个位置可能扩展 O(n) 个位置

### 第三步：贪心解法

**核心思想**：
每一步都选择"能跳最远"的那个位置作为下一跳的起点。

**关键变量**：
- `current_end`：当前这一步能到达的最远位置
- `farthest`：从当前范围出发，下一步能到达的最远位置

**算法流程**：
1. 遍历数组，维护 `farthest`（下一步能到达的最远位置）
2. 当到达 `current_end` 时，必须跳一步
3. 更新 `current_end = farthest`，继续

---

## 完整代码实现

```python
from typing import List

class Solution:
    def jump(self, nums: List[int]) -> int:
        """
        跳跃游戏 II - 贪心算法

        核心思想：每一步都跳到能覆盖最远范围的位置
        """
        n = len(nums)
        if n <= 1:
            return 0

        ans = 0           # 跳跃次数
        current_end = 0   # 当前这一步能到达的最远位置
        farthest = 0      # 下一步能到达的最远位置

        for i in range(n - 1):  # 不需要遍历到最后一个位置
            # 更新下一步能到达的最远位置
            farthest = max(farthest, i + nums[i])

            # 到达当前步数的边界，必须跳一步
            if i == current_end:
                ans += 1
                current_end = farthest  # 更新当前步数的边界

        return ans
```

---

## 示例推演

**示例**：`nums = [2,3,1,1,4]`

**初始化**：
- `ans = 0`, `current_end = 0`, `farthest = 0`

**遍历过程**：

| i | nums[i] | farthest (max) | i == current_end? | 操作 | ans | current_end |
|---|---------|----------------|-------------------|------|-----|-------------|
| 0 | 2 | max(0, 0+2) = 2 | 0 == 0 ✓ | ans=1, cur=2 | 1 | 2 |
| 1 | 3 | max(2, 1+3) = 4 | 1 == 2 ✗ | - | 1 | 2 |
| 2 | 1 | max(4, 2+1) = 4 | 2 == 2 ✓ | ans=2, cur=4 | 2 | 4 |
| 3 | 1 | max(4, 3+1) = 4 | 3 == 4 ✗ | - | 2 | 4 |

**结果**：`ans = 2`

**为什么遍历到 n-1 而不是 n？**
因为最后一个位置是终点，到达它就不需要再跳了。

---

## 复杂度分析

| 解法 | 时间复杂度 | 空间复杂度 | 说明 |
|------|-----------|-----------|------|
| BFS | O(n²) | O(n) | 最坏情况每个位置扩展 n 次 |
| 贪心 | O(n) | O(1) | **最优解**，一次遍历 |

---

## 易错点总结

### 1. 遍历范围

```python
for i in range(n - 1):  # 不是 range(n)
```
当到达最后一个位置时已经完成任务，不需要再处理。

### 2. 更新顺序

```python
farthest = max(farthest, i + nums[i])  # 先更新 farthest
if i == current_end:                    # 再判断是否到达边界
    ans += 1
    current_end = farthest
```
顺序不能错，先更新下一步能到达的最远位置，再判断是否需要跳跃。

### 3. 初始条件

```python
if n <= 1:
    return 0
```
只有一个位置时，不需要跳跃。

### 4. 理解 current_end 和 farthest

- `current_end`：当前这一步"预算"能到达的最远位置
- `farthest`：从起点到当前位置的所有选择中，下一步能到达的最远位置

---

## 扩展思考

### 1. 如果要求输出具体的路径？

需要记录每个位置的"前驱"，回溯得到路径。

### 2. 如果改为"最多能跳多远"？

这就是 [55. 跳跃游戏]，只需要判断 `max_reach >= n-1`。

### 3. 贪心算法的正确性证明

核心思想：
- 在当前可达范围内，选择能跳最远的位置作为下一跳
- 这样保证每一步都"不浪费"覆盖范围
- 最终得到的跳跃次数一定是最少的

---

## 相关题目

- [55. 跳跃游戏](https://leetcode.cn/problems/jump-game/)
- [1306. 跳跃游戏 III](https://leetcode.cn/problems/jump-game-iii/)
- [1345. 跳跃游戏 IV](https://leetcode.cn/problems/jump-game-iv/)
