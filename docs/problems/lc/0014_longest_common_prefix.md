---
title: 最长公共前缀
platform: LeetCode
difficulty: 简单
id: 14
url: https://leetcode.cn/problems/longest-common-prefix/
tags:
  - 字符串
topics:
  - ../../topics/string.md
date_added: 2026-03-20
date_reviewed: []
---

# 14. 最长公共前缀

## 题目描述

编写一个函数来查找字符串数组中的最长公共前缀。如果不存在公共前缀，返回空字符串 `""`。

**示例**：
- 输入：`strs = ["flower","flow","flight"]` → 输出：`"fl"`
- 输入：`strs = ["dog","racecar","car"]` → 输出：`""`（不存在公共前缀）

**约束**：
- `1 <= strs.length <= 200`
- `0 <= strs[i].length <= 200`
- `strs[i]` 仅由小写英文字母组成

---

## 解题思路

### 第一步：理解问题本质

"最长公共前缀"意味着：从第 0 个字符开始，找到所有字符串共同拥有的最长连续字符序列。

关键洞察：**公共前缀不可能比任何一个字符串更长**。因此，一旦某个字符串在某个位置与其他字符串不同（或已经到达该字符串末尾），公共前缀就在此终止。

### 第二步：暴力解法

最直觉的方法是**两两合并**：先求前两个字符串的公共前缀，再用结果与第三个字符串求公共前缀，依此类推。

```python
class Solution:
    def longestCommonPrefix(self, strs: list[str]) -> str:
        if not strs:
            return ""

        def common_prefix(a: str, b: str) -> str:
            i = 0
            while i < len(a) and i < len(b) and a[i] == b[i]:
                i += 1
            return a[:i]

        prefix = strs[0]
        for s in strs[1:]:
            prefix = common_prefix(prefix, s)
            if not prefix:  # 提前终止
                return ""
        return prefix
```

**时间复杂度**：O(n * m)，其中 n 为字符串数量，m 为最短字符串长度。

**为何还能更直接**：两两合并引入了一个辅助函数和中间变量，逻辑绕了一圈。实际上可以直接按"列"比较，更直观——固定列索引 `i`，检查所有字符串第 `i` 个字符是否相同。

### 第三步：优化解法（纵向逐列比较）

以第一个字符串为"参照"，逐字符（逐列）向右扫描，对每一列检查所有字符串在该位置的字符是否与参照字符一致。只要发现不一致，立刻返回当前已确认的前缀。

```python
class Solution:
    def longestCommonPrefix(self, strs: list[str]) -> str:
        if not strs:
            return ""
        # 以第一个字符串为基准，逐字符比较
        for i, char in enumerate(strs[0]):
            for s in strs[1:]:
                # 两种终止条件：
                # 1. 当前字符串已到末尾（i >= len(s)）
                # 2. 当前字符与基准字符不同
                if i >= len(s) or s[i] != char:
                    return strs[0][:i]
        # 所有字符都匹配，第一个字符串本身就是公共前缀
        return strs[0]
```

### 第四步：最优解法（二分查找）

理论上还可以用二分查找缩小前缀长度范围：最长公共前缀的长度一定在 `[0, min_len]` 之间（`min_len` 为最短字符串长度），对这个范围二分，每次检查候选长度是否是公共前缀。

但对于本题，二分查找的时间复杂度为 O(n * m * log m)，**反而比纵向比较的 O(n * m) 更慢**，因此纵向逐列比较就是实际最优解法，二分查找仅作为思路扩展了解即可。

---

## 完整代码实现

```python
from typing import List

class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if not strs:
            return ""
        for i, char in enumerate(strs[0]):
            for s in strs[1:]:
                if i >= len(s) or s[i] != char:
                    return strs[0][:i]
        return strs[0]
```

---

## 示例推演

以 `strs = ["flower", "flow", "flight"]` 为例，期望输出 `"fl"`。

以 `strs[0] = "flower"` 为基准，逐列检查：

**第 0 列，`i = 0`，`char = 'f'`**：
- `"flow"[0] = 'f'` == `'f'`，通过
- `"flight"[0] = 'f'` == `'f'`，通过
- 本列全部通过，继续

**第 1 列，`i = 1`，`char = 'l'`**：
- `"flow"[1] = 'l'` == `'l'`，通过
- `"flight"[1] = 'l'` == `'l'`，通过
- 本列全部通过，继续

**第 2 列，`i = 2`，`char = 'o'`**：
- `"flow"[2] = 'o'` == `'o'`，通过
- `"flight"[2] = 'i'` != `'o'`，不匹配！
- 立刻返回 `strs[0][:2]` = `"fl"`

最终结果：`"fl"`，正确。

---

## 复杂度分析

| 解法 | 时间复杂度 | 空间复杂度 | 说明 |
|------|-----------|-----------|------|
| 暴力（两两合并） | O(n * m) | O(m) | 需存储中间前缀变量 |
| 最优（纵向逐列） | O(n * m) | O(1) | 无额外空间，提前终止更快 |
| 二分查找 | O(n * m * log m) | O(m) | 理论有趣但实际更慢 |

> n 为字符串数量，m 为最短字符串长度。两种主流方法时间复杂度相同，纵向比较空间更优且实现更简洁。

---

## 易错点总结

1. **越界检查优先于字符比较**：在判断 `s[i] != char` 之前，必须先判断 `i >= len(s)`，否则当某个字符串比基准字符串短时会触发索引越界错误。代码中使用 `or` 的短路特性，先检查越界条件。
2. **空数组的处理**：题目约束保证数组非空，但防御性地加上 `if not strs` 是良好习惯。
3. **返回值的切片**：返回 `strs[0][:i]` 而非 `strs[0][:i+1]`，因为在发现第 `i` 列不匹配时，公共前缀是第 `0` 到 `i-1` 列，共 `i` 个字符，Python 切片 `[:i]` 恰好取前 `i` 个字符（不含第 `i` 个）。

---

## 扩展思考

- **字典序排序优化**：若先对字符串数组排序，最长公共前缀只需比较排序后的第一个和最后一个字符串即可（因为排序后差异最大的就是首尾两个）。这在字符串数量很多但最长公共前缀很短时可以显著减少比较次数。
- **本题核心**：这道题考查的是对"逐列扫描"思维的运用——将二维问题（多字符串 × 多字符）转化为按列逐步确认的线性扫描，遇到第一个不匹配就停止，避免无效计算。
