#
# @lc app=leetcode.cn id=104 lang=python3
# @lcpr version=30204
#
# [104] 二叉树的最大深度
#


# @lcpr-template-start

# @lcpr-template-end
# @lc code=start
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

from typing import Optional


class Solution:
    """
    二叉树的最大深度 - 递归/DFS

    核心思想：
    二叉树的最大深度 = max(左子树的最大深度, 右子树的最大深度) + 1
    递归终止条件：空节点的深度为0

    时间复杂度：O(n)，每个节点访问一次
    空间复杂度：O(h)，h是树的高度，递归栈的深度
    """

    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        # 左右子树的最大深度加1（当前层）
        return max(self.maxDepth(root.left), self.maxDepth(root.right)) + 1


# 测试用例
if __name__ == "__main__":
    sol = Solution()

    # 构建测试树: [3,9,20,null,null,15,7]
    root1 = TreeNode(3)
    root1.left = TreeNode(9)
    root1.right = TreeNode(20)
    root1.right.left = TreeNode(15)
    root1.right.right = TreeNode(7)

    # 构建测试树: [1,null,2]
    root2 = TreeNode(1)
    root2.right = TreeNode(2)

    tests = [
        (root1, 3),
        (root2, 2),
        (None, 0),
        (TreeNode(1), 1),
    ]

    print("二叉树的最大深度 - 测试开始")
    for i, (root, expected) in enumerate(tests, 1):
        result = sol.maxDepth(root)
        passed = result == expected
        status = "✓ PASS" if passed else "✗ FAIL"
        print(f"测试 {i}: {status}")
    print("测试结束")
# @lc code=end



#
# @lcpr case=start
# [3,9,20,null,null,15,7]\n
# @lcpr case=end

# @lcpr case=start
# [1,null,2]\n
# @lcpr case=end

#

