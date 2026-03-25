#
# @lc app=leetcode.cn id=114 lang=python3
# @lcpr version=30204
#
# [114] 二叉树展开为链表
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


class Solution:
    """
    二叉树展开为链表 - O(1)空间复杂度

    核心思想：
    将二叉树展开为链表，展开后的链表应该与二叉树的前序遍历顺序相同。
    要求使用 O(1) 额外空间（不考虑递归栈）。

    算法步骤（Morris遍历的变种）：
    1. 对于当前节点curr，如果它有左子树：
       a. 找到左子树的最右节点（前驱节点）
       b. 将curr的右子树接到前驱节点的右边
       c. 将curr的左子树变为右子树，左子树置空
    2. curr移动到右子节点

    时间复杂度：O(n)，每个节点访问常数次
    空间复杂度：O(1)，只使用常数额外空间
    """

    def flatten(self, root: TreeNode) -> None:
        curr = root
        while curr:
            if curr.left:
                # 找到左子树的最右节点（前驱节点）
                predecessor = curr.left
                while predecessor.right:
                    predecessor = predecessor.right

                # 将curr的右子树接到前驱节点的右边
                predecessor.right = curr.right

                # 将左子树移到右边，左子树置空
                curr.right = curr.left
                curr.left = None

            # 移动到下一个节点
            curr = curr.right


        
# @lc code=end



#
# @lcpr case=start
# [1,2,5,3,4,null,6]\n
# @lcpr case=end

# @lcpr case=start
# []\n
# @lcpr case=end

# @lcpr case=start
# [0]\n
# @lcpr case=end

#

