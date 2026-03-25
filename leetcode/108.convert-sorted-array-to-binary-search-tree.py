#
# @lc app=leetcode.cn id=108 lang=python3
# @lcpr version=30204
#
# [108] 将有序数组转换为二叉搜索树
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

from typing import List, Optional


class Solution:
    """
    将有序数组转换为二叉搜索树 - 递归

    核心思想：
    二叉搜索树的中序遍历是有序数组。选择数组中间元素作为根节点，
    可以保证树的高度平衡。然后递归构建左右子树。

    算法步骤：
    1. 选择数组中间元素作为根节点
    2. 递归构建左子树（左半部分）
    3. 递归构建右子树（右半部分）

    时间复杂度：O(n)，每个元素访问一次
    空间复杂度：O(log n)，递归栈深度
    """

    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        def dfs(left: int, right: int) -> Optional[TreeNode]:
            if left > right:
                return None

            # 选择中间元素作为根节点，确保树平衡
            mid = left + (right - left) // 2
            root = TreeNode(nums[mid])

            # 递归构建左右子树
            root.left = dfs(left, mid - 1)
            root.right = dfs(mid + 1, right)

            return root

        return dfs(0, len(nums) - 1)
# @lc code=end



#
# @lcpr case=start
# [-10,-3,0,5,9]\n
# @lcpr case=end

# @lcpr case=start
# [1,3]\n
# @lcpr case=end

#

