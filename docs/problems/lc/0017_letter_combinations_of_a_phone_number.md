---
title: 电话号码的字母组合
platform: LeetCode
difficulty: Medium
id: 17
url: https://leetcode.cn/problems/letter-combinations-of-a-phone-number/
tags:
  - 字符串
  - 回溯
  - 递归
date_added: 2026-03-25
---

# 17. 电话号码的字母组合

## 题目描述

给定一个仅包含数字 `2-9` 的字符串，返回所有它能表示的字母组合。答案可以按 **任意顺序** 返回。

给出数字到字母的映射如下（与电话按键相同）。注意 1 不对应任何字母。

```
2: abc
3: def
4: ghi
5: jkl
6: mno
7: pqrs
8: tuv
9: wxyz
```

## 示例

**示例 1：**
```
输入：digits = "23"
输出：["ad","ae","af","bd","be","bf","cd","ce","cf"]
```

**示例 2：**
```
输入：digits = ""
输出：[]
```

**示例 3：**
```
输入：digits = "2"
输出：["a","b","c"]
```

---

## 解题思路

### 第一步：理解问题本质

这是一个**组合问题**，需要枚举所有可能的字母组合。每个数字对应多个字母，需要将所有可能的组合都列举出来。

### 第二步：暴力解法

**思路**：用多重循环枚举所有组合。

```python
class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return []

        mapping = ["", "", "abc", "def", "ghi", "jkl", "mno", "pqrs", "tuv", "wxyz"]

        # 只能处理固定长度的情况
        result = []
        for c1 in mapping[int(digits[0])]:
            for c2 in mapping[int(digits[1])]:
                result.append(c1 + c2)
        return result
```

**缺点**：只能处理固定长度的输入，无法通用。

### 第三步：最优解法 —— 回溯

**核心洞察**：
- 这是一个经典的回溯/DFS 问题
- 逐位处理数字，对每个数字尝试所有可能的字母
- 递归处理下一位，直到处理完所有数字

**回溯三要素**：
1. **路径**：当前已构建的字母组合（path）
2. **选择列表**：当前数字对应的所有字母
3. **终止条件**：path 长度等于 digits 长度

---

## 完整代码实现

```python
from typing import List

# 电话号码到字母的映射
MAPPING = ["", "", "abc", "def", "ghi", "jkl", "mno", "pqrs", "tuv", "wxyz"]

class Solution:
    """
    电话号码的字母组合 - 回溯算法

    核心思想：
    每个数字对应多个字母，需要枚举所有可能的字母组合。
    使用回溯（DFS）逐位选择字母，构建所有组合。

    回溯框架：
    1. 路径：当前已构建的字母组合（path）
    2. 选择列表：当前数字对应的所有字母
    3. 终止条件：path 长度等于 digits 长度

    时间复杂度：O(3^m * 4^n)，m 是映射到3个字母的数字个数，n 是映射到4个字母的数字个数
    空间复杂度：O(m+n)，递归深度
    """

    def letterCombinations(self, digits: str) -> List[str]:
        n = len(digits)
        if n == 0:
            return []

        ans = []
        path = [''] * n  # 预分配空间，存储当前路径

        def dfs(num: int):
            """
            处理第 num 个数字
            num: 当前处理的数字索引（0-based）
            """
            if num == n:
                # 所有数字都处理完毕，得到一个完整组合
                ans.append(''.join(path))
                return

            # 遍历当前数字对应的所有字母
            for word in MAPPING[int(digits[num])]:
                path[num] = word      # 做选择
                dfs(num + 1)          # 递归处理下一个数字
                # 撤销选择（回溯）：path[num] 会被覆盖，无需显式恢复

        dfs(0)
        return ans
```

---

## 示例推演

以 `digits = "23"` 为例：

**MAPPING**：
- `MAPPING[2] = "abc"`
- `MAPPING[3] = "def"`

**DFS 过程**：

```
dfs(0): 处理 '2'
  ├─ 选 'a': path=['a', '']
  │   └─ dfs(1): 处理 '3'
  │       ├─ 选 'd': path=['a', 'd'] → 得到 "ad"
  │       ├─ 选 'e': path=['a', 'e'] → 得到 "ae"
  │       └─ 选 'f': path=['a', 'f'] → 得到 "af"
  ├─ 选 'b': path=['b', '']
  │   └─ dfs(1): 处理 '3'
  │       ├─ 选 'd': path=['b', 'd'] → 得到 "bd"
  │       ├─ 选 'e': path=['b', 'e'] → 得到 "be"
  │       └─ 选 'f': path=['b', 'f'] → 得到 "bf"
  └─ 选 'c': path=['c', '']
      └─ dfs(1): 处理 '3'
          ├─ 选 'd': path=['c', 'd'] → 得到 "cd"
          ├─ 选 'e': path=['c', 'e'] → 得到 "ce"
          └─ 选 'f': path=['c', 'f'] → 得到 "cf"
```

**结果**：`["ad","ae","af","bd","be","bf","cd","ce","cf"]`

---

## 复杂度分析

| 解法 | 时间复杂度 | 空间复杂度 | 说明 |
|------|-----------|-----------|------|
| 暴力 | - | - | 无法处理变长输入 |
| **回溯（最优）** | **O(3^m × 4^n)** | **O(m+n)** | m是3字母数字个数，n是4字母数字个数 |

---

## 易错点总结

### 1. 空字符串处理

```python
if n == 0:
    return []  # 不是 return [""]
```

### 2. 回溯的撤销操作

本题中 `path[num]` 会被下一次循环覆盖，所以无需显式撤销。但在其他回溯问题中可能需要。

### 3. 预分配 path 空间

```python
path = [''] * n  # 预分配，避免频繁创建字符串
```

---

## 扩展思考

### 1. 如果要求按字典序返回？

回溯天然按字典序生成，当前实现已经满足。

### 2. 如果数字可以重复按？

修改 MAPPING，或者添加额外的映射逻辑。

---

## 相关题目

- [39. 组合总和](https://leetcode.cn/problems/combination-sum/)
- [46. 全排列](https://leetcode.cn/problems/permutations/)
- [78. 子集](https://leetcode.cn/problems/subsets/)
