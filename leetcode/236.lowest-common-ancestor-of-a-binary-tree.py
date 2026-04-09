#
# @lc app=leetcode.cn id=236 lang=python3
# @lcpr version=30204
#
# [236] 二叉树的最近公共祖先
#

# @lcpr-template-start
from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
# @lcpr-template-end
# @lc code=start
class Solution:
    """
    二叉树的最近公共祖先 - 递归法

    问题描述：
    给定一个二叉树, 找到该树中两个指定节点的最近公共祖先。
    最近公共祖先的定义为：对于有根树 T 的两个节点 p、q，
    最近公共祖先表示为一个节点 x，满足 x 是 p、q 的祖先且 x 的深度尽可能大
    （一个节点也可以是它自己的祖先）。

    题目保证：
    - 所有 Node.val 互不相同
    - p != q
    - p 和 q 均存在于给定的二叉树中

    核心思路：
    递归遍历树，对于每个节点：
    1. 如果当前节点是 p 或 q，返回当前节点
    2. 递归在左子树和右子树中查找 p 和 q
    3. 如果左右子树都找到了，说明当前节点是 LCA
    4. 如果只有一边找到，返回那一边的结果

    为什么这样有效？
    - 如果 p 和 q 分别在当前节点的左右子树中，当前节点就是 LCA
    - 如果 p 和 q 都在左子树（或右子树），LCA 也在那一边

    时间复杂度：O(n) - 最坏情况遍历整棵树
    空间复杂度：O(h) - h 为树高度，递归栈空间
    """

    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        """
        返回 p 和 q 的最近公共祖先
        """
        # 递归终止条件
        # 1. 当前节点为空
        # 2. 当前节点是 p 或 q（找到了其中一个）
        if not root or root == p or root == q:
            return root

        # 递归在左子树中查找
        left = self.lowestCommonAncestor(root.left, p, q)
        # 递归在右子树中查找
        right = self.lowestCommonAncestor(root.right, p, q)

        # 如果左右子树都找到了，说明当前节点是 LCA
        if left and right:
            return root

        # 如果只有左子树找到了，返回左子树的结果
        if left:
            return left

        # 如果只有右子树找到了，返回右子树的结果
        if right:
            return right

        # 都没找到（这种情况在题目保证下不会发生）
        return None

    def lowestCommonAncestorIterative(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        """
        迭代法 - 使用父指针

        思路：
        1. 遍历树，记录每个节点的父节点
        2. 从 p 开始，记录 p 到根节点的路径
        3. 从 q 开始，向上遍历，第一个在 p 的路径中的节点就是 LCA
        """
        from collections import deque

        # 记录每个节点的父节点
        parent = {root: None}
        queue = deque([root])

        # BFS 遍历，直到找到 p 和 q
        while p not in parent or q not in parent:
            node = queue.popleft()
            if node.left:
                parent[node.left] = node
                queue.append(node.left)
            if node.right:
                parent[node.right] = node
                queue.append(node.right)

        # 记录 p 到根节点的路径
        ancestors = set()
        while p:
            ancestors.add(p)
            p = parent[p]

        # 从 q 向上遍历，找到第一个公共祖先
        while q not in ancestors:
            q = parent[q]

        return q


# @lc code=end



#
# @lcpr case=start
# [3,5,1,6,2,0,8,null,null,7,4]\n5\n1\n
# @lcpr case=end

# @lcpr case=start
# [3,5,1,6,2,0,8,null,null,7,4]\n5\n4\n
# @lcpr case=end

# @lcpr case=start
# [1,2]\n1\n2\n
# @lcpr case=end

#

if __name__ == "__main__":
    sol = Solution()

    # 辅助函数：根据层序遍历列表构建二叉树，并返回节点值到节点的映射
    def build_tree(values):
        """根据层序遍历列表构建二叉树，返回 (root, node_map)"""
        if not values or values[0] is None:
            return None, {}

        from collections import deque
        root = TreeNode(values[0])
        node_map = {values[0]: root}
        queue = deque([root])
        i = 1

        while queue and i < len(values):
            node = queue.popleft()

            # 左子节点
            if i < len(values) and values[i] is not None:
                node.left = TreeNode(values[i])
                node_map[values[i]] = node.left
                queue.append(node.left)
            i += 1

            # 右子节点
            if i < len(values) and values[i] is not None:
                node.right = TreeNode(values[i])
                node_map[values[i]] = node.right
                queue.append(node.right)
            i += 1

        return root, node_map

    # 测试用例 1：基本示例，p 和 q 在不同子树
    #       3
    #      / \
    #     5   1
    #    / \  / \
    #   6  2 0  8
    #     / \
    #    7   4
    # p=5, q=1, LCA=3
    root1, map1 = build_tree([3, 5, 1, 6, 2, 0, 8, None, None, 7, 4])
    p1, q1 = map1[5], map1[1]
    result1 = sol.lowestCommonAncestor(root1, p1, q1)
    print(f"Test 1: LCA of 5 and 1 = {result1.val}")
    assert result1.val == 3, f"Expected 3, got {result1.val}"

    # 测试用例 2：p 是 q 的祖先
    # p=5, q=4, LCA=5
    root2, map2 = build_tree([3, 5, 1, 6, 2, 0, 8, None, None, 7, 4])
    p2, q2 = map2[5], map2[4]
    result2 = sol.lowestCommonAncestor(root2, p2, q2)
    print(f"Test 2: LCA of 5 and 4 = {result2.val}")
    assert result2.val == 5, f"Expected 5, got {result2.val}"

    # 测试用例 3：简单树
    #   1
    #  /
    # 2
    # p=1, q=2, LCA=1
    root3, map3 = build_tree([1, 2])
    p3, q3 = map3[1], map3[2]
    result3 = sol.lowestCommonAncestor(root3, p3, q3)
    print(f"Test 3: LCA of 1 and 2 = {result3.val}")
    assert result3.val == 1, f"Expected 1, got {result3.val}"

    # 测试用例 4：迭代法测试
    root4, map4 = build_tree([3, 5, 1, 6, 2, 0, 8, None, None, 7, 4])
    p4, q4 = map4[5], map4[1]
    result4 = sol.lowestCommonAncestorIterative(root4, p4, q4)
    print(f"Test 4 (Iterative): LCA of 5 and 1 = {result4.val}")
    assert result4.val == 3, f"Expected 3, got {result4.val}"

    print("\nAll tests passed!")
