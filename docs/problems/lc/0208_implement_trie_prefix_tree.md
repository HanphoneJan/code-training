---
title: 实现 Trie (前缀树)
platform: LeetCode
difficulty: Medium
id: 208
url: https://leetcode.cn/problems/implement-trie-prefix-tree/
tags:
  - 设计
  - 字典树
  - 哈希表
  - 字符串
topics:
  - ../../topics/trie.md
patterns:
  - ../../patterns/prefix-tree.md
date_added: 2026-04-09
date_reviewed: []
---

# 208. 实现 Trie (前缀树)

## 题目描述

**Trie**（发音类似 "try"），又称**前缀树**或**字典树**，是一种有序树，用于保存关联数组，其中的键通常是字符串。

实现 Trie 类：
- `Trie()` 初始化前缀树对象
- `void insert(String word)` 向前缀树中插入字符串 `word`
- `boolean search(String word)` 如果字符串 `word` 在前缀树中，返回 `true`；否则，返回 `false`
- `boolean startsWith(String prefix)` 如果之前已经插入的字符串 `word` 的前缀之一为 `prefix`，返回 `true`；否则，返回 `false`

## 示例

```
输入
["Trie", "insert", "search", "search", "startsWith", "insert", "search"]
[[], ["apple"], ["apple"], ["app"], ["app"], ["app"], ["app"]]

输出
[null, null, true, false, true, null, true]

解释
Trie trie = new Trie();
trie.insert("apple");
trie.search("apple");   // 返回 True
trie.search("app");     // 返回 False
trie.startsWith("app"); // 返回 True
trie.insert("app");
trie.search("app");     // 返回 True
```

---

## 解题思路

### 第一步：理解问题本质

Trie 是一种**树形数据结构**，用于高效地存储和检索字符串集合。核心特点是：
- **共享前缀**：具有相同前缀的字符串共享路径
- **快速查找**：查找时间只与字符串长度有关，与集合大小无关

### 第二步：暴力解法 - 哈希表

用哈希表存储所有单词，搜索时遍历所有单词检查。

```python
class Trie:
    def __init__(self):
        self.words = set()
        self.prefixes = set()

    def insert(self, word: str) -> None:
        self.words.add(word)
        for i in range(len(word)):
            self.prefixes.add(word[:i+1])
```

**为什么不够好**：
- 空间复杂度高，每个前缀都要存储
- 无法实现前缀相关的扩展功能（如自动补全）

### 第三步：优化解法 - 链表式 Trie

每个节点用字典存储子节点，适用于字符集较大的情况。

```python
class TrieNode:
    def __init__(self):
        self.children = {}  # 字典存储子节点
        self.is_end = False
```

### 第四步：最优解法 - 数组式 Trie

假设只包含小写字母，用固定大小数组存储子节点，访问更快。

---

## 完整代码实现

```python
class TrieNode:
    """Trie 节点类"""
    __slots__ = ['son', 'end']

    def __init__(self):
        self.son = [None] * 26  # 子节点数组
        self.end = False        # 标记单词结束


class Trie:
    """
    实现 Trie (前缀树)

    核心思想：
    利用字符串的公共前缀来减少查询时间。

    时间复杂度：
    - insert: O(m) - m 为单词长度
    - search: O(m)
    - startsWith: O(m)
    """

    def __init__(self):
        self.root = TrieNode()

    def insert(self, word: str) -> None:
        cur = self.root
        for c in word:
            idx = ord(c) - ord('a')
            if cur.son[idx] is None:
                cur.son[idx] = TrieNode()
            cur = cur.son[idx]
        cur.end = True

    def search(self, word: str) -> bool:
        cur = self.root
        for c in word:
            idx = ord(c) - ord('a')
            if cur.son[idx] is None:
                return False
            cur = cur.son[idx]
        return cur.end

    def startsWith(self, prefix: str) -> bool:
        cur = self.root
        for c in prefix:
            idx = ord(c) - ord('a')
            if cur.son[idx] is None:
                return False
            cur = cur.son[idx]
        return True
```

---

## 示例推演

插入 `"apple"` 和 `"app"` 后的 Trie 结构：

```
        root
         |
         a
         |
         p
         |
         p (end=True)  <-- "app" 结束
         |
         l
         |
         e (end=True)  <-- "apple" 结束
```

**insert("apple") 过程**：

| 步骤 | 字符 | 操作 | 当前节点 |
|------|------|------|----------|
| 1 | 'a' | 创建节点 | root -> a |
| 2 | 'p' | 创建节点 | a -> p |
| 3 | 'p' | 创建节点 | p -> p |
| 4 | 'l' | 创建节点 | p -> l |
| 5 | 'e' | 创建节点，标记 end | l -> e (end) |

**search("app") 过程**：

| 步骤 | 字符 | 操作 | 结果 |
|------|------|------|------|
| 1 | 'a' | 找到子节点 | 继续 |
| 2 | 'p' | 找到子节点 | 继续 |
| 3 | 'p' | 找到子节点，检查 end | end=False，返回 False |

---

## 复杂度分析

| 操作 | 时间复杂度 | 空间复杂度 | 说明 |
|------|-----------|-----------|------|
| insert | O(m) | O(m) | m 为单词长度 |
| search | O(m) | O(1) | |
| startsWith | O(m) | O(1) | |

**空间复杂度分析**：
- 最坏情况：O(26^n)，无共享前缀
- 最好情况：O(总字符数)，完全共享前缀

---

## 易错点总结

### 1. 忘记标记 end

**错误**：插入后没有设置 `cur.end = True`

**正确**：
```python
def insert(self, word: str) -> None:
    cur = self.root
    for c in word:
        # ... 遍历
        cur = cur.son[idx]
    cur.end = True  # 必须标记！
```

### 2. search 和 startsWith 的区别

```python
def search(self, word: str) -> bool:
    node = self._find(word)
    return node is not None and node.end  # 必须检查 end

def startsWith(self, prefix: str) -> bool:
    return self._find(prefix) is not None  # 不需要检查 end
```

### 3. 字符索引计算

```python
# 正确：小写字母转索引
idx = ord(c) - ord('a')  # 'a' -> 0, 'b' -> 1, ...

# 如果是大写字母或其他字符，需要调整
```

---

## 扩展思考

### 1. 支持删除操作

需要引用计数或父指针，删除时清理无用节点。

### 2. 统计前缀出现次数

每个节点增加 `count` 字段，insert 时递增。

### 3. 自动补全功能

找到前缀节点后，DFS 遍历所有子节点收集单词。

### 4. 相关题目

- [208. 实现 Trie](https://leetcode.cn/problems/implement-trie-prefix-tree/)
- [211. 添加与搜索单词](https://leetcode.cn/problems/design-add-and-search-words-data-structure/) - 支持通配符
- [212. 单词搜索 II](https://leetcode.cn/problems/word-search-ii/) - Trie + DFS
- [421. 数组中两个数的最大异或值](https://leetcode.cn/problems/maximum-xor-of-two-numbers-in-an-array/) - 二进制 Trie
- [648. 单词替换](https://leetcode.cn/problems/replace-words/)

---

## 相关题目

- [211. 添加与搜索单词 - 数据结构设计](https://leetcode.cn/problems/design-add-and-search-words-data-structure/)
- [212. 单词搜索 II](https://leetcode.cn/problems/word-search-ii/)
- [421. 数组中两个数的最大异或值](https://leetcode.cn/problems/maximum-xor-of-two-numbers-in-an-array/)
- [648. 单词替换](https://leetcode.cn/problems/replace-words/)
- [677. 键值映射](https://leetcode.cn/problems/map-sum-pairs/)
