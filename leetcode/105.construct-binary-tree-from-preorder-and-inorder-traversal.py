#
# @lc app=leetcode.cn id=105 lang=python3
# @lcpr version=30204
#
# [105] 从前序与中序遍历序列构造二叉树
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
    从前序与中序遍历序列构造二叉树 - 递归

    核心思想：
    前序遍历的第一个元素是根节点，在中序遍历中找到该根节点的位置，
    其左边是左子树，右边是右子树。然后递归构建左右子树。

    算法步骤：
    1. 从前序遍历取第一个元素作为根节点
    2. 在中序遍历中找到根节点的位置，确定左子树大小
    3. 递归构建左子树和右子树

    时间复杂度：O(n²)，每次查找根节点位置需要O(n)
    空间复杂度：O(n)，递归栈深度
    """

    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        if not preorder:  # 空节点
            return None

        # 前序遍历的第一个元素是根节点
        root_val = preorder[0]
        # 在中序遍历中找到根节点的位置，确定左子树大小
        left_size = inorder.index(root_val)

        # 递归构建左子树
        left = self.buildTree(preorder[1:1 + left_size], inorder[:left_size])
        # 递归构建右子树
        right = self.buildTree(preorder[1 + left_size:], inorder[left_size + 1:])

        return TreeNode(root_val, left, right)

# @lc code=end



#
# @lcpr case=start
# [3,9,20,15,7]\n[9,3,15,20,7]\n
# @lcpr case=end

# @lcpr case=start
# [-1]\n[-1]\n
# @lcpr case=end

#

