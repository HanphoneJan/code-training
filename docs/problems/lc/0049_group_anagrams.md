---
title: 字母异位词分组
platform: LeetCode
difficulty: Medium
id: 49
url: https://leetcode.cn/problems/group-anagrams/
tags:
  - 字符串
  - 哈希表
  - 排序
date_added: 2026-03-25
---

# 49. 字母异位词分组

## 题目描述

给你一个字符串数组，请你将 **字母异位词** 组合在一起。可以按任意顺序返回结果列表。

**字母异位词** 是由重新排列源单词的所有字母得到的一个新单词。

## 示例

**示例 1：**
```
输入: strs = ["eat", "tea", "tan", "ate", "nat", "bat"]
输出: [["bat"],["nat","tan"],["ate","eat","tea"]]
```

**示例 2：**
```
输入: strs = [""]
输出: [[""]]
```

**示例 3：**
```
输入: strs = ["a"]
输出: [["a"]]
```

---

## 解题思路

### 第一步：理解问题本质

字母异位词的特点是：**排序后的字符串相同**。

例如：
- "eat", "tea", "ate" 排序后都是 "aet"
- "tan", "nat" 排序后都是 "ant"

### 第二步：暴力解法

**思路**：对每个字符串，检查其他字符串是否是它的异位词。

```python
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        n = len(strs)
        used = [False] * n
        result = []

        for i in range(n):
            if used[i]:
                continue
            group = [strs[i]]
            used[i] = True
            for j in range(i + 1, n):
                if not used[j] and sorted(strs[i]) == sorted(strs[j]):
                    group.append(strs[j])
                    used[j] = True
            result.append(group)

        return result
```

**缺点**：时间复杂度 O(n² × k log k)，效率太低。

### 第三步：最优解法 —— 哈希表

**核心洞察**：
- 异位词排序后的结果相同，可以作为 key
- 使用哈希表将相同 key 的字符串分到同一组

**算法步骤**：
1. 创建一个空哈希表
2. 遍历每个字符串：
   - 将字符串排序作为 key
   - 将原字符串加入 key 对应的列表
3. 返回哈希表的所有值

**为什么正确**：
- 异位词排序后必然相同，所以会被分到同一组
- 非异位词排序后不同，会被分到不同组

---

## 完整代码实现

```python
from typing import List

class Solution:
    """
    字母异位词分组 - 哈希表

    核心思想：
    字母异位词（anagram）的特点是：排序后的字符串相同。
    例如 "eat", "tea", "ate" 排序后都是 "aet"。

    算法步骤：
    1. 遍历每个字符串，将其排序作为 key
    2. 将原字符串加入 key 对应的列表
    3. 返回所有列表

    为什么用排序作为 key？
    因为异位词的字母组成完全相同，排序后必然相同。

    时间复杂度：O(n * k log k)，n 是字符串数量，k 是最大字符串长度
    空间复杂度：O(n * k)
    """

    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagrams = {}
        for s in strs:
            key = ''.join(sorted(s))  # 排序作为 key
            if key not in anagrams:
                anagrams[key] = []
            anagrams[key].append(s)
        return list(anagrams.values())
```

---

## 示例推演

以 `strs = ["eat","tea","tan","ate","nat","bat"]` 为例：

| 字符串 | 排序后 | 哈希表状态 |
|--------|--------|-----------|
| "eat" | "aet" | {"aet": ["eat"]} |
| "tea" | "aet" | {"aet": ["eat", "tea"]} |
| "tan" | "ant" | {"aet": ["eat", "tea"], "ant": ["tan"]} |
| "ate" | "aet" | {"aet": ["eat", "tea", "ate"], "ant": ["tan"]} |
| "nat" | "ant" | {"aet": [...], "ant": ["tan", "nat"]} |
| "bat" | "abt" | {"aet": [...], "ant": [...], "abt": ["bat"]} |

**结果**：[ ["eat","tea","ate"], ["tan","nat"], ["bat"] ]

---

## 复杂度分析

| 解法 | 时间复杂度 | 空间复杂度 | 说明 |
|------|-----------|-----------|------|
| 暴力 | O(n² × k log k) | O(n × k) | 两两比较 |
| **哈希表（最优）** | **O(n × k log k)** | **O(n × k)** | n是字符串数量，k是最大长度 |

---

## 易错点总结

### 1. key 的生成

```python
key = ''.join(sorted(s))  # 正确
key = sorted(s)           # 错误，返回的是列表，不能作为字典 key
```

### 2. 空字符串的处理

空字符串排序后仍是空字符串，可以正常处理。

### 3. 使用 defaultdict 简化代码

```python
from collections import defaultdict

anagrams = defaultdict(list)
for s in strs:
    anagrams[''.join(sorted(s))].append(s)
return list(anagrams.values())
```

---

## 扩展思考

### 1. 如果不使用排序？

可以用字符计数作为 key。例如 "eat" 的计数是 `a:1, e:1, t:1`，可以表示为字符串 `"1#1#1#0#..."` 或元组 `(1,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0)`。

时间复杂度可以优化到 O(n × k)。

### 2. 如果需要返回每组内排序后的结果？

可以在返回前对每个组进行排序。

---

## 相关题目

- [242. 有效的字母异位词](https://leetcode.cn/problems/valid-anagram/)
- [438. 找到字符串中所有字母异位词](https://leetcode.cn/problems/find-all-anagrams-in-a-string/)
