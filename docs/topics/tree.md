---
title: 树
category: 数据结构
difficulty_range: [简单, 困难]
last_updated: 2026-03-23
---

# 树

![树的示例图1.webp](https://hanphone.top/gh/HanphoneJan/public-pictures/datastructure/%E6%A0%91%E7%9A%84%E7%A4%BA%E4%BE%8B%E5%9B%BE1.webp)

## 知识点概述

树是一种非线性数据结构，由节点和边组成，具有层次关系。

### 核心特性

- **层次结构**：节点之间具有父子关系
- **无环**：任意两个节点间只有一条路径
- **根节点**：树的起始节点
- **叶节点**：没有子节点的节点

### 基本术语

- **节点**：树中的每个元素都可以统称为节点
- **根节点**：顶层节点或者说没有父节点的节点
- **父节点**：若一个节点含有子节点，则这个节点称为其子节点的父节点
- **子节点**：一个节点含有的子树的根节点称为该节点的子节点
- **兄弟节点**：具有相同父节点的节点互称为兄弟节点
- **叶子节点**：没有子节点的节点
- **节点的高度**：该节点到叶子节点的最长路径所包含的边数。叶子的高度为0
- **节点的深度**：根节点到该节点的路径所包含的边数。根的深度为0
- **节点的层数**：节点的深度+1
- **树的高度**：根节点的高度

## 树的分类

### 1. 二叉树

每个节点最多有两个子节点。

**类型：**
- 满二叉树
- 完全二叉树
- 二叉搜索树（BST）
- 平衡二叉树（AVL）

### 2. N 叉树

每个节点可以有多个子节点。

N叉树没有中序遍历的概念，只有前序、后序和层序遍历。

```python
# N叉树节点定义
class Node:
    def __init__(self, val=0, children=None):
        self.val = val
        self.children = children if children else []

# N叉树前序遍历
def preorder(self, root: 'Node') -> List[int]:
    res = []
    if root is None:
        return res
    res.append(root.val)
    for child in root.children:
        res += self.preorder(child)
    return res

# N叉树前序遍历（迭代）
def preorder(self, root: 'Node') -> List[int]:
    if root is None:
        return []
    res = []
    stk = [root]
    while stk:
        node = stk.pop()
        res.append(node.val)
        stk.extend(reversed(node.children))  # 反转保证顺序
    return res
```

### 3. 特殊树

- **Trie（前缀树）**
- **线段树**
- **树状数组**
- **B树 / B+树**（数据库索引）

**B树**：平衡多路搜索树，每个节点最多有m个子节点，适用于磁盘索引场景（减少I/O次数）。

**B+树**：所有叶子节点包含全部关键字及指向数据的指针，且叶子节点按顺序链接（便于范围查询），数据库索引常用。

### 4. 红黑树

一种自平衡二叉查找树，确保最坏情况下的时间复杂度为 O(log n)。

## 遍历方法

### 递归遍历

```python
# 前序遍历
def preorder(root):
    if not root:
        return
    visit(root)          # 访问根节点
    preorder(root.left)  # 遍历左子树
    preorder(root.right) # 遍历右子树

# 中序遍历
def inorder(root):
    if not root:
        return
    inorder(root.left)   # 遍历左子树
    visit(root)          # 访问根节点
    inorder(root.right)  # 遍历右子树

# 后序遍历
def postorder(root):
    if not root:
        return
    postorder(root.left)  # 遍历左子树
    postorder(root.right) # 遍历右子树
    visit(root)           # 访问根节点
```

### 迭代遍历

使用栈实现非递归遍历。

**核心思想**：调用自己是"递"，return就是"归"。迭代解法本质是在模拟递归，使用Stack来模拟系统栈。

| 遍历方式 | 顺序 | 根节点处理时机 | 能否 "边走边处理" |
|---------|------|---------------|------------------|
| 前序 | 根→左→右 | 第一次遇到根节点就处理 | ✅ 完全同步 |
| 中序 | 左→根→右 | 左子树遍历完，第一次弹栈时处理 | ✅ 基本同步 |
| 后序 | 左→右→根 | 左右子树都遍历完，第二次遇到根才处理 | ❌ 必须"回头处理" |

```python
# 前序遍历（迭代）
def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
    res = []
    stk = []
    while root or stk:
        while root:
            res.append(root.val)  # 先处理根节点
            stk.append(root)
            root = root.left
        root = stk.pop()
        root = root.right
    return res

# 中序遍历（迭代）
def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
    res = []
    stk = []
    while root or stk:
        while root:
            stk.append(root)
            root = root.left
        root = stk.pop()
        res.append(root.val)  # 左子树处理完再处理根
        root = root.right
    return res

# 后序遍历（迭代）- 使用逆前序的方法
# 后序：左→右→根，可以看作：根→右→左 的逆序
# 所以用类似前序的方法，但是先遍历右子树，最后反转结果
def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
    if not root:
        return []
    res = []
    stk = []
    while root or stk:
        while root:
            res.append(root.val)
            stk.append(root)
            root = root.right  # 先遍历右子树
        root = stk.pop()
        root = root.left
    return res[::-1]  # 反转得到结果
```

### 层序遍历

使用队列实现 BFS。

```python
from collections import deque

def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
    if not root:
        return []
    res = []
    cur = deque([root])
    while cur:
        level = []
        for _ in range(len(cur)):
            node = cur.popleft()
            level.append(node.val)
            if node.left:
                cur.append(node.left)
            if node.right:
                cur.append(node.right)
        res.append(level)
    return res
```

## 常见题型

### 1. 遍历

- 前序遍历
- 中序遍历
- 后序遍历
- 层序遍历

**相关题目：**
- TBD

### 2. 递归

- 树的深度
- 路径和
- 翻转树

### 3. 构造

- 从遍历序列构造树
- 最近公共祖先

## 解题技巧

### 技巧 1：递归三要素

1. 确定递归函数的参数和返回值
2. 确定终止条件
3. 确定单层递归的逻辑

### 技巧 2：DFS vs BFS

- **DFS**：深度优先，使用递归或栈
- **BFS**：广度优先，使用队列，适合层序遍历

### 技巧 3：分治思想

将树分为根节点、左子树、右子树三部分。

## 相关知识点

- [二叉树](binary_tree)
- [二叉搜索树](binary_search_tree)
- [DFS 模式](../patterns/dfs)
- [BFS 模式](../patterns/bfs)
- [递归模式](../patterns/recursion)

## 题目列表

**简单：**
- TBD

**中等：**
- TBD

**困难：**
- TBD

## 学习路径

1. 掌握基本遍历方法
2. 理解递归本质
3. 练习 DFS 和 BFS
4. 学习特殊树结构
