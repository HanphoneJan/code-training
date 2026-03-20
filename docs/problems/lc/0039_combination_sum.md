---
title: 组合总和
platform: LeetCode
difficulty: 中等
id: 39
url: https://leetcode.cn/problems/combination-sum/
tags:
  - 数组
  - 回溯
topics:
  - ../../topics/array.md
patterns:
  - ../../patterns/backtracking.md
  - ../../patterns/dfs.md
date_added: 2026-03-20
date_reviewed: []
---

# 0039. 组合总和

## 题目描述

给你一个**无重复元素**的整数数组 `candidates` 和一个目标整数 `target`，找出 `candidates` 中可以使数字和为目标数 `target` 的**所有不同组合**，并以列表形式返回。你可以按**任意顺序**返回这些组合。

`candidates` 中的**同一个**数字可以**无限制重复被选取**。如果至少一个数字的被选数量不同，则两种组合是不同的。

对于给定的输入，保证和为 `target` 的不同组合数少于 `150` 个。

**示例 1：**
```
输入：candidates = [2,3,6,7], target = 7
输出：[[2,2,3],[7]]
```

**示例 2：**
```
输入：candidates = [2,3,5], target = 8
输出：[[2,2,2,2],[2,3,3],[3,5]]
```

**示例 3：**
```
输入：candidates = [2], target = 1
输出：[]
```

---

## 解题思路

### 第一步：理解问题本质

这道题要找所有满足条件的**组合**（不考虑顺序，`[2,3]` 和 `[3,2]` 视为同一组合），且每个数字可以重复使用。

搜索"所有满足条件的组合"这类问题，经典解法是**回溯（Backtracking）**：逐步构建候选组合，如果当前路径不可能达到目标就提前放弃（剪枝），如果达到目标就记录。

形象地说，回溯就是在一棵"选择树"上做深度优先搜索（DFS）：每个节点代表一次选择，走到叶子节点时判断是否满足条件，不满足就原路返回（回溯）尝试其他分支。

### 第二步：暴力解法

递归枚举所有可能的组合（不带剪枝，且不去重）。

```python
class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        ans = []
        def dfs(path, remain):
            if remain == 0:
                ans.append(sorted(path[:]))  # 排序后去重
                return
            if remain < 0:
                return
            for c in candidates:
                path.append(c)
                dfs(path, remain - c)
                path.pop()
        dfs([], target)
        # 去除重复组合
        return [list(x) for x in set(tuple(p) for p in ans)]
```

**为什么不够好**：
- 每个位置都从所有候选数重新选择，会产生大量重复状态（如 `[2,3]` 和 `[3,2]` 会都被生成）。
- 去重操作本身耗时，且递归树分支爆炸，时间复杂度极高。

### 第三步：优化——通过起始下标避免重复

**为什么会产生重复？** 如果每次选择都从头开始扫描 candidates，`[2,3]` 和 `[3,2]` 都会被生成。

**解决方法**：给 DFS 传入一个 `start` 参数，每次只从 `start` 位置开始选，不往前回头。这样保证组合中的数字是非递减的，自然消除了重复。

比如，选了 `3` 之后，下次只能继续选 `3` 或更大的数，不会再选 `2`，从而避免 `[3,2]` 的出现。

### 第四步：加入剪枝——提前终止无效分支

在加入 `start` 参数之后，还可以进一步优化：如果当前候选数已经大于剩余目标，那更大的候选数也一定大于剩余目标，直接 `break` 跳出循环。

**前提**：candidates 需要先排序，才能保证从 `start` 往后的数字是递增的，`break` 才合理。

排序后，当 `candidates[i] > remain` 时，`i` 之后的所有数都大于 `remain`，无需继续枚举，直接剪枝。

---

## 完整代码实现

```python
from typing import List

class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()  # 排序，方便剪枝
        ans = []
        path = []

        def dfs(start: int, remain: int):
            if remain == 0:
                ans.append(path[:])  # 找到一个合法组合，记录副本
                return
            for i in range(start, len(candidates)):
                if candidates[i] > remain:
                    break  # 剪枝：当前数已超过剩余目标，后续更大，无需继续
                path.append(candidates[i])
                dfs(i, remain - candidates[i])  # 允许重复使用，从 i 开始（而非 i+1）
                path.pop()                       # 回溯：撤销上一步选择

        dfs(0, target)
        return ans
```

**关键点**：
- `dfs(i, remain - candidates[i])` 中用 `i` 而非 `i+1`，允许当前数字被重复选取。
- `path[:]` 是列表的浅拷贝，必须拷贝后再存入 `ans`，否则 `path` 后续被修改后 `ans` 中的记录也会变。

---

## 示例推演

以 `candidates = [2, 3, 6, 7]`，`target = 7` 为例（已排序）：

下面展示完整的递归树搜索过程（只展示主要分支）：

```
dfs(start=0, remain=7), path=[]
├── 选 2: path=[2], dfs(start=0, remain=5)
│   ├── 选 2: path=[2,2], dfs(start=0, remain=3)
│   │   ├── 选 2: path=[2,2,2], dfs(start=0, remain=1)
│   │   │   ├── 选 2: 2>1, break（剪枝）
│   │   │   └── 回溯 → path=[2,2]
│   │   ├── 选 3: path=[2,2,3], dfs(start=1, remain=0)
│   │   │   └── remain==0，记录 [2,2,3]
│   │   ├── 选 6: 6>3, break（剪枝）
│   │   └── 回溯 → path=[2]
│   ├── 选 3: path=[2,3], dfs(start=1, remain=2)
│   │   ├── 选 3: 3>2, break（剪枝）
│   │   └── 回溯 → path=[2]
│   ├── 选 6: 6>5, break（剪枝）
│   └── 回溯 → path=[]
├── 选 3: path=[3], dfs(start=1, remain=4)
│   ├── 选 3: path=[3,3], dfs(start=1, remain=1)
│   │   ├── 选 3: 3>1, break（剪枝）
│   │   └── 回溯 → path=[3]
│   ├── 选 6: 6>4, break（剪枝）
│   └── 回溯 → path=[]
├── 选 6: path=[6], dfs(start=2, remain=1)
│   ├── 选 6: 6>1, break（剪枝）
│   └── 回溯 → path=[]
└── 选 7: path=[7], dfs(start=3, remain=0)
    └── remain==0，记录 [7]
```

**最终结果**：`[[2, 2, 3], [7]]`，与预期一致。

---

## 复杂度分析

| 解法 | 时间复杂度 | 空间复杂度 | 说明 |
|------|-----------|-----------|------|
| 暴力（无 start、无剪枝） | 指数级，含大量重复 | O(target/min) | 每层都从头枚举，重复状态极多 |
| 回溯+start（无剪枝） | O(n^(target/min)) | O(target/min) | min 为最小候选数，递归深度上限 |
| 回溯+start+剪枝（最优） | 剪枝后大幅减小 | O(target/min) | 排序后遇到大数提前 break |

> 注：组合数问题没有一个简洁的精确时间复杂度，通常用"指数级"描述，剪枝能显著减少实际运行时间。空间复杂度主要由递归栈深度决定，最深为 `target / min(candidates)`。

---

## 易错点总结

- **`path[:]` 而非 `path`**：`ans.append(path)` 存入的是引用，后续 `path.pop()` 会修改已存入的内容。必须用 `path[:]` 存一个当前状态的副本。

- **重复使用用 `i` 而非 `i+1`**：`dfs(i, ...)` 表示下一层仍可选当前数字（允许重复）。若改为 `dfs(i+1, ...)`，则每个数字最多选一次，变成了另一道题（LeetCode 40. 组合总和 II）。

- **剪枝依赖排序**：`break` 的前提是 candidates 已排序，否则后面可能有更小的数，不能直接跳出。

- **回溯要配对**：`path.append(...)` 和 `path.pop()` 必须成对出现，否则 path 状态会在不同递归分支间相互污染。

---

## 扩展思考

- **LeetCode 40. 组合总和 II**：candidates 有重复元素，每个数字只能用一次。需要在 `start` 基础上额外跳过同层重复元素（`if i > start and candidates[i] == candidates[i-1]: continue`）。

- **LeetCode 216. 组合总和 III**：从 1-9 中选 k 个不重复数字，使其和为 n，每个数字最多使用一次。

- **算法本质**：回溯算法是在解空间树上进行深度优先搜索，剪枝是其核心优化手段。`start` 参数的引入从根本上消除了组合重复问题（保证生成的组合字典序单调不降），比生成后去重高效得多。这种"通过限制搜索起点来去重"的技巧在所有组合/子集类问题中普遍适用。
