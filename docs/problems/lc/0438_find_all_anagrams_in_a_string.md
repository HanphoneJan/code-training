---
title: 找到字符串中所有字母异位词
platform: LeetCode
difficulty: Medium
id: 438
url: https://leetcode.cn/problems/find-all-anagrams-in-a-string/
tags:
  - 字符串
  - 哈希表
  - 滑动窗口
topics:
  - ../../topics/sliding-window.md
  - ../../topics/hash-table.md
patterns:
  - ../../patterns/fixed-size-window.md
date_added: 2026-04-09
date_reviewed: []
---

# 438. 找到字符串中所有字母异位词

## 题目描述

给定两个字符串 `s` 和 `p`，找到 `s` 中所有 `p` 的 **异位词** 的子串，返回这些子串的起始索引。不考虑答案输出的顺序。

**异位词** 指由相同字母以相同数量组成的字符串，即字母相同但排列顺序可能不同。

**示例 1：**
```
输入: s = "cbaebabacd", p = "abc"
输出: [0,6]
解释:
起始索引等于 0 的子串是 "cba"，它是 "abc" 的异位词。
起始索引等于 6 的子串是 "bac"，它是 "abc" 的异位词。
```

**示例 2：**
```
输入: s = "abab", p = "ab"
输出: [0,1,2]
解释:
起始索引等于 0 的子串是 "ab"，它是 "ab" 的异位词。
起始索引等于 1 的子串是 "ba"，它是 "ab" 的异位词。
起始索引等于 2 的子串是 "ab"，它是 "ab" 的异位词。
```

---

## 解题思路

### 第一步：理解问题本质

这道题的核心是**判断两个字符串是否为异位词**。

异位词的判断方法：
- 排序后相等
- 字符频率相同（哈希表/数组）

由于需要在 s 中找所有长度为 len(p) 的子串，这是一个典型的**滑动窗口**问题。

### 第二步：暴力解法

**思路：** 枚举 s 中所有长度为 len(p) 的子串，排序后与 p 比较。

```python
class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        k = len(p)
        n = len(s)
        std = sorted(p)
        ans = []
        
        for i in range(n - k + 1):
            substr = s[i:i + k]
            if sorted(substr) == std:
                ans.append(i)
        
        return ans
```

**为什么不够好？** 每次排序需要 O(k log k)，总时间复杂度 O(n × k log k)，会超时。

### 第三步：优化解法 - 滑动窗口 + 哈希表

**关键洞察：** 滑动窗口移动时，只有首尾两个字符发生变化，可以利用这个特点优化。

**思路：**
1. 用 Counter 统计 p 的字符频率
2. 维护一个大小为 len(p) 的滑动窗口
3. 窗口滑动时，左边字符出窗，右边字符入窗
4. 比较两个 Counter 是否相等

```python
from collections import Counter

class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        cnt_p = Counter(p)
        cnt_s = Counter()
        ans = []
        k = len(p)
        
        for right, c in enumerate(s):
            cnt_s[c] += 1
            left = right - k + 1
            
            if left < 0:
                continue
            
            if cnt_s == cnt_p:
                ans.append(left)
            
            cnt_s[s[left]] -= 1
        
        return ans
```

### 第四步：最优解法 - 数组 + 差值计数

**关键洞察：** 字符只有 26 个小写字母，可以用固定大小的数组代替 Counter，比较更快。

**进一步优化：** 维护一个「差异计数器」，记录窗口与 p 有多少个字符的频率不同。

```python
class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        m, n = len(s), len(p)
        if m < n:
            return []
        
        cnt = [0] * 26  # 差值数组
        
        # 初始化：p 中的字符加 1，s 中前 n 个字符减 1
        for i in range(n):
            cnt[ord(p[i]) - ord('a')] += 1
            cnt[ord(s[i]) - ord('a')] -= 1
        
        ans = []
        if self.all_zero(cnt):
            ans.append(0)
        
        # 滑动窗口
        for i in range(n, m):
            cnt[ord(s[i]) - ord('a')] -= 1      # 右边进入
            cnt[ord(s[i - n]) - ord('a')] += 1  # 左边离开
            
            if self.all_zero(cnt):
                ans.append(i - n + 1)
        
        return ans
    
    def all_zero(self, cnt):
        return all(c == 0 for c in cnt)
```

---

## 完整代码实现

```python
from typing import List
from collections import Counter

class Solution:
    """
    找到字符串中所有字母异位词 - 滑动窗口

    核心思路：
    使用滑动窗口 + Counter 来比较窗口内的字符频率。
    维护一个大小为 len(p) 的窗口，滑动时更新字符计数。

    时间复杂度: O(n × m) - m 是字符集大小（26）
    空间复杂度: O(m)
    """
    def findAnagrams(self, s: str, p: str) -> List[int]:
        cnt_p = Counter(p)  # 统计 p 的字符频率
        cnt_s = Counter()   # 统计窗口的字符频率
        ans = []
        k = len(p)

        for right, c in enumerate(s):
            cnt_s[c] += 1   # 右端点字母进入窗口

            left = right - k + 1
            if left < 0:    # 窗口长度不足 k
                continue

            if cnt_s == cnt_p:
                ans.append(left)

            cnt_s[s[left]] -= 1   # 左端点字母离开窗口

        return ans
```

---

## 示例推演

以 `s = "cbaebabacd", p = "abc"` 为例：

**初始化：**
- `cnt_p = {'a': 1, 'b': 1, 'c': 1}`
- 窗口大小 k = 3

**滑动过程：**

| 步骤 | 右端点 | 窗口内容 | cnt_s | 是否匹配 | 左端点离开 |
|------|--------|----------|-------|----------|-----------|
| 1 | c | c | {'c':1} | - | - |
| 2 | b | cb | {'c':1,'b':1} | - | - |
| 3 | a | cba | {'c':1,'b':1,'a':1} | 匹配(0) | c |
| 4 | e | bae | {'b':1,'a':1,'e':1} | 不匹配 | b |
| 5 | b | aeb | {'a':1,'e':1,'b':1} | 不匹配 | a |
| 6 | a | eba | {'e':1,'b':1,'a':1} | 不匹配 | e |
| 7 | b | bab | {'b':2,'a':1} | 不匹配 | b |
| 8 | a | aba | {'a':2,'b':1} | 不匹配 | a |
| 9 | c | bac | {'b':1,'a':1,'c':1} | 匹配(6) | b |
| 10 | d | acd | {'a':1,'c':1,'d':1} | 不匹配 | a |

**结果：** `[0, 6]`

---

## 复杂度分析

| 解法 | 时间复杂度 | 空间复杂度 | 说明 |
|------|-----------|-----------|------|
| 暴力排序 | O(n × k log k) | O(k) | 每次排序比较 |
| Counter | O(n × m) | O(m) | m=26 为字符集大小 |
| 数组+差值 | O(n) | O(1) | 固定大小数组 |

**说明：**
- n 是字符串 s 的长度
- k 是字符串 p 的长度
- m 是字符集大小（本题固定为 26）

---

## 易错点总结

### 1. 窗口边界处理

```python
# 计算左端点位置
left = right - k + 1

# 检查窗口是否已满
if left < 0:
    continue
```

### 2. Counter 比较的时机

```python
# 先比较，再将左端点移出
if cnt_s == cnt_p:
    ans.append(left)
cnt_s[s[left]] -= 1
```

### 3. 字符计数为 0 的处理

```python
# Counter 中计数为 0 的键不会被删除
# 但这不影响比较结果
```

---

## 扩展思考

### 1. 如果字符集扩大？

如果包含所有 ASCII 字符，数组大小设为 128 或 256 即可，依然是 O(1) 空间。

### 2. 如果要求返回所有异位词本身？

```python
return [s[i:i+k] for i in ans]
```

### 3. 相关题目

- [567. 字符串的排列](https://leetcode.cn/problems/permutation-in-string/) - 判断是否存在异位词
- [76. 最小覆盖子串](https://leetcode.cn/problems/minimum-window-substring/) - 滑动窗口求最小覆盖
- [3. 无重复字符的最长子串](https://leetcode.cn/problems/longest-substring-without-repeating-characters/) - 滑动窗口变长

---

## 相关题目

- [567. 字符串的排列](https://leetcode.cn/problems/permutation-in-string/)
- [76. 最小覆盖子串](https://leetcode.cn/problems/minimum-window-substring/)
- [3. 无重复字符的最长子串](https://leetcode.cn/problems/longest-substring-without-repeating-characters/)
