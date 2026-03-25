#
# @lc app=leetcode.cn id=124 lang=python3
# @lcpr version=30204
#
# [124] 二叉树中的最大路径和
#


# @lcpr-template-start

# @lcpr-template-end
# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        res = root.val
        def findPath(root:TreeNode) -> int:
            if not root:
                return 0
            left_s = max(findPath(root.left),0)
            right_s = max(findPath(root.right),0)

            nonlocal res
            ans = left_s + right_s + root.val
            res = max(ans,res)
            return max(left_s,right_s)+root.val
        res =max(findPath(root),res)
        return res 
# @lc code=end



#
# @lcpr case=start
# [1,2,3]\n
# @lcpr case=end

# @lcpr case=start
# [-10,9,20,null,null,15,7]\n
# @lcpr case=end

#

