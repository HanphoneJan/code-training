---
title: 全排列
platform: LeetCode
difficulty: 中等
id: 46
url: https://leetcode.cn/problems/permutations/
tags:
  - 回溯
  - 数组
topics:
  - ../../topics/array.md
  - ../../topics/backtracking.md
patterns:
  - ../../patterns/backtracking_template.md
date_added: 2026-03-23
date_reviewed: []
---

# 0046. 全排列

## 题目描述

给定一个不含重复数字的数组 `nums` ，返回其 **所有可能的全排列** 。你可以 **按任意顺序** 返回答案。

## 示例

**示例 1：**
```
输入：nums = [1,2,3]
输出：[[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]]
```

**示例 2：**
```
输入：nums = [0,1]
输出：[[0,1],[1,0]]
```

**示例 3：**
```
输入：nums = [1]
输出：[[1]]
```

---

## 解题思路

### 第一步：理解问题本质

**全排列**：给定 n 个不同元素，求所有可能的排列顺序。

对于 n 个不同元素，共有 `n!` 种排列。

**示例**：`[1,2,3]`
- 第1位可以是 1, 2, 或 3
- 第2位可以是剩余两个中的任意一个
- 第3位只能是剩下的最后一个

### 第二步：回溯算法框架

回溯算法通用模板：

```python
def backtrack(路径, 选择列表):
    if 满足结束条件:
        收集结果
        return
    for 选择 in 选择列表:
        if 选择不合法:
            continue
        做选择        # 将选择加入路径，标记为已使用
        backtrack(新路径, 新选择列表)
        撤销选择      # 恢复现场，撤销标记
```

对于全排列问题：
- **路径**：当前已经选择的数字序列
- **选择列表**：还未使用的数字
- **结束条件**：路径长度等于 n

### 第三步：关键问题——如何标记已使用的数字？

使用 `visited` 数组：
- `visited[i] = True` 表示 `nums[i]` 已经在路径中
- 每次选择时跳过已使用的数字

---

## 完整代码实现

```python
from typing import List

class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        """
        全排列 - 回溯算法（DFS）

        核心思想：逐位选择，每次从剩余数字中选一个，直到选完所有数字
        """
        ans = []      # 存储所有排列结果
        path = []     # 当前路径（一个排列的构建过程）
        n = len(nums)
        visited = [False] * n  # 标记哪些元素已被使用

        def dfs() -> None:
            """深度优先搜索构建排列"""
            # 结束条件：路径长度等于 n，得到一个完整排列
            if len(path) == n:
                ans.append(path[:])  # 必须复制，否则 path 变化会影响已保存的结果
                return

            # 遍历所有选择
            for i in range(n):
                if visited[i]:
                    continue  # 已使用的元素跳过

                # 做选择：将 nums[i] 加入路径
                visited[i] = True
                path.append(nums[i])

                # 递归进入下一层决策树
                dfs()

                # 撤销选择：恢复现场（回溯的关键）
                path.pop()
                visited[i] = False

        dfs()
        return ans
```

---

## 示例推演

**示例**：`nums = [1,2,3]`

**决策树**：

```
                    开始
                   / | \
                 1   2   3
                / \  / \  / \
               2   3 1   3 1   2
               |   | |   | |   |
               3   2 3   1 2   1
```

**DFS遍历过程**：

| 步骤 | 操作 | path | 说明 |
|------|------|------|------|
| 1 | 选1 | [1] | 标记1已使用 |
| 2 | 选2 | [1,2] | 标记2已使用 |
| 3 | 选3 | [1,2,3] | 标记3已使用，得到第一个排列 |
| 4 | 撤销3 | [1,2] | 回溯 |
| 5 | 无其他选择，撤销2 | [1] | 回溯 |
| 6 | 选3 | [1,3] | 标记3已使用 |
| 7 | 选2 | [1,3,2] | 标记2已使用，得到第二个排列 |
| 8 | 撤销2,3,1 | [] | 回溯到根 |
| 9 | 选2 | [2] | 开始以2开头的排列 |
| ... | ... | ... | 继续递归... |

**最终结果**：`[[1,2,3], [1,3,2], [2,1,3], [2,3,1], [3,1,2], [3,2,1]]`

---

## 复杂度分析

| 指标 | 复杂度 | 说明 |
|------|--------|------|
| 时间 | O(n × n!) | 共 n! 个排列，每个排列需要 O(n) 时间构造 |
| 空间 | O(n) | 递归深度 + visited 数组 + path |

---

## 易错点总结

### 1. 路径必须复制

```python
ans.append(path[:])  # 必须是 path[:]，不能是 path
```
`path` 是引用，后续修改会影响已保存的结果。

### 2. 恢复现场的顺序

```python
path.pop()           # 先弹出路径
visited[i] = False   # 再标记为未使用
```
顺序不能颠倒。

### 3. visited 数组的索引

```python
visited[i] = True   # i 是 nums 的索引
```
不是值，是索引！

### 4. 结束条件

```python
if len(path) == n:  # 不是 n-1
```
路径长度等于元素个数时才是一个完整排列。

---

## 扩展思考

### 1. 交换法实现

```python
def permuteSwap(self, nums: List[int]) -> List[List[int]]:
    ans = []
    n = len(nums)

    def dfs(start: int) -> None:
        if start == n:
            ans.append(nums[:])
            return
        for i in range(start, n):
            nums[start], nums[i] = nums[i], nums[start]  # 交换
            dfs(start + 1)
            nums[start], nums[i] = nums[i], nums[start]  # 恢复

    dfs(0)
    return ans
```
不需要 visited 数组，通过交换位置来生成排列。

### 2. 如果数组有重复元素？

需要剪枝：
```python
if i > 0 and nums[i] == nums[i-1] and not visited[i-1]:
    continue  # 跳过重复元素
```
这就是 [47. 全排列 II]。

### 3. 全排列与组合的区别

- 排列：考虑顺序，[1,2] 和 [2,1] 是不同的
- 组合：不考虑顺序，[1,2] 和 [2,1] 是相同的

---

## 相关题目

- [47. 全排列 II](https://leetcode.cn/problems/permutations-ii/)（含重复元素）
- [31. 下一个排列](https://leetcode.cn/problems/next-permutation/)
- [60. 排列序列](https://leetcode.cn/problems/permutation-sequence/)
- [77. 组合](https://leetcode.cn/problems/combinations/)
