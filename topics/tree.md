---
title: 树
category: 数据结构
difficulty_range: [简单, 困难]
last_updated: 2026-02-25
---

# 树

## 知识点概述

树是一种非线性数据结构，由节点和边组成，具有层次关系。

### 核心特性

- **层次结构**：节点之间具有父子关系
- **无环**：任意两个节点间只有一条路径
- **根节点**：树的起始节点
- **叶节点**：没有子节点的节点

### 基本术语

- **深度**：从根节点到当前节点的边数
- **高度**：从当前节点到最远叶节点的边数
- **层**：深度相同的节点集合

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

### 3. 特殊树

- Trie（前缀树）
- 线段树
- 树状数组

## 常见题型

### 1. 遍历

- 前序遍历
- 中序遍历
- 后序遍历
- 层序遍历

**相关题目：**
- [102. 二叉树的层序遍历](../problems/lc/0102_level_order.md)

### 2. 递归

- 树的深度
- 路径和
- 翻转树

### 3. 构造

- 从遍历序列构造树
- 最近公共祖先

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

### 层序遍历

使用队列实现 BFS。

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

- [二叉树](binary_tree.md)
- [二叉搜索树](binary_search_tree.md)
- [DFS 模式](../patterns/dfs.md)
- [BFS 模式](../patterns/bfs.md)
- [递归模式](../patterns/recursion.md)

## 题目列表

**简单：**
- TBD

**中等：**
- [102. 二叉树的层序遍历](../problems/lc/0102_level_order.md)

**困难：**
- TBD

## 学习路径

1. 掌握基本遍历方法
2. 理解递归本质
3. 练习 DFS 和 BFS
4. 学习特殊树结构
