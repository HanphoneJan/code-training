---
title: 最小覆盖子串
platform: LeetCode
difficulty: Hard
id: 76
url: https://leetcode.cn/problems/minimum-window-substring/
tags:
  - 字符串
  - 滑动窗口
  - 哈希表
date_added: 2026-03-25
---

# 76. 最小覆盖子串

## 题目描述

给你一个字符串 `s`、一个字符串 `t`。返回 `s` 中涵盖 `t` 所有字符的最小子串。如果不存在符合条件的子串，则返回空字符串 `""`。

**注意**：
- 对于 `t` 中重复字符，我们寻找的子字符串中该字符数量必须不少于 `t` 中该字符数量。
- 如果 `s` 中存在这样的子串，我们保证它是唯一的答案。

## 示例

**示例 1：**
```
输入：s = "ADOBECODEBANC", t = "ABC"
输出："BANC"
解释：最小覆盖子串 "BANC" 包含来自字符串 t 的 'A'、'B' 和 'C'。
```

**示例 2：**
```
输入：s = "a", t = "a"
输出："a"
解释：整个字符串 s 是最小覆盖子串。
```

**示例 3：**
```
输入：s = "a", t = "aa"
输出：""
解释：t 中两个字符 'a' 均应包含在 s 的子串中，因此没有符合条件的子字符串，返回空字符串。
```

---

## 解题思路

### 第一步：理解问题本质

这是一个经典的**滑动窗口**问题。需要在字符串 s 中找到一个包含 t 所有字符的最小子串。

### 第二步：滑动窗口

**核心洞察**：
- 右指针扩展窗口，直到窗口包含 t 的所有字符
- 左指针收缩窗口，在保证包含 t 所有字符的前提下，寻找最小窗口
- 使用 Counter 判断窗口是否包含 t 的所有字符

---

## 完整代码实现

```python
from collections import Counter

class Solution:
    """
    最小覆盖子串 - 滑动窗口

    核心思想：
    使用滑动窗口在字符串 s 中寻找包含 t 所有字符的最小子串。

    滑动窗口的关键：
    1. 右指针扩展窗口，直到窗口包含 t 的所有字符
    2. 左指针收缩窗口，在保证包含 t 所有字符的前提下，寻找最小窗口
    3. 记录最小窗口的位置

    如何判断窗口包含 t 的所有字符？
    使用 Counter 比较：cnt_s >= cnt_t 表示 s 的子串中每个字符的出现次数
    都不小于 t 中对应字符的出现次数。

    时间复杂度：O(|s| + |t|)
    空间复杂度：O(|s| + |t|)
    """

    def minWindow(self, s: str, t: str) -> str:
        cnt_s = Counter()   # s 的子串中各字符的出现次数
        cnt_t = Counter(t)  # t 中各字符的出现次数

        ans_left, ans_right = -1, len(s)  # 记录最小窗口的左右边界
        left = 0  # 窗口左边界

        for right, c in enumerate(s):  # 右指针扩展窗口
            cnt_s[c] += 1  # 右端点字母移入窗口

            # 当窗口包含 t 的所有字符时，尝试收缩左边界
            while cnt_s >= cnt_t:
                # 更新最小窗口
                if right - left < ans_right - ans_left:
                    ans_left, ans_right = left, right

                # 左端点字母移出窗口
                cnt_s[s[left]] -= 1
                left += 1

        return "" if ans_left < 0 else s[ans_left: ans_right + 1]
```

---

## 复杂度分析

| 解法 | 时间复杂度 | 空间复杂度 |
|------|-----------|-----------|
| 暴力 | O(|s|²) | O(|t|) |
| **滑动窗口（最优）** | **O(|s| + |t|)** | **O(|s| + |t|)** |

---

## 相关题目

- [3. 无重复字符的最长子串](https://leetcode.cn/problems/longest-substring-without-repeating-characters/)
- [438. 找到字符串中所有字母异位词](https://leetcode.cn/problems/find-all-anagrams-in-a-string/)
- [567. 字符串的排列](https://leetcode.cn/problems/permutation-in-string/)
