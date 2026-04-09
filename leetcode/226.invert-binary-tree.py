#
# @lc app=leetcode.cn id=226 lang=python3
# @lcpr version=30204
#
# [226] 翻转二叉树
#

# @lcpr-template-start
from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
# @lcpr-template-end
# @lc code=start
class Solution:
    """
    翻转二叉树 - 递归法

    问题描述：
    给你一棵二叉树的根节点 root，翻转这棵二叉树，并返回其根节点。
    翻转意味着交换每个节点的左右子树。

    核心思路：
    递归地翻转左右子树，然后交换它们。

    递归定义：
    invertTree(root) = 交换(invertTree(root.left), invertTree(root.right))

    递归终止条件：
    - 如果 root 为 None，返回 None
    - 如果 root 是叶子节点，返回 root（无需翻转）

    为什么这样有效？
    二叉树的翻转具有递归结构：整棵树的翻转 = 左子树翻转 + 右子树翻转 + 交换左右子树

    时间复杂度：O(n) - 每个节点访问一次
    空间复杂度：O(h) - h 为树高度，递归栈空间
    """

    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        """
        翻转二叉树
        """
        # 递归终止条件：空节点
        if not root:
            return None

        # 递归翻转左右子树
        # 注意：先递归翻转，再交换；或者先交换再递归都可以
        left = self.invertTree(root.left)
        right = self.invertTree(root.right)

        # 交换左右子树
        root.left = right
        root.right = left

        return root

    def invertTreeIterative(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        """
        翻转二叉树 - 迭代法（BFS）

        使用队列进行层序遍历，对每个节点交换其左右子节点。

        时间复杂度：O(n)
        空间复杂度：O(w) - w 为树的最大宽度
        """
        from collections import deque

        if not root:
            return None

        queue = deque([root])

        while queue:
            node = queue.popleft()

            # 交换当前节点的左右子节点
            node.left, node.right = node.right, node.left

            # 将子节点加入队列（注意：交换后，原来的右子树现在在左边）
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)

        return root


# @lc code=end



#
# @lcpr case=start
# [4,2,7,1,3,6,9]\n
# @lcpr case=end

# @lcpr case=start
# [2,1,3]\n
# @lcpr case=end

# @lcpr case=start
# []\n
# @lcpr case=end

#

if __name__ == "__main__":
    sol = Solution()

    # 辅助函数：根据层序遍历列表构建二叉树
    def build_tree(values):
        """根据层序遍历列表构建二叉树，None 表示空节点"""
        if not values or values[0] is None:
            return None

        from collections import deque
        root = TreeNode(values[0])
        queue = deque([root])
        i = 1

        while queue and i < len(values):
            node = queue.popleft()

            # 左子节点
            if i < len(values) and values[i] is not None:
                node.left = TreeNode(values[i])
                queue.append(node.left)
            i += 1

            # 右子节点
            if i < len(values) and values[i] is not None:
                node.right = TreeNode(values[i])
                queue.append(node.right)
            i += 1

        return root

    # 辅助函数：将二叉树转换为层序遍历列表
    def tree_to_list(root):
        """将二叉树转换为层序遍历列表"""
        if not root:
            return []

        from collections import deque
        result = []
        queue = deque([root])

        while queue:
            node = queue.popleft()
            if node:
                result.append(node.val)
                queue.append(node.left)
                queue.append(node.right)
            else:
                result.append(None)

        # 去掉末尾的 None
        while result and result[-1] is None:
            result.pop()

        return result

    # 测试用例 1：基本示例
    #       4              4
    #      / \            / \
    #     2   7    ->    7   2
    #    / \  / \        / \  / \
    #   1  3 6  9      9  6 3  1
    root1 = build_tree([4, 2, 7, 1, 3, 6, 9])
    inverted1 = sol.invertTree(root1)
    result1 = tree_to_list(inverted1)
    print(f"Test 1: invertTree([4,2,7,1,3,6,9]) = {result1}")
    assert result1 == [4, 7, 2, 9, 6, 3, 1], f"Expected [4,7,2,9,6,3,1], got {result1}"

    # 测试用例 2：简单树
    #     2        2
    #    / \  ->  / \
    #   1   3    3   1
    root2 = build_tree([2, 1, 3])
    inverted2 = sol.invertTree(root2)
    result2 = tree_to_list(inverted2)
    print(f"Test 2: invertTree([2,1,3]) = {result2}")
    assert result2 == [2, 3, 1], f"Expected [2,3,1], got {result2}"

    # 测试用例 3：空树
    root3 = build_tree([])
    inverted3 = sol.invertTree(root3)
    result3 = tree_to_list(inverted3)
    print(f"Test 3: invertTree([]) = {result3}")
    assert result3 == [], f"Expected [], got {result3}"

    # 测试用例 4：单节点
    root4 = build_tree([1])
    inverted4 = sol.invertTree(root4)
    result4 = tree_to_list(inverted4)
    print(f"Test 4: invertTree([1]) = {result4}")
    assert result4 == [1], f"Expected [1], got {result4}"

    # 测试用例 5：只有左子树
    #     1           1
    #    /      ->    \
    #   2             2
    #  /               \
    # 3                 3
    root5 = build_tree([1, 2, None, 3])
    inverted5 = sol.invertTree(root5)
    result5 = tree_to_list(inverted5)
    print(f"Test 5: invertTree([1,2,null,3]) = {result5}")
    assert result5 == [1, None, 2, None, 3], f"Expected [1,None,2,None,3], got {result5}"

    # 测试用例 6：迭代法测试
    root6 = build_tree([4, 2, 7, 1, 3, 6, 9])
    inverted6 = sol.invertTreeIterative(root6)
    result6 = tree_to_list(inverted6)
    print(f"Test 6 (Iterative): invertTreeIterative([4,2,7,1,3,6,9]) = {result6}")
    assert result6 == [4, 7, 2, 9, 6, 3, 1], f"Expected [4,7,2,9,6,3,1], got {result6}"

    print("\nAll tests passed!")
