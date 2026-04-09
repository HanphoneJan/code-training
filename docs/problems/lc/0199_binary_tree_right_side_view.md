---
title: 二叉树的右视图
platform: LeetCode
difficulty: Medium
id: 199
url: https://leetcode.cn/problems/binary-tree-right-side-view/
tags:
  - 树
  - 深度优先搜索
  - 广度优先搜索
  - 二叉树
topics:
  - ../../topics/binary-tree.md
  - ../../topics/bfs.md
patterns:
  - ../../patterns/tree-traversal.md
date_added: 2026-04-09
date_reviewed: []
---

# 199. 二叉树的右视图

## 题目描述

给定一个二叉树的根节点 `root`，想象自己站在它的右侧，按照从顶部到底部的顺序，返回从右侧所能看到的节点值。

## 示例

**示例 1：**
```
输入: [1,2,3,null,5,null,4]
输出: [1,3,4]
解释:
       1            <---
     /   \
    2     3         <---
     \     \
      5     4       <---
```

**示例 2：**
```
输入: [1,2,3,4,null,null,null,5]
输出: [1,3,4,5]
解释:
       1            <---
     /   \
    2     3         <---
   /
  4               <---
 /
5                 <---
```

---

## 解题思路

### 第一步：理解问题本质

"右视图"意味着：**从右侧看，每层只能看到最右边的那个节点**。

所以问题转化为：获取二叉树每一层最右侧的节点值。

### 第二步：暴力解法 - DFS + 记录深度

用 DFS 遍历整棵树，记录每个节点所在的深度。对于每个深度，保留最后访问到的节点值。

```python
def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
    result = []

    def dfs(node, depth):
        if not node:
            return
        # 如果是该深度第一次访问，添加新元素
        # 否则覆盖（后面的就是更靠右的）
        if depth == len(result):
            result.append(node.val)
        else:
            result[depth] = node.val
        dfs(node.left, depth + 1)
        dfs(node.right, depth + 1)

    dfs(root, 0)
    return result
```

**分析**：时间复杂度 O(n)，空间复杂度 O(h)。

### 第三步：优化解法 - DFS 先右后左

调整遍历顺序，先访问右子节点，这样每层第一个访问到的就是最右侧节点。

```python
def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
    result = []

    def dfs(node, depth):
        if not node:
            return
        if depth == len(result):
            result.append(node.val)
        # 先右后左
        dfs(node.right, depth + 1)
        dfs(node.left, depth + 1)

    dfs(root, 0)
    return result
```

**分析**：每层只记录第一个访问的节点，代码更简洁。

### 第四步：最优解法 - BFS 层序遍历

BFS 天然按层遍历，对于每一层，最后一个出队的节点就是最右侧的节点。

---

## 完整代码实现

```python
from typing import List, Optional
from collections import deque

class Solution:
    """
    二叉树的右视图 - BFS层序遍历

    核心思路：
    本质上是返回每一层最右侧的节点。
    使用 BFS 层序遍历，对于每一层，最后一个出队的节点就是该层最右侧的节点。

    时间复杂度：O(n)
    空间复杂度：O(w) - w 为树的最大宽度
    """

    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []

        result = []
        queue = deque([root])

        while queue:
            current_level_size = len(queue)

            for i in range(current_level_size):
                node = queue.popleft()

                # 当前层的最后一个节点，加入结果
                if i == current_level_size - 1:
                    result.append(node.val)

                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)

        return result
```

---

## 示例推演

以 `[1,2,3,null,5,null,4]` 为例：

```
       1
     /   \
    2     3
     \     \
      5     4
```

**BFS 过程**：

| 步骤 | 队列内容 | 当前层大小 | 出队节点 | 是否最右 | 结果 |
|------|----------|------------|----------|----------|------|
| 初始 | [1] | - | - | - | [] |
| 第1层 | [1] | 1 | 1 | 是 | [1] |
| 第2层 | [2,3] | 2 | 2 | 否 | [1] |
| | | | 3 | 是 | [1,3] |
| 第3层 | [5,4] | 2 | 5 | 否 | [1,3] |
| | | | 4 | 是 | [1,3,4] |

最终结果：`[1, 3, 4]`

---

## 复杂度分析

| 解法 | 时间复杂度 | 空间复杂度 | 说明 |
|------|-----------|-----------|------|
| DFS | O(n) | O(h) | h 为树高度，递归栈空间 |
| DFS（先右后左） | O(n) | O(h) | 每层只记录第一个 |
| BFS | O(n) | O(w) | w 为树的最大宽度 |

**注意**：对于平衡二叉树，h = O(log n)，w = O(n)；对于链状树，h = O(n)，w = O(1)。

---

## 易错点总结

### 1. BFS 中判断最右节点的时机

**错误**：在加入子节点时判断

**正确**：在出队时判断是否是当前层最后一个

```python
for i in range(current_level_size):
    node = queue.popleft()
    if i == current_level_size - 1:  # 正确：判断是否是最后一个
        result.append(node.val)
```

### 2. DFS 先左后右 vs 先右后左

```python
# 先右后左：每层第一个就是最右，代码更简洁
dfs(node.right, depth + 1)
dfs(node.left, depth + 1)

# 先左后右：需要覆盖，每层保留最后访问的
dfs(node.left, depth + 1)
dfs(node.right, depth + 1)
```

### 3. 空树处理

```python
if not root:
    return []  # 不是 return None
```

---

## 扩展思考

### 1. 求左视图？

与右视图类似，每层取第一个节点即可：

```python
if i == 0:  # 第一个节点
    result.append(node.val)
```

### 2. 求俯视图？

这是 [987. 二叉树的垂序遍历](https://leetcode.cn/problems/vertical-order-traversal-of-a-binary-tree/) 的简化版。

需要记录每个节点的水平位置（列号），按列号分组，每列取最上面的节点。

### 3. 相关题目

- [102. 二叉树的层序遍历](https://leetcode.cn/problems/binary-tree-level-order-traversal/)
- [107. 二叉树的层序遍历 II](https://leetcode.cn/problems/binary-tree-level-order-traversal-ii/)
- [103. 二叉树的锯齿形层序遍历](https://leetcode.cn/problems/binary-tree-zigzag-level-order-traversal/)
- [987. 二叉树的垂序遍历](https://leetcode.cn/problems/vertical-order-traversal-of-a-binary-tree/)

---

## 相关题目

- [102. 二叉树的层序遍历](https://leetcode.cn/problems/binary-tree-level-order-traversal/)
- [103. 二叉树的锯齿形层序遍历](https://leetcode.cn/problems/binary-tree-zigzag-level-order-traversal/)
- [107. 二叉树的层序遍历 II](https://leetcode.cn/problems/binary-tree-level-order-traversal-ii/)
- [116. 填充每个节点的下一个右侧节点指针](https://leetcode.cn/problems/populating-next-right-pointers-in-each-node/)
