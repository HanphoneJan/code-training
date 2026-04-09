#
# @lc app=leetcode.cn id=543 lang=python3
# @lcpr version=30204
#
# [543] 二叉树的直径
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
    二叉树的直径 - 深度优先搜索

    问题描述：
    给定一棵二叉树，你需要计算它的直径长度。
    一棵二叉树的直径长度是任意两个结点路径长度中的最大值。
    这条路径可能穿过也可能不穿过根结点。

    核心思路：
    二叉树的直径 = 左子树的最大深度 + 右子树的最大深度

    对于每个节点，计算经过它的最长路径（左深度 + 右深度），
    然后在所有节点中取最大值。

    具体做法：
    1. 定义 dfs(node) 返回以 node 为根的最大深度
    2. 在 dfs 中，递归计算左右子树的深度
    3. 经过当前节点的直径 = left_depth + right_depth
    4. 更新全局最大值
    5. 返回当前节点的深度 = max(left_depth, right_depth) + 1

    时间复杂度: O(n) - 每个节点只访问一次
    空间复杂度: O(h) - h 是树的高度，递归栈空间
    """
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self.ans = 0  # 记录最大直径

        def dfs(node: Optional[TreeNode]) -> int:
            """
            返回以 node 为根的最大深度
            同时更新经过 node 的最大直径
            """
            if not node:
                return 0

            # 递归计算左右子树的深度
            left_depth = dfs(node.left)
            right_depth = dfs(node.right)

            # 经过当前节点的直径 = 左深度 + 右深度
            self.ans = max(self.ans, left_depth + right_depth)

            # 返回当前节点的深度
            return max(left_depth, right_depth) + 1

        dfs(root)
        return self.ans


# 其他解法：显式返回两个值
# class Solution:
#     def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
#         """
#         返回 (最大深度, 最大直径)
#         """
#         def dfs(node):
#             if not node:
#                 return 0, 0
#
#             left_depth, left_dia = dfs(node.left)
#             right_depth, right_dia = dfs(node.right)
#
#             depth = max(left_depth, right_depth) + 1
#             # 经过当前节点的直径，或在子树中
#             diameter = max(left_depth + right_depth, left_dia, right_dia)
#
#             return depth, diameter
#
#         return dfs(root)[1]

# @lc code=end



#
# @lcpr case=start
# [1,2,3,4,5]\n
# @lcpr case=end

# @lcpr case=start
# [1,2]\n
# @lcpr case=end

#


def build_tree(values):
    """
    根据层序遍历列表构建二叉树
    None 表示空节点
    """
    if not values:
        return None

    root = TreeNode(values[0])
    queue = [root]
    i = 1

    while queue and i < len(values):
        node = queue.pop(0)

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


if __name__ == "__main__":
    sol = Solution()

    # 测试用例 1：基本示例
    #       1
    #      / \
    #     2   3
    #    / \
    #   4   5
    # 直径：4-2-1-3 或 5-2-1-3，长度为 3
    nums1 = [1, 2, 3, 4, 5]
    root1 = build_tree(nums1)
    result1 = sol.diameterOfBinaryTree(root1)
    print(f"Test 1: root={nums1}")
    print(f"Result: {result1}")
    assert result1 == 3, f"Expected 3, got {result1}"
    print("Passed!\n")

    # 测试用例 2：两个节点
    nums2 = [1, 2]
    root2 = build_tree(nums2)
    result2 = sol.diameterOfBinaryTree(root2)
    print(f"Test 2: root={nums2}")
    print(f"Result: {result2}")
    assert result2 == 1, f"Expected 1, got {result2}"
    print("Passed!\n")

    # 测试用例 3：空树
    result3 = sol.diameterOfBinaryTree(None)
    print(f"Test 3: root=None")
    print(f"Result: {result3}")
    assert result3 == 0, f"Expected 0, got {result3}"
    print("Passed!\n")

    # 测试用例 4：单节点
    nums4 = [1]
    root4 = build_tree(nums4)
    result4 = sol.diameterOfBinaryTree(root4)
    print(f"Test 4: root={nums4}")
    print(f"Result: {result4}")
    assert result4 == 0, f"Expected 0, got {result4}"
    print("Passed!\n")

    # 测试用例 5：链状树
    # 1-2-3-4-5，直径为 4
    nums5 = [1, 2, None, 3, None, 4, None, 5]
    root5 = build_tree(nums5)
    result5 = sol.diameterOfBinaryTree(root5)
    print(f"Test 5: 链状树")
    print(f"Result: {result5}")
    assert result5 == 4, f"Expected 4, got {result5}"
    print("Passed!\n")

    print("All tests passed!")
