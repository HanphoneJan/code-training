#
# @lc app=leetcode.cn id=226 lang=python3
# @lcpr version=30204
#
# [226] 翻转二叉树
#
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# @lcpr-template-start

# @lcpr-template-end
# @lc code=start
# Definition for a binary tree node.

from typing import Optional
class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root:
            return None
        left = self.invertTree(root.right)
        right = self.invertTree(root.left)
        root.left = left
        root.right = right
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

