#
# @lc app=leetcode.cn id=543 lang=python3
# @lcpr version=30204
#
# [543] 二叉树的直径
#
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# @lcpr-template-start

# @lcpr-template-end
# @lc code=start
# 转为深度问题
from typing import Optional
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        ans = 0
        def findDiameter(root:TreeNode) -> int:
            if not root:
                return 0
            left_s = findDiameter(root.left)
            right_s = findDiameter(root.right)
            nonlocal ans 
            ans = max(ans,left_s+right_s)
            return max(left_s,right_s)+1
        findDiameter(root)
        return ans 
# @lc code=end



#
# @lcpr case=start
# [1,2,3,4,5]\n
# @lcpr case=end

# @lcpr case=start
# [1,2]\n
# @lcpr case=end

#

