#
# @lc app=leetcode.cn id=101 lang=python3
# @lcpr version=30204
#
# [101] 对称二叉树
#


# @lcpr-template-start

# @lcpr-template-end
# @lc code=start
# Definition for a binary tree node.
from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    # 100. 相同的树（改成镜像判断）
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        if p is None or q is None:
            return p is q
        return p.val == q.val and self.isSameTree(p.left, q.right) and self.isSameTree(p.right, q.left)

    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        return self.isSameTree(root.left, root.right)

# @lc code=end



# ========== 示例推演：root = [1,2,2,3,4,4,3] ==========
#
#       1
#      / \
#     2   2
#    / \ / \
#   3  4 4  3
#
# 检查 (2, 2)：值相等
#   检查 (3, 3)：值相等，都为空子树，返回 True
#   检查 (4, 4)：值相等，都为空子树，返回 True
# 返回 True
#
# 示例：root = [1,2,2,null,3,null,3]
#
#       1
#      / \
#     2   2
#      \   \
#       3   3
#
# 检查 (2, 2)：值相等
#   检查 (null, 3)：一个空一个非空，返回 False
# 返回 False

#
# @lcpr case=start
# [1,2,2,3,4,4,3]\n
# @lcpr case=end

# @lcpr case=start
# [1,2,2,null,3,null,3]\n
# @lcpr case=end

#

