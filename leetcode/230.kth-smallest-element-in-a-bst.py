#
# @lc app=leetcode.cn id=230 lang=python3
# @lcpr version=30204
#
# [230] 二叉搜索树中第 K 小的元素
#


# @lcpr-template-start
from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
# @lcpr-template-end
# @lc code=start
class Solution:
    """
    二叉搜索树中第 K 小的元素 - 中序遍历

    问题描述：
    给定一个二叉搜索树的根节点 root ，和一个整数 k ，
    请你设计一个算法查找其中第 k 小的元素（从 1 开始计数）。

    核心思路：
    二叉搜索树（BST）的性质：中序遍历结果是升序序列。
    因此，第 k 小的元素 = 中序遍历的第 k 个元素。

    优化：不需要遍历完整棵树，找到第 k 个就可以停止。

    时间复杂度：O(h + k) - h 为树高度，遍历到第 k 个元素
    空间复杂度：O(h) - 递归栈空间

    进阶思考：
    如果频繁查询第 k 小元素，可以给每个节点增加子树大小字段，
    实现 O(h) 时间复杂度的查询。
    """

    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        """
        返回二叉搜索树中第 k 小的元素
        """
        # 直接中序遍历转为数组当然简单，但是这样就违背用二叉搜索树的初衷了

        # 使用外部变量来计数，也可以不使用
        # 递归中序遍历，找到第 k 小就返回
        self.result = 0
        self.count = 0

        def dfs(node: Optional[TreeNode]) -> bool:
            """
            中序遍历 DFS
            返回 True 表示已经找到第 k 小元素
            """
            if not node:
                return False

            # 遍历左子树
            if dfs(node.left):
                return True

            # 访问当前节点
            self.count += 1
            if self.count == k:
                self.result = node.val
                return True

            # 遍历右子树
            return dfs(node.right)

        dfs(root)
        return self.result

    def kthSmallestIterative(self, root: Optional[TreeNode], k: int) -> int:
        """
        迭代版中序遍历

        使用栈模拟递归，找到第 k 小就停止。
        """
        stack = []
        cur = root
        count = 0

        while cur or stack:
            # 走到最左边
            while cur:
                stack.append(cur)
                cur = cur.left

            # 弹出栈顶元素（当前子树的最小值）
            cur = stack.pop()
            count += 1

            if count == k:
                return cur.val

            # 转向右子树
            cur = cur.right

        return -1  # 不应该执行到这里


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

if __name__ == "__main__":
    sol = Solution()

    # 辅助函数：根据层序遍历列表构建二叉搜索树
    def build_tree(values):
        """根据层序遍历列表构建二叉树，None 表示空节点"""
        if not values or values[0] is None:
            return None

        from collections import deque
        root = TreeNode(values[0])
        queue = deque([root])
        i = 1

        while queue and i < len(values):
            node = queue.popleft()

            # 左子节点
            if i < len(values) and values[i] is not None:
                node.left = TreeNode(values[i])
                queue.append(node.left)
            i += 1

            # 右子节点
            if i < len(values) and values[i] is not None:
                node.right = TreeNode(values[i])
                queue.append(node.right)
            i += 1

        return root

    # 测试用例 1：基本示例
    #       3
    #      / \
    #     1   4
    #      \
    #       2
    # 中序：1, 2, 3, 4
    root1 = build_tree([3, 1, 4, None, 2])
    k1 = 1
    result1 = sol.kthSmallest(root1, k1)
    print(f"Test 1: kthSmallest([3,1,4,null,2], 1) = {result1}")
    assert result1 == 1, f"Expected 1, got {result1}"

    # 测试用例 2：另一个示例
    #         5
    #        / \
    #       3   6
    #      / \
    #     2   4
    #    /
    #   1
    # 中序：1, 2, 3, 4, 5, 6
    root2 = build_tree([5, 3, 6, 2, 4, None, None, 1])
    k2 = 3
    result2 = sol.kthSmallest(root2, k2)
    print(f"Test 2: kthSmallest([5,3,6,2,4,null,null,1], 3) = {result2}")
    assert result2 == 3, f"Expected 3, got {result2}"

    # 测试用例 3：k = n（最大值）
    result3 = sol.kthSmallest(root1, 4)
    print(f"Test 3: kthSmallest([3,1,4,null,2], 4) = {result3}")
    assert result3 == 4, f"Expected 4, got {result3}"

    # 测试用例 4：单节点
    root4 = build_tree([1])
    result4 = sol.kthSmallest(root4, 1)
    print(f"Test 4: kthSmallest([1], 1) = {result4}")
    assert result4 == 1, f"Expected 1, got {result4}"

    # 测试用例 5：迭代法测试
    root5 = build_tree([3, 1, 4, None, 2])
    result5 = sol.kthSmallestIterative(root5, 2)
    print(f"Test 5 (Iterative): kthSmallestIterative([3,1,4,null,2], 2) = {result5}")
    assert result5 == 2, f"Expected 2, got {result5}"

    print("\nAll tests passed!")
