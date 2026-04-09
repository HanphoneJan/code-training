---
title: N 天后的牢房
platform: LeetCode
difficulty: Medium
id: 957
url: https://leetcode.cn/problems/prison-cells-after-n-days/
tags:
  - 数组
  - 哈希表
  - 找规律
topics:
  - ../../topics/array.md
  - ../../topics/hash-table.md
patterns:
  - ../../patterns/find-cycle.md
date_added: 2026-04-09
date_reviewed: []
---

# 957. N 天后的牢房

## 题目描述

8 间牢房排成一排，每间牢房不是有人住就是空着。

每天，根据牢房前一天的状态，所有牢房的状态都会发生变化：
- 如果一间牢房的两个相邻的房间都被占用或都是空的，则该牢房变为占用
- 否则，该牢房变为空着

注意：第一个和最后一个牢房没有两个相邻的房间，它们的状态永远为 0。

给定初始状态数组 `cells` 和一个整数 `n`，返回 `n` 天后的牢房状态。

**示例 1：**
```
输入: cells = [0,1,0,1,1,0,0,1], n = 7
输出: [0,0,1,1,0,0,0,0]
解释: 下表总结了监狱每天的状况：
Day 0: [0, 1, 0, 1, 1, 0, 0, 1]
Day 1: [0, 1, 1, 0, 0, 0, 0, 0]
Day 2: [0, 0, 0, 0, 1, 1, 1, 0]
Day 3: [0, 1, 1, 0, 0, 1, 0, 0]
...
Day 7: [0, 0, 1, 1, 0, 0, 0, 0]
```

**示例 2：**
```
输入: cells = [1,0,0,1,0,0,1,0], n = 1000000000
输出: [0,0,1,1,1,1,1,0]
```

---

## 解题思路

### 第一步：理解问题本质

这道题的关键在于：**N 可能非常大**（10^9），不能直接模拟每一天。

**关键洞察：**
- 只有 8 间牢房
- 首尾两间永远为 0
- 实际变化的只有中间 6 间
- 6 个二进制位最多有 2^6 = 64 种状态

**结论：** 状态必然会出现循环，周期最多为 64。

### 第二步：暴力解法

**思路：** 直接模拟每一天的状态变化。

```python
class Solution:
    def prisonAfterNDays(self, cells: List[int], n: int) -> List[int]:
        for _ in range(n):
            new_cells = [0] * 8
            for i in range(1, 7):
                new_cells[i] = 1 if cells[i-1] == cells[i+1] else 0
            cells = new_cells
        return cells
```

**为什么不够好？** 当 N = 10^9 时，需要模拟 10^9 天，会超时。

### 第三步：优化解法 - 找循环周期

**关键洞察：** 由于状态数有限，必然会出现循环。找到循环后可以跳过大量天数。

**算法步骤：**
1. 用哈希表记录每个状态出现的天数
2. 模拟每一天，更新状态
3. 如果发现重复状态，说明找到了循环
4. 计算循环周期，跳过完整的循环
5. 继续模拟剩余的天数

```python
class Solution:
    def prisonAfterNDays(self, cells: List[int], n: int) -> List[int]:
        def next_day(curr_cells):
            next_cells = [0] * 8
            for i in range(1, 7):
                next_cells[i] = 1 if curr_cells[i-1] == curr_cells[i+1] else 0
            return next_cells

        seen = {}

        while n > 0:
            state = tuple(cells)

            if state in seen:
                # 发现循环
                cycle_length = seen[state] - n
                n %= cycle_length
                break

            seen[state] = n

            if n >= 1:
                n -= 1
                cells = next_day(cells)

        # 继续模拟剩余天数
        while n > 0:
            cells = next_day(cells)
            n -= 1

        return cells
```

---

## 完整代码实现

```python
from typing import List

class Solution:
    """
    N 天后的牢房 - 找循环周期

    核心思路：
    由于牢房状态只有 8 间，且首尾固定为 0，实际只有 6 个位置会变化。
    6 个位置最多有 2^6 = 64 种状态，因此状态必然会出现循环。
    找到循环周期后，可以跳过大量天数。

    时间复杂度: O(1) - 最多模拟 64 个状态
    空间复杂度: O(1) - 最多存储 64 个状态
    """
    def prisonAfterNDays(self, cells: List[int], n: int) -> List[int]:
        def next_day(curr_cells: List[int]) -> List[int]:
            """计算下一天的牢房状态"""
            next_cells = [0] * 8
            for i in range(1, 7):
                next_cells[i] = 1 if curr_cells[i-1] == curr_cells[i+1] else 0
            return next_cells

        seen = {}

        while n > 0:
            state = tuple(cells)

            if state in seen:
                # 发现循环，计算循环周期
                cycle_length = seen[state] - n
                n %= cycle_length
                break

            seen[state] = n

            if n >= 1:
                n -= 1
                cells = next_day(cells)

        # 继续模拟剩余的天数
        while n > 0:
            cells = next_day(cells)
            n -= 1

        return cells
```

---

## 示例推演

以 `cells = [0,1,0,1,1,0,0,1], n = 7` 为例：

**状态变化过程：**

| 天数 | 状态 | 说明 |
|------|------|------|
| 0 | [0,1,0,1,1,0,0,1] | 初始状态 |
| 1 | [0,1,1,0,0,0,0,0] | 根据规则计算 |
| 2 | [0,0,0,0,1,1,1,0] | |
| 3 | [0,1,1,0,0,1,0,0] | |
| 4 | [0,0,0,0,0,1,0,0] | |
| 5 | [0,1,1,1,0,1,0,0] | |
| 6 | [0,0,1,0,1,1,0,0] | |
| 7 | [0,0,1,1,0,0,0,0] | 最终结果 |

**结果：** `[0,0,1,1,0,0,0,0]`

---

## 复杂度分析

| 解法 | 时间复杂度 | 空间复杂度 | 说明 |
|------|-----------|-----------|------|
| 暴力 | O(n × 8) | O(1) | 模拟每一天 |
| 找循环 | O(1) | O(1) | 最多 64 个状态 |

**说明：**
- 由于状态数最多 64 种，时间复杂度和空间复杂度都是 O(1)
- 这是典型的「状态压缩 + 找循环」问题

---

## 易错点总结

### 1. 首尾牢房的处理

```python
# 首尾永远为 0
next_cells = [0] * 8  # 直接初始化为 0
for i in range(1, 7):  # 只处理中间 6 间
    ...
```

### 2. 状态变化规则

```python
# 两个相邻房间状态相同，则变为占用(1)
# 否则变为空(0)
next_cells[i] = 1 if curr_cells[i-1] == curr_cells[i+1] else 0
```

### 3. 循环检测的时机

```python
# 先检查是否见过当前状态，再更新
if state in seen:
    cycle_length = seen[state] - n
    ...
seen[state] = n  # 记录当前状态
```

---

## 扩展思考

### 1. 如何确定最大循环周期？

- 实际变化的牢房：6 间
- 状态数：2^6 = 64
- 因此循环周期最多为 64

### 2. 如果牢房数量增加？

如果有 m 间牢房（首尾固定），则状态数为 2^(m-2)，仍然可以用同样的方法解决。

### 3. 相关题目

- [957. N 天后的牢房](https://leetcode.cn/problems/prison-cells-after-n-days/)
- [460. LFU 缓存](https://leetcode.cn/problems/lfu-cache/) - 类似的状态管理
- [202. 快乐数](https://leetcode.cn/problems/happy-number/) - 找循环的另一个例子

---

## 相关题目

- [460. LFU 缓存](https://leetcode.cn/problems/lfu-cache/)
- [202. 快乐数](https://leetcode.cn/problems/happy-number/)
- [166. 分数到小数](https://leetcode.cn/problems/fraction-to-recurring-decimal/) - 找循环
