#
# @lc app=leetcode.cn id=230 lang=python3
# @lcpr version=30204
#
# [230] 二叉搜索树中第 K 小的元素
#


# @lcpr-template-start
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
# @lcpr-template-end
# @lc code=start
# Definition for a binary tree node.
# 二叉搜索树转升序数组
from operator import le
from typing import Optional
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        # 直接中序遍历转为数组当然简单，但是这样就违背用二叉搜索树的初衷了

        # 可以使用外部变量来计数，也可以不适用
        def dfs(root:Optional[TreeNode])->int:
            if not root:
                return -1
            left_dfs = dfs(root.left)
            if left_dfs != -1:
                return left_dfs
            nonlocal k
            k -= 1
            if 0 == k:
                return root.val
            return dfs(root.right)
        return dfs(root)


# 思考：改成求第 k 大要怎么做？--> 右中左的顺序遍历
# @lc code=end



#
# @lcpr case=start
# [3,1,4,null,2]\n1\n
# @lcpr case=end

# @lcpr case=start
# [5,3,6,2,4,null,null,1]\n3\n
# @lcpr case=end

#

