#
# @lc app=leetcode.cn id=104 lang=python3
# @lcpr version=30204
#
# [104] 二叉树的最大深度
#

# @lcpr-template-start
from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    """二叉树节点类

    属性:
        val: 节点值
        left: 左子节点
        right: 右子节点
    """

    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


# @lcpr-template-end
# @lc code=start
class Solution:
    """
    二叉树的最大深度 - 递归/DFS

    核心思想：
    二叉树的最大深度 = max(左子树的最大深度, 右子树的最大深度) + 1
    递归终止条件：空节点的深度为0

    为什么这样计算？
    - 深度是从根节点到最远叶子节点的路径上的节点数
    - 当前节点的深度 = 左右子树中更深的那个 + 当前层（1）

    递归三要素：
    1. 递归定义：maxDepth(node) 返回以 node 为根的子树的最大深度
    2. 递归终止：node 为 None 时返回 0（空树深度为0）
    3. 递归关系：maxDepth(node) = max(maxDepth(left), maxDepth(right)) + 1

    时间复杂度：O(n)，每个节点访问一次
    空间复杂度：O(h)，h是树的高度，递归栈的深度
                  最坏情况下（斜树）h = n
                  最好情况下（平衡树）h = log(n)
    """

    def maxDepth(self, root: Optional[TreeNode]) -> int:
        """
        计算二叉树的最大深度

        Args:
            root: 二叉树的根节点

        Returns:
            二叉树的最大深度（整数）
        """
        # 递归终止条件：空节点的深度为0
        if not root:
            return 0

        # 递归计算左子树的最大深度
        left_depth = self.maxDepth(root.left)
        # 递归计算右子树的最大深度
        right_depth = self.maxDepth(root.right)

        # 当前节点的深度 = 左右子树中较大的深度 + 1（当前层）
        return max(left_depth, right_depth) + 1


# @lc code=end


#
# @lcpr case=start
# [3,9,20,null,null,15,7]\n
# @lcpr case=end

# @lcpr case=start
# [1,null,2]\n
# @lcpr case=end

#


# 可运行测试用例
if __name__ == "__main__":
    sol = Solution()

    # 辅助函数：根据层序遍历列表构建二叉树
    from collections import deque
    from typing import List

    def build_tree(values: List[Optional[int]]) -> Optional[TreeNode]:
        """根据层序遍历列表构建二叉树

        Args:
            values: 层序遍历列表，None 表示空节点

        Returns:
            构建好的二叉树根节点
        """
        if not values or values[0] is None:
            return None

        root = TreeNode(values[0])
        queue: deque[TreeNode] = deque([root])
        i = 1

        while queue and i < len(values):
            node = queue.popleft()

            # 处理左子节点
            if i < len(values) and values[i] is not None:
                left_val: int = values[i]  # type: ignore
                node.left = TreeNode(left_val)
                queue.append(node.left)
            i += 1

            # 处理右子节点
            if i < len(values) and values[i] is not None:
                right_val: int = values[i]  # type: ignore
                node.right = TreeNode(right_val)
                queue.append(node.right)
            i += 1

        return root

    # 测试用例列表：(输入树, 预期深度)
    tests = [
        # 测试用例 1：平衡二叉树 [3,9,20,null,null,15,7]
        #       3
        #      / \
        #     9  20
        #       /  \
        #      15   7
        # 深度：3（路径 3->20->15 或 3->20->7）
        ([3, 9, 20, None, None, 15, 7], 3),
        # 测试用例 2：只有右子树 [1,null,2]
        #       1
        #        \
        #         2
        # 深度：2（路径 1->2）
        ([1, None, 2], 2),
        # 测试用例 3：空树 []
        # 深度：0
        ([], 0),
        # 测试用例 4：单节点树 [1]
        #       1
        # 深度：1
        ([1], 1),
        # 测试用例 5：斜树（只有左子树）[1,2,null,3,null,4]
        #       1
        #      /
        #     2
        #    /
        #   3
        #  /
        # 4
        # 深度：4
        ([1, 2, None, 3, None, 4], 4),
        # 测试用例 6：完全二叉树 [1,2,3,4,5,6,7]
        #        1
        #       / \
        #      2   3
        #     / \  / \
        #    4  5 6  7
        # 深度：3
        ([1, 2, 3, 4, 5, 6, 7], 3),
    ]

    print("=" * 50)
    print("二叉树的最大深度 - 测试开始")
    print("=" * 50)

    all_passed = True
    for i, (values, expected) in enumerate(tests, 1):
        root = build_tree(values)
        result = sol.maxDepth(root)
        passed = result == expected
        all_passed = all_passed and passed
        status = "✓ PASS" if passed else "✗ FAIL"
        print(f"\n测试 {i}: {status}")
        print(f"  输入: {values}")
        print(f"  输出: {result}")
        print(f"  预期: {expected}")

    print("\n" + "=" * 50)
    print(f"所有测试 {'通过' if all_passed else '未通过'}！")
    print("=" * 50)