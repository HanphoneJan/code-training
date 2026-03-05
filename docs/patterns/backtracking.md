---
title: 回溯
category: 算法模式
difficulty: 中等
applicable_to:
  - 组合
  - 排列
  - 子集
last_updated: 2026-03-05
---

# 回溯

## 模式要点

回溯是在递归的基础上，尝试所有可能的解，并在不满足条件时回退，撤销上一步的决策。

**何时使用回溯**：如果在某个选择上不确定它是否能得到想要的答案，或者在相同情况下其他选择也可能得到答案，那么需要用回溯来枚举所有可能。

**核心框架**：
- 选择（做选择）
- 递归（进入下一层决策树）
- 撤销选择（恢复现场）

## 回溯三问

1. **当前操作是什么？**
2. **子问题是什么？**
3. **下一个子问题是什么？**

## 常见题型

- 组合/排列/子集
- 棋盘搜索
- 树的路径问题

## 子集型回溯

子集型回溯有两种常用写法：

### 方法一：选或不选

每个元素有两种选择：选 或 不选。只有到达叶子节点时才构成完整解。

```python
def subsets(self, nums: List[int]) -> List[List[int]]:
    n = len(nums)
    ans = []
    path = []

    def dfs(i: int) -> None:
        if i == n:  # 子集构造完毕
            ans.append(path.copy())
            return

        # 不选 nums[i]
        dfs(i + 1)

        # 选 nums[i]
        path.append(nums[i])
        dfs(i + 1)
        path.pop()  # 恢复现场

    dfs(0)
    return ans
```

### 方法二：枚举

每个节点都是解，枚举从当前位置开始所有可能的选择。

```python
def subsets(self, nums: List[int]) -> List[List[int]]:
    n = len(nums)
    ans = []
    path = []

    def dfs(i: int) -> None:
        ans.append(path.copy())  # 每个节点都是解
        for j in range(i, n):    # 枚举选择的数字
            path.append(nums[j])
            dfs(j + 1)
            path.pop()           # 恢复现场

    dfs(0)
    return ans
```

## 二叉树回溯

### 路径总和 II

[113. 路径总和 II](https://leetcode.cn/problems/path-sum-ii/)

```python
def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
    ans = []
    path = []

    def findPath(root: Optional[TreeNode], targetSum: int) -> None:
        if not root:
            return
        path.append(root.val)
        if not root.left and not root.right and targetSum == root.val:
            ans.append(list(path))
        else:
            findPath(root.left, targetSum - root.val)
            findPath(root.right, targetSum - root.val)
        path.pop()  # 恢复现场

    findPath(root, targetSum)
    return ans
```

## 剪枝技巧

- **可行性剪枝**：当前选择不满足约束条件时停止搜索
- **最优性剪枝**：当前路径不可能得到最优解时停止搜索
- **重复性剪枝**：避免重复计算相同状态
