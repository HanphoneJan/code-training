#
# @lc app=leetcode.cn id=105 lang=python3
# @lcpr version=30204
#
# [105] 从前序与中序遍历序列构造二叉树
#

# @lcpr-template-start
from typing import List, Optional


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
    从前序与中序遍历序列构造二叉树 - 递归

    核心思想：
    前序遍历的第一个元素是根节点，在中序遍历中找到该根节点的位置，
    其左边是左子树，右边是右子树。然后递归构建左右子树。

    为什么前序+中序可以唯一确定一棵二叉树？
    - 前序：[根节点, [左子树前序], [右子树前序]]
    - 中序：[[左子树中序], 根节点, [右子树中序]]
    - 前序的第一个元素确定根，在中序中找到根的位置即可划分左右

    算法步骤：
    1. 从前序遍历取第一个元素作为根节点
    2. 在中序遍历中找到根节点的位置，确定左子树大小
    3. 递归构建左子树和右子树

    时间复杂度：O(n²)，每次查找根节点位置需要O(n)
    空间复杂度：O(n)，递归栈深度
    """

    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        """
        根据前序遍历和中序遍历序列构造二叉树

        Args:
            preorder: 前序遍历序列
            inorder: 中序遍历序列

        Returns:
            构造好的二叉树根节点
        """
        # 递归终止条件：空序列表示空节点
        if not preorder:
            return None

        # 前序遍历的第一个元素是当前子树的根节点
        root_val = preorder[0]

        # 在中序遍历中找到根节点的位置
        # 该位置左边的元素都属于左子树，右边的都属于右子树
        left_size = inorder.index(root_val)

        # 递归构建左子树
        # 左子树的前序：preorder[1:1+left_size]（跳过根，取left_size个）
        # 左子树的中序：inorder[:left_size]（根左边的部分）
        left = self.buildTree(preorder[1:1 + left_size], inorder[:left_size])

        # 递归构建右子树
        # 右子树的前序：preorder[1+left_size:]（跳过根和左子树）
        # 右子树的中序：inorder[left_size+1:]（跳过根，取右边部分）
        right = self.buildTree(preorder[1 + left_size:], inorder[left_size + 1:])

        # 构造当前节点并返回
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


# 可运行测试用例
if __name__ == "__main__":
    sol = Solution()

    # 辅助函数：计算二叉树的最大深度（用于验证树结构）
    def max_depth(root: Optional[TreeNode]) -> int:
        """计算二叉树的最大深度"""
        if not root:
            return 0
        return max(max_depth(root.left), max_depth(root.right)) + 1

    # 辅助函数：二叉树的层序遍历（用于验证树结构）
    from collections import deque

    def level_order(root: Optional[TreeNode]) -> List[List[int]]:
        """二叉树层序遍历"""
        if not root:
            return []
        result: List[List[int]] = []
        queue: deque[TreeNode] = deque([root])
        while queue:
            level_size = len(queue)
            level: List[int] = []
            for _ in range(level_size):
                node = queue.popleft()
                level.append(node.val)
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            result.append(level)
        return result

    # 辅助函数：获取树的前序遍历
    def get_preorder(root: Optional[TreeNode]) -> List[int]:
        """获取二叉树的前序遍历序列"""
        if not root:
            return []
        return [root.val] + get_preorder(root.left) + get_preorder(root.right)

    # 辅助函数：获取树的中序遍历
    def get_inorder(root: Optional[TreeNode]) -> List[int]:
        """获取二叉树的中序遍历序列"""
        if not root:
            return []
        return get_inorder(root.left) + [root.val] + get_inorder(root.right)

    # 测试用例列表：(前序遍历, 中序遍历)
    tests = [
        # 测试用例 1：标准二叉树
        # 前序: [3,9,20,15,7]
        # 中序: [9,3,15,20,7]
        # 构建的树：
        #       3
        #      / \
        #     9  20
        #       /  \
        #      15   7
        ([3, 9, 20, 15, 7], [9, 3, 15, 20, 7]),
        # 测试用例 2：单节点
        # 前序: [-1]
        # 中序: [-1]
        ([-1], [-1]),
        # 测试用例 3：只有左子树
        # 前序: [1,2,3]
        # 中序: [3,2,1]
        # 构建的树：
        #       1
        #      /
        #     2
        #    /
        #   3
        ([1, 2, 3], [3, 2, 1]),
        # 测试用例 4：只有右子树
        # 前序: [1,2,3]
        # 中序: [1,2,3]
        # 构建的树：
        #       1
        #        \
        #         2
        #          \
        #           3
        ([1, 2, 3], [1, 2, 3]),
        # 测试用例 5：完全二叉树
        # 前序: [1,2,4,5,3,6,7]
        # 中序: [4,2,5,1,6,3,7]
        ([1, 2, 4, 5, 3, 6, 7], [4, 2, 5, 1, 6, 3, 7]),
    ]

    print("=" * 50)
    print("从前序与中序遍历序列构造二叉树 - 测试开始")
    print("=" * 50)

    all_passed = True
    for i, (preorder, inorder) in enumerate(tests, 1):
        # 构建树
        root = sol.buildTree(preorder, inorder)

        # 验证：重新获取前序和中序，应该与输入一致
        result_preorder = get_preorder(root)
        result_inorder = get_inorder(root)

        passed = (result_preorder == preorder and result_inorder == inorder)
        all_passed = all_passed and passed
        status = "✓ PASS" if passed else "✗ FAIL"

        print(f"\n测试 {i}: {status}")
        print(f"  输入前序: {preorder}")
        print(f"  输入中序: {inorder}")
        print(f"  输出前序: {result_preorder}")
        print(f"  输出中序: {result_inorder}")
        print(f"  层序遍历: {level_order(root)}")

    print("\n" + "=" * 50)
    print(f"所有测试 {'通过' if all_passed else '未通过'}！")
    print("=" * 50)