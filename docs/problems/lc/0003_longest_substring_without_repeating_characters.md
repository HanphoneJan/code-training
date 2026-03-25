---
title: 无重复字符的最长子串
platform: LeetCode
difficulty: Medium
id: 3
url: https://leetcode.cn/problems/longest-substring-without-repeating-characters/
tags:
  - 字符串
  - 滑动窗口
  - 哈希表
date_added: 2026-03-25
---

# 3. 无重复字符的最长子串

## 题目描述

给定一个字符串 `s`，请你找出其中不含有重复字符的最长子串的长度。

## 示例

**示例 1：**
```
输入：s = "abcabcbb"
输出：3
解释：因为无重复字符的最长子串是 "abc"，所以其长度为 3。
```

**示例 2：**
```
输入：s = "bbbbb"
输出：1
解释：因为无重复字符的最长子串是 "b"，所以其长度为 1。
```

**示例 3：**
```
输入：s = "pwwkew"
输出：3
解释：因为无重复字符的最长子串是 "wke"，所以其长度为 3。
注意：答案必须是子串，"pwke" 是子序列，不是子串。
```

---

## 解题思路

### 第一步：理解问题本质

这是一个典型的**滑动窗口**问题：
- 需要找到一个连续的子串
- 子串内不能有重复字符
- 求满足条件的子串的最大长度

### 第二步：暴力解法

**思路**：枚举所有子串，检查是否有重复字符，记录最大长度。

```python
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        n = len(s)
        max_len = 0

        for i in range(n):
            seen = set()
            for j in range(i, n):
                if s[j] in seen:
                    break
                seen.add(s[j])
                max_len = max(max_len, j - i + 1)

        return max_len
```

**缺点**：时间复杂度 O(n²)，效率太低。

### 第三步：优化解法 —— 滑动窗口

**核心洞察**：
- 使用左右两个指针表示窗口的边界
- 右指针不断向右扩展窗口
- 当遇到重复字符时，收缩左指针直到窗口内无重复
- 使用哈希表记录字符位置，快速判断重复

**算法步骤**：
1. `left`：窗口左边界，`i`：窗口右边界（当前遍历位置）
2. 哈希表记录每个字符最后一次出现的索引
3. 遍历字符串：
   - 如果当前字符未出现过，窗口直接扩展
   - 如果出现过，收缩左边界到重复字符的下一个位置
   - 更新当前字符的位置
   - 更新最大长度

**为什么正确**：
- 哈希表记录字符最后出现的位置，可以在 O(1) 时间内判断重复
- 左边界只能右移不能左移，保证滑动窗口的正确性
- 每个字符最多被访问两次（被右指针和左指针各一次）

---

## 完整代码实现

```python
class Solution:
    """
    无重复字符的最长子串 - 滑动窗口

    核心思想：
    用滑动窗口维护一个不包含重复字符的子串，窗口右边界不断右移扩展，
    遇到重复字符时收缩左边界，保证窗口内无重复字符。

    为什么用哈希表？
    哈希表记录每个字符最后一次出现的位置，可以在 O(1) 时间内判断字符是否重复，
    并快速确定左边界应该移动到哪里。

    滑动窗口的关键：
    1. left：窗口左边界
    2. i：窗口右边界（当前遍历位置）
    3. hash_dict：记录字符最后一次出现的索引

    时间复杂度：O(n)，每个字符只访问一次
    空间复杂度：O(min(m,n))，m 是字符集大小
    """

    def lengthOfLongestSubstring(self, s: str) -> int:
        hash_dict = {}  # 记录字符最后一次出现的索引
        n = len(s)
        left, ans, result = 0, 0, 0  # left:左边界, ans:当前窗口长度, result:最大长度

        for i in range(0, n):
            if hash_dict.get(s[i], -1) == -1:
                # 字符未出现过，窗口直接扩展
                ans += 1
            else:
                # 字符出现过，需要收缩左边界
                # 注意：left 只能右移不能左移（取 max 保证）
                if left < hash_dict[s[i]]:
                    left = hash_dict[s[i]]
                ans = i - left  # 重新计算当前窗口长度

            hash_dict[s[i]] = i  # 更新字符位置
            result = max(ans, result)  # 更新最大长度

        return result
```

---

## 示例推演

以 `s = "abcabcbb"` 为例：

| i | s[i] | hash_dict | left | ans | result | 说明 |
|---|------|-----------|------|-----|--------|------|
| 0 | 'a' | {} | 0 | 1 | 1 | 首次出现，窗口扩展 |
| 1 | 'b' | {'a':0} | 0 | 2 | 2 | 首次出现，窗口扩展 |
| 2 | 'c' | {'a':0,'b':1} | 0 | 3 | 3 | 首次出现，窗口扩展 |
| 3 | 'a' | {'a':0,'b':1,'c':2} | 0→1 | 2 | 3 | 'a'重复，left移到1 |
| 4 | 'b' | {'a':3,'b':1,'c':2} | 1→2 | 2 | 3 | 'b'重复，left移到2 |
| 5 | 'c' | {'a':3,'b':4,'c':2} | 2→3 | 2 | 3 | 'c'重复，left移到3 |
| 6 | 'b' | {'a':3,'b':4,'c':5} | 3→5 | 1 | 3 | 'b'重复，left移到5 |
| 7 | 'b' | {'a':3,'b':6,'c':5} | 5→7 | 0 | 3 | 'b'重复，left移到7 |

**结果**：3（最长子串为 "abc"）

再以一个特殊例子 `s = "abba"` 为例：

| i | s[i] | hash_dict | left | 说明 |
|---|------|-----------|------|------|
| 0 | 'a' | {} | 0 | - |
| 1 | 'b' | {'a':0} | 0 | - |
| 2 | 'b' | {'a':0,'b':1} | 0→2 | 'b'重复，left移到2 |
| 3 | 'a' | {'a':0,'b':2} | 2 | hash_dict['a']=0 < left=2，不更新left |

**关键点**：当 `hash_dict[s[i]] < left` 时，说明这个字符虽然之前出现过，但已经在窗口外了，不需要收缩左边界。这就是为什么代码中要判断 `if left < hash_dict[s[i]]`。

---

## 复杂度分析

| 解法 | 时间复杂度 | 空间复杂度 | 说明 |
|------|-----------|-----------|------|
| 暴力 | O(n²) | O(min(m,n)) | 枚举所有子串 |
| **滑动窗口（最优）** | **O(n)** | **O(min(m,n))** | m是字符集大小 |

---

## 易错点总结

### 1. 左边界更新要取 max

```python
# 错误写法
left = hash_dict[s[i]]

# 正确写法
if left < hash_dict[s[i]]:
    left = hash_dict[s[i]]
```

原因：左边界只能右移，如果重复字符在窗口左边界的左边，不需要更新左边界。

### 2. 窗口长度的计算

```python
ans = i - left  # 不是 i - left + 1
```

原因：left 是重复字符的索引，新的窗口应该从重复字符的下一个位置开始，所以是 `i - left`。

### 3. 先更新结果还是先更新哈希表？

先更新哈希表，再计算结果。因为当前字符已经算入窗口。

---

## 扩展思考

### 1. 如何返回最长子串本身？

记录最大长度时，同时记录起始位置，最后截取子串。

### 2. 如果最多允许 k 个重复字符？

使用一个计数器记录窗口内每个字符的出现次数，当不同字符的数量超过 k 时收缩窗口。

### 3. 滑动窗口的通用模板

```python
def sliding_window(s):
    left = 0
    window = {}
    for right in range(len(s)):
        # 扩大窗口，加入 s[right]
        window[s[right]] = window.get(s[right], 0) + 1

        # 收缩窗口的条件
        while 需要收缩:
            # 移除 s[left]
            window[s[left]] -= 1
            left += 1

        # 更新结果
        update_result()
```

---

## 相关题目

- [76. 最小覆盖子串](https://leetcode.cn/problems/minimum-window-substring/)
- [567. 字符串的排列](https://leetcode.cn/problems/permutation-in-string/)
- [438. 找到字符串中所有字母异位词](https://leetcode.cn/problems/find-all-anagrams-in-a-string/)
- [209. 长度最小的子数组](https://leetcode.cn/problems/minimum-size-subarray-sum/)
