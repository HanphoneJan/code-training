#
# @lc app=leetcode.cn id=124 lang=python3
# @lcpr version=30204
#
# [124] 二叉树中的最大路径和
#


# @lcpr-template-start
from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


# @lcpr-template-end
# @lc code=start
class Solution:
    """
    124. 二叉树中的最大路径和 - 深度优先搜索（后序遍历）

    核心思想：
    路径和 = 路径上所有节点值的总和。
    对于每个节点，以它为 "最高点" 的路径可能有三种情况：
    1. 只包含该节点本身
    2. 该节点 + 左子树中的某条路径
    3. 该节点 + 右子树中的某条路径
    4. 左子树 + 该节点 + 右子树（穿过该节点的完整路径）

    但是！对于父节点来说，只能接上一条 "分支"（不能是完整的穿过路径）。
    所以递归函数返回的是：以当前节点为端点的最大路径和（只能选左或右或都不选）。

    关键技巧：
    - 用 max(子树贡献, 0) 来处理负贡献（负数子树不如不选）
    - 用全局变量（nonlocal）记录 "经过当前节点的完整路径和" 的最大值

    时间复杂度：O(n)，每个节点访问一次
    空间复杂度：O(h)，递归栈深度，h 为树高
    """

    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0

        res = root.val  # 全局最大路径和，初始化为根节点值

        def findPath(root: TreeNode) -> int:
            """
            返回以 root 为端点的最大路径和（只能是一条链，不能分叉）。
            同时更新全局最大路径和 res（可以分叉的完整路径）。
            """
            nonlocal res
            if not root:
                return 0

            # 递归计算左右子树的贡献值
            # 如果子树贡献为负数，不如不选（取 0）
            left_s = max(findPath(root.left), 0)
            right_s = max(findPath(root.right), 0)

            # 以当前节点为 "最高点" 的完整路径和
            # 这条路径可以包含左右两个子树
            ans = left_s + right_s + root.val
            res = max(ans, res)  # 更新全局最大值

            # 返回以当前节点为端点的最大路径和
            # 只能选左或右中的一条（因为要向上连接父节点）
            return max(left_s, right_s) + root.val

        findPath(root)
        return res


# @lc code=end


#
# @lcpr case=start
# [1,2,3]\n
# @lcpr case=end

# @lcpr case=start
# [-10,9,20,null,null,15,7]\n
# @lcpr case=end


if __name__ == "__main__":
    # 辅助函数：根据层序遍历列表构建二叉树（null 表示空节点）
    def build_tree(values):
        if not values or values[0] is None:
            return None
        root = TreeNode(values[0])
        queue = [root]
        i = 1
        while queue and i < len(values):
            node = queue.pop(0)
            if i < len(values) and values[i] is not None:
                node.left = TreeNode(values[i])
                queue.append(node.left)
            i += 1
            if i < len(values) and values[i] is not None:
                node.right = TreeNode(values[i])
                queue.append(node.right)
            i += 1
        return root

    sol = Solution()

    tests = [
        ([1, 2, 3], 6),                          # 1->2 和 1->3，最大路径 2+1+3=6
        ([-10, 9, 20, None, None, 15, 7], 42),  # 15->20->7 = 42
        ([-3], -3),                              # 只有一个负数节点
        ([2, -1], 2),                            # 2 比 2+(-1)=1 大
    ]

    print("二叉树中的最大路径和 - 测试开始")
    for i, (vals, expected) in enumerate(tests, 1):
        root = build_tree(vals)
        result = sol.maxPathSum(root)
        passed = result == expected
        status = "PASS" if passed else "FAIL"
        print(f"测试 {i}: vals={vals} -> {status}")
        if not passed:
            print(f"  输出: {result}")
            print(f"  期望: {expected}")
    print("测试结束")
