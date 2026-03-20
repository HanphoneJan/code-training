---
title: 正则表达式匹配
platform: LeetCode
difficulty: 困难
id: 10
url: https://leetcode.cn/problems/regular-expression-matching/
tags:
  - 字符串
  - 动态规划
  - 递归
topics:
  - ../../topics/string.md
  - ../../topics/dynamic_programming.md
patterns:
  - ../../patterns/recursion.md
date_added: 2026-03-20
date_reviewed: []
---

# 10. 正则表达式匹配

## 题目描述

给你一个字符串 s 和一个字符规律 p，请你来实现一个支持 `'.'` 和 `'*'` 的正则表达式匹配。

- `'.'` 匹配任意单个字符
- `'*'` 匹配零个或多个前面的那一个元素

所谓匹配，是要涵盖**整个**字符串 s，而不是部分字符串。

**示例：**
- 输入：s = "aa"，p = "a"，输出：false（"a" 无法匹配整个 "aa"）
- 输入：s = "aa"，p = "a*"，输出：true（"a*" 可以匹配零个或多个 'a'，此处匹配两个）
- 输入：s = "ab"，p = ".*"，输出：true（".*" 匹配任意字符串）
- 输入：s = "aab"，p = "c*a*b"，输出：true（"c*" 匹配零个 'c'，"a*" 匹配两个 'a'，"b" 匹配 'b'）

---

## 解题思路

### 第一步：理解问题本质

这道题的难点在于 `'*'` 的特殊语义：它不能单独使用，必须跟在某个字符后面，代表"该字符出现 0 次或多次"。

例如 `a*` 可以表示空字符串、"a"、"aa"、"aaa"……这种**不确定性**使得直接用循环逐字符比较行不通，必须使用能够处理"选择"的算法。

核心挑战：**遇到 `x*` 时，不知道它应该匹配多少个字符**，需要穷举所有可能性并找到一种成立的情况。

### 第二步：暴力解法——递归

递归的思路是：每次处理 s 和 p 的当前字符，根据 p 的当前字符决定如何递归处理剩余部分。

**递归的三种情况：**

**情况一：p 的下一个字符是 `'*'`**

此时 `p[j]` 与 `p[j+1]='*'` 合在一起，有两种选择：
1. 让 `x*` 匹配 0 次：跳过 p 中的这两个字符，s 不动，递归 `match(i, j+2)`
2. 让 `x*` 匹配 1 次（如果当前字符匹配）：s 向后移一位，p 不动（因为 `*` 还可以继续匹配），递归 `match(i+1, j)`

**情况二：p 的下一个字符不是 `'*'`**

当前字符必须严格匹配（`s[i] == p[j]` 或 `p[j] == '.'`），然后双方都向后移一位，递归 `match(i+1, j+1)`。

**情况三：到达终止状态**

若 p 已经用完，则 s 也必须同时用完，才算匹配成功。

```python
class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        def match(i, j):
            # 终止条件：p 已用完
            if j == len(p):
                return i == len(s)
            # 当前字符是否匹配
            first_match = i < len(s) and (p[j] == '.' or p[j] == s[i])
            # p 的下一个字符是否是 '*'
            if j + 1 < len(p) and p[j + 1] == '*':
                # 选择1：x* 匹配0次（跳过 x*）
                # 选择2：x* 匹配1次（需要当前字符匹配）
                return match(i, j + 2) or (first_match and match(i + 1, j))
            else:
                return first_match and match(i + 1, j + 1)

        return match(0, 0)
```

**为什么不够好：** 递归中存在大量重复计算。例如 `match(i, j)` 可能被调用多次，但每次的结果是相同的。时间复杂度在最坏情况下是指数级的，对于较长的 s 和 p 会超时。

### 第三步：优化解法——记忆化递归

在递归的基础上，加一个"备忘录"：第一次计算 `match(i, j)` 后，把结果缓存起来。下次再遇到相同的 (i, j)，直接返回缓存值，不再重新计算。

```python
class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        from functools import lru_cache

        @lru_cache(maxsize=None)
        def match(i, j):
            if j == len(p):
                return i == len(s)
            first_match = i < len(s) and (p[j] == '.' or p[j] == s[i])
            if j + 1 < len(p) and p[j + 1] == '*':
                return match(i, j + 2) or (first_match and match(i + 1, j))
            else:
                return first_match and match(i + 1, j + 1)

        return match(0, 0)
```

加上缓存后，每个 (i, j) 只计算一次，总共有 O(m × n) 种状态，时间复杂度降为 O(m × n)。

**为什么还有更好的做法：** 记忆化递归依赖系统调用栈，递归深度过大时可能导致栈溢出。动态规划用循环替代递归，更加稳健，也更容易理解状态转移的全貌。

### 第四步：最优解法——动态规划

动态规划将递归的"自顶向下"改为"自底向上"的填表过程。

**定义 dp 数组：**

`dp[i][j]` 表示：s 的前 i 个字符（即 `s[0..i-1]`）能否被 p 的前 j 个字符（即 `p[0..j-1]`）完全匹配。

注意：下标偏移了 1，`dp[0][0] = True` 表示空字符串匹配空模式。

**状态转移方程：**

对于每个位置 (i, j)，分两大情况：

**情况一：p[j-1] == '*'**

`'*'` 必须与它前面的字符 `p[j-2]` 配合使用，有两种选项：

- **选项 A：`*` 匹配 0 次**（抛弃 `p[j-2]` 和 `p[j-1]` 这两个字符）
  ```
  dp[i][j] |= dp[i][j-2]
  ```

- **选项 B：`*` 匹配 1 次或多次**（需要 s[i-1] 与 p[j-2] 匹配）
  ```
  如果 matches(i, j-1)：dp[i][j] |= dp[i-1][j]
  ```
  这里 `dp[i-1][j]` 表示：s 的前 i-1 个字符已经被 p 的前 j 个字符匹配，再让 `p[j-2]*` 额外匹配一个 `s[i-1]`。

**情况二：p[j-1] 是普通字符或 `'.'`**

当前字符必须对应匹配：
```
如果 matches(i, j)：dp[i][j] |= dp[i-1][j-1]
```

**辅助函数 matches(i, j)：**

判断 s[i-1] 与 p[j-1] 是否能够匹配（注意 i 和 j 是 1-indexed，要减 1 才是实际下标）：
- 若 i == 0，s 没有字符可以匹配，返回 false
- 若 p[j-1] == '.'，匹配任意字符，返回 true
- 否则判断 s[i-1] == p[j-1]

**初始化：**

- `dp[0][0] = True`：空字符串匹配空模式
- `dp[0][j]`：空字符串匹配 p 的前 j 个字符，只有当 p 的前 j 个字符是若干个 `x*` 的组合时才为 true。例如 `dp[0][2]` 在 `p = "a*"` 时为 true，因为 `a*` 可以匹配 0 次

```python
class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        m, n = len(s), len(p)

        def matches(i: int, j: int) -> bool:
            if i == 0:
                return False
            if p[j - 1] == '.':
                return True
            return s[i - 1] == p[j - 1]

        dp = [[False] * (n + 1) for _ in range(m + 1)]
        dp[0][0] = True

        for i in range(m + 1):
            for j in range(1, n + 1):
                if p[j - 1] == "*":
                    dp[i][j] |= dp[i][j - 2]          # '*' 匹配0次
                    if matches(i, j - 1):
                        dp[i][j] |= dp[i - 1][j]      # '*' 匹配1次或多次
                else:
                    if matches(i, j):
                        dp[i][j] |= dp[i - 1][j - 1]  # 普通字符逐一匹配

        return dp[m][n]
```

---

## 完整代码实现

```python
class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        m, n = len(s), len(p)

        def matches(i: int, j: int) -> bool:
            """判断 s[i-1] 与 p[j-1] 是否能够匹配（i, j 为 1-indexed）"""
            if i == 0:
                return False
            if p[j - 1] == '.':
                return True
            return s[i - 1] == p[j - 1]

        # dp[i][j] = s 的前 i 个字符能否被 p 的前 j 个字符匹配
        dp = [[False] * (n + 1) for _ in range(m + 1)]
        dp[0][0] = True

        for i in range(m + 1):
            for j in range(1, n + 1):
                if p[j - 1] == "*":
                    dp[i][j] |= dp[i][j - 2]          # '*' 匹配0次：跳过 x*
                    if matches(i, j - 1):
                        dp[i][j] |= dp[i - 1][j]      # '*' 匹配更多：s 向后退一格
                else:
                    if matches(i, j):
                        dp[i][j] |= dp[i - 1][j - 1]  # 普通字符：逐一匹配

        return dp[m][n]
```

---

## 示例推演

以 s = "aab"，p = "c*a*b" 为例，期望结果为 true。

m = 3，n = 5，p 各位：`c`, `*`, `a`, `*`, `b`

构建 dp 表（行为 s 的前 i 个字符，列为 p 的前 j 个字符）：

**初始化：**

```
dp[0][0] = True（空匹配空）
dp[0][1]：p[0]='c'，不是'*'，保持 False
dp[0][2]：p[1]='*'，dp[0][2] |= dp[0][0] = True（c* 匹配0次）
dp[0][3]：p[2]='a'，不是'*'，保持 False
dp[0][4]：p[3]='*'，dp[0][4] |= dp[0][2] = True（a* 匹配0次，在 c* 匹配0次的基础上）
dp[0][5]：p[4]='b'，不是'*'，保持 False
```

**i = 1（s[0] = 'a'）：**

```
j=1：p[0]='c'，matches(1,1)=False（'a'!='c'），dp[1][1]=False
j=2：p[1]='*'，dp[1][2] |= dp[1][0]=False；matches(1,1)='a' vs 'c'=False，dp[1][2]=False
j=3：p[2]='a'，matches(1,3)=True（'a'=='a'），dp[1][3] |= dp[0][2]=True → dp[1][3]=True
j=4：p[3]='*'，dp[1][4] |= dp[1][2]=False；matches(1,3)=True，dp[1][4] |= dp[0][4]=True → dp[1][4]=True
j=5：p[4]='b'，matches(1,5)=False（'a'!='b'），dp[1][5]=False
```

**i = 2（s[1] = 'a'）：**

```
j=1：matches(2,1)=False，dp[2][1]=False
j=2：p[1]='*'，dp[2][2] |= dp[2][0]=False；matches(2,1)=False，dp[2][2]=False
j=3：p[2]='a'，matches(2,3)=True，dp[2][3] |= dp[1][2]=False → dp[2][3]=False
j=4：p[3]='*'，dp[2][4] |= dp[2][2]=False；matches(2,3)=True，dp[2][4] |= dp[1][4]=True → dp[2][4]=True
j=5：p[4]='b'，matches(2,5)=False（'a'!='b'），dp[2][5]=False
```

**i = 3（s[2] = 'b'）：**

```
j=1：matches(3,1)=False，dp[3][1]=False
j=2：dp[3][2] |= dp[3][0]=False；matches(3,1)=False，dp[3][2]=False
j=3：p[2]='a'，matches(3,3)=False（'b'!='a'），dp[3][3]=False
j=4：p[3]='*'，dp[3][4] |= dp[3][2]=False；matches(3,3)=False，dp[3][4]=False
j=5：p[4]='b'，matches(3,5)=True（'b'=='b'），dp[3][5] |= dp[2][4]=True → dp[3][5]=True
```

最终 `dp[3][5] = True`，返回 true。

含义：`c*` 匹配零个 'c'，`a*` 匹配两个 'a'，`b` 匹配一个 'b'，整体匹配成功。

---

## 复杂度分析

| 解法 | 时间复杂度 | 空间复杂度 | 说明 |
|------|-----------|-----------|------|
| 暴力递归 | 指数级 O(2^(m+n)) | O(m+n) | 大量重复子问题，递归栈空间 |
| 记忆化递归 | O(m × n) | O(m × n) | 缓存所有子问题结果 |
| 动态规划 | O(m × n) | O(m × n) | 自底向上填表，无递归开销 |

> m = len(s)，n = len(p)

---

## 易错点总结

- **`'*'` 的含义**：`'*'` 绝不单独使用，永远表示"前一个字符出现 0 次或多次"。`dp[i][j-2]` 对应"匹配 0 次"，必须向前跳两格而不是一格。
- **下标偏移**：dp 数组是 1-indexed（从 1 开始），所以访问实际字符时需要 `s[i-1]` 和 `p[j-1]`。这个偏移是为了让 `dp[0][0]` 表示空字符串，处理边界更方便。
- **`matches(i, j)` 中的 `i == 0` 判断**：当 i=0 时，s 没有字符，不能和 p 的任何字符匹配，必须返回 False，否则会产生越界错误。
- **`dp[i-1][j]` 而不是 `dp[i-1][j-2]`**：`'*'` 匹配"更多次"时，p 不移动（因为 `*` 还可以继续匹配），只有 s 向后移一位。这是最常见的理解误区。
- **初始化 `dp[0][j]`**：空字符串 s 能匹配某些非空模式 p，例如 `a*`、`a*b*c*` 等（它们都可以匹配零次），初始化时必须通过循环正确填写这些值，不能全部设为 False。

---

## 扩展思考

**相关题目：**
- LeetCode 44. 通配符匹配：`'*'` 的含义不同，这里 `'*'` 可以匹配任意字符串（包括空串），DP 思路相似但状态转移不同
- LeetCode 72. 编辑距离：同样是字符串 DP，`dp[i][j]` 定义为两个子串的编辑代价

**算法本质：**

这道题的本质是"带不确定性的字符串匹配"。`'*'` 引入了"分支"——在每个 `*` 处，算法必须同时考虑"匹配 0 次"和"匹配多次"两条路径。

动态规划将这些分支系统地组织成一张表，避免重复计算。每个格子 `dp[i][j]` 相当于问一个子问题："s 的前 i 个字符能否被 p 的前 j 个字符匹配？"，大问题的答案依赖小问题的结果，这正是动态规划的核心思想。

**记忆点：** 遇到 `p[j-1] == '*'` 时，优先写"匹配 0 次"的转移 `dp[i][j-2]`，然后再考虑"匹配多次"的转移 `dp[i-1][j]`（需要当前字符能匹配）。
