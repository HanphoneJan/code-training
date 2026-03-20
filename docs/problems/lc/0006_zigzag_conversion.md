---
title: Z 字形变换
platform: LeetCode
difficulty: 中等
id: 6
url: https://leetcode.cn/problems/zigzag-conversion/
tags:
  - 字符串
topics:
  - ../../topics/string.md
date_added: 2026-03-20
date_reviewed: []
---

# 0006. Z 字形变换

## 题目描述

将一个给定字符串 `s` 根据给定的行数 `numRows`，以从上往下、从左到右进行 Z 字形排列。之后，你的输出需要从左往右逐行读取，产生一个新的字符串。

**示例 1：**
```
输入：s = "PAYPALISHIRING", numRows = 3
输出："PAHNAPLSIIGYIR"
解释：
P   A   H   N
A P L S I I G
Y   I   R
```

**示例 2：**
```
输入：s = "PAYPALISHIRING", numRows = 4
输出："PINALSIGYAHRPI"
解释：
P     I    N
A   L S  I G
Y A   H R
P     I
```

**示例 3：**
```
输入：s = "A", numRows = 1
输出："A"
```

**约束**：`1 <= s.length <= 1000`，`numRows` 满足 `1 <= numRows <= 1000`。

---

## 解题思路

### 第一步：理解问题本质

Z 字形排列的规律是：字符按照一个固定的"之"字形路径填入行中。具体而言，路径方向在到达第一行或最后一行时反转：

```
行 0:  s[0]           s[4]           s[8]
行 1:  s[1]     s[3]  s[5]     s[7]  s[9]
行 2:  s[2]           s[6]           s[10]
         ↓       ↑       ↓       ↑
```

每次从上到下走 `numRows` 步，再从下到上走 `numRows - 2` 步（中间行），形成一个周期 `cycle = 2 * (numRows - 1)`。

最终答案是把每一行的字符拼接起来。

### 第二步：暴力解法——模拟 Z 字形矩阵

直接开一个二维矩阵，按照 Z 字形路径逐格填入字符，最后按行读取。

```python
def convert(s: str, numRows: int) -> str:
    if numRows == 1:
        return s
    # 构建足够宽的矩阵
    n = len(s)
    cycle = 2 * (numRows - 1)
    num_cols = (n // cycle + 1) * (numRows - 1)
    grid = [[''] * num_cols for _ in range(numRows)]

    row, col = 0, 0
    going_down = True
    for ch in s:
        grid[row][col] = ch
        if going_down:
            if row == numRows - 1:
                going_down = False
                row -= 1
                col += 1
            else:
                row += 1
        else:
            if row == 0:
                going_down = True
                row += 1
            else:
                row -= 1
                col += 1

    return ''.join(ch for row in grid for ch in row)
```

- 时间复杂度：O(n × numRows)——遍历矩阵所有格子
- 空间复杂度：O(n × numRows)——整个矩阵

**问题**：矩阵中绝大多数格子都是空的，浪费大量空间；读取时还要跳过空格子，逻辑繁琐。

### 第三步：优化——按行收集字符

观察关键点：**最终结果只依赖于每一行的字符序列**，完全不需要知道列的位置。

因此，只需维护 `numRows` 个字符串，模拟 Z 字形路径的行号变化，把每个字符追加到对应行的字符串末尾，最后将所有行拼接即可。

行号的变化规律：从 0 增加到 `numRows - 1`，再从 `numRows - 1` 减回 0，不断重复。用一个方向标志 `flag` 控制：到达第一行时 `flag = +1`（向下），到达最后一行时 `flag = -1`（向上）。

### 第四步：最优解法——行号模拟

```
flag 初始为 +1（向下）
index 初始为 0（从第 0 行开始）

对于 s 中每个字符：
  1. 将字符加入 rows[index]
  2. 如果 index == 0，设 flag = +1
     如果 index == numRows - 1，设 flag = -1
  3. index += flag
```

两个边界条件的更新顺序：**先把字符加入当前行，再根据当前行判断是否反向**。这样可以保证第一行和最后一行各自只触发一次方向切换。

---

## 完整代码实现

```python
class Solution:
    def convert(self, s: str, numRows: int) -> str:
        # 只有一行时，Z 字形退化为原字符串
        if numRows == 1:
            return s

        rows = [''] * numRows  # 每行的字符收集桶
        index = 0              # 当前所在行
        flag = 1               # 行进方向：+1 向下，-1 向上

        for ch in s:
            rows[index] += ch
            # 到达第一行：转为向下；到达最后一行：转为向上
            if index == 0:
                flag = 1
            elif index == numRows - 1:
                flag = -1
            index += flag

        return ''.join(rows)
```

---

## 示例推演

**输入**：`s = "PAYPALISHIRING"`, `numRows = 3`

初始化：`rows = ['', '', '']`，`index = 0`，`flag = 1`

逐字符追踪（先记录当前 index，再更新 flag 和 index）：

| 字符 | 进入前 index | 操作 | flag 更新 | index 更新后 |
|------|------------|------|-----------|------------|
| P | 0 | rows[0] += 'P' → `"P"` | index==0，flag=1 | 0+1=1 |
| A | 1 | rows[1] += 'A' → `"A"` | 无 | 1+1=2 |
| Y | 2 | rows[2] += 'Y' → `"Y"` | index==2，flag=-1 | 2-1=1 |
| P | 1 | rows[1] += 'P' → `"AP"` | 无 | 1-1=0 |
| A | 0 | rows[0] += 'A' → `"PA"` | index==0，flag=1 | 0+1=1 |
| L | 1 | rows[1] += 'L' → `"APL"` | 无 | 1+1=2 |
| I | 2 | rows[2] += 'I' → `"YI"` | index==2，flag=-1 | 2-1=1 |
| S | 1 | rows[1] += 'S' → `"APLS"` | 无 | 1-1=0 |
| H | 0 | rows[0] += 'H' → `"PAH"` | index==0，flag=1 | 0+1=1 |
| I | 1 | rows[1] += 'I' → `"APLSI"` | 无 | 1+1=2 |
| R | 2 | rows[2] += 'R' → `"YIR"` | index==2，flag=-1 | 2-1=1 |
| I | 1 | rows[1] += 'I' → `"APLSII"` | 无 | 1-1=0 |
| N | 0 | rows[0] += 'N' → `"PAHN"` | index==0，flag=1 | 0+1=1 |
| G | 1 | rows[1] += 'G' → `"APLSIIG"` | 无 | 1+1=2 |

最终各行：
- `rows[0] = "PAHN"`
- `rows[1] = "APLSIIG"`
- `rows[2] = "YIR"`

拼接结果：`"PAHN" + "APLSIIG" + "YIR" = "PAHNAPLSIIGYIR"` ✓

---

## 复杂度分析

| 解法 | 时间复杂度 | 空间复杂度 | 说明 |
|------|-----------|-----------|------|
| 二维矩阵模拟 | O(n × numRows) | O(n × numRows) | 矩阵大量空格浪费空间 |
| 行号模拟（最优） | O(n) | O(n) | 只遍历一次字符串，**最优解** |

注：输出本身需要 O(n) 空间，`rows` 数组的总字符数等于 `n`，因此空间复杂度是 O(n) 而非 O(n × numRows)。

---

## 易错点总结

- **numRows = 1 的特判**：当只有一行时，`flag` 永远不会反转（不存在"最后一行"触发反向的条件），`index` 会无限增大导致越界。必须在最开始单独处理。
- **先追加字符，再更新 flag**：如果先更新 flag 再追加字符，第一行的字符会被追加到 `rows[1]`，导致结果错误。正确顺序是：追加 → 判断边界 → 移动。
- **flag 初始值**：`flag = 1` 表示从第 0 行向下开始，这是正确的初始方向。如果初始化为 `-1`，`index` 会立即变成 `-1` 导致越界。

---

## 扩展思考

### 1. 数学规律求解

不模拟路径，直接通过数学公式计算每个字符属于哪一行，可以省去 `rows` 数组并直接按行读取。核心是周期 `cycle = 2 * (numRows - 1)`：

- 每个周期内，第 0 行和第 `numRows-1` 行各贡献 1 个字符
- 中间行 `r`（1 ≤ r ≤ numRows-2）每个周期贡献 2 个字符：位置 `r` 和 `cycle - r`

这种方法时间复杂度同为 O(n)，但可以直接输出结果而无需 `join`。

### 2. 相关题目

- [6 变体] 如果不是按行读取，而是按 Z 字形的顺序输出，逻辑完全相同，只需修改最终拼接方式。
- [48. 旋转图像](https://leetcode.cn/problems/rotate-image/)——同样是字符/元素在二维结构中按规律移动的问题。
