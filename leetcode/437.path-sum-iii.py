#
# @lc app=leetcode.cn id=437 lang=python3
# @lcpr version=30204
#
# [437] 路径总和 III


# @lcpr-template-start
from typing import Optional
from collections import defaultdict

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
    路径总和 III - 前缀和 + 哈希表

    问题描述：
    给定一个二叉树的根节点 root，和一个整数 targetSum，
    求该二叉树里节点值之和等于 targetSum 的路径的数目。

    路径不需要从根节点开始，也不需要在叶子节点结束，
    但是路径方向必须是向下的（只能从父节点到子节点）。

    核心思路：
    利用前缀和的思想。定义从根节点到当前节点的路径和为 curr_sum，
    如果存在某个祖先节点，使得从该祖先节点到当前节点的路径和等于 targetSum，
    那么 curr_sum - targetSum 就是该祖先节点的前缀和。

    具体做法：
    1. 用哈希表 cnt 记录各个前缀和出现的次数
    2. 初始化 cnt[0] = 1，表示前缀和为 0 的路径有 1 条（空路径）
    3. 遍历树时，计算当前前缀和 curr_sum
    4. 以当前节点为终点的有效路径数 = cnt[curr_sum - targetSum]
    5. 将当前前缀和加入哈希表，递归处理左右子树
    6. 回溯时将当前前缀和的计数减 1

    时间复杂度: O(n) - 每个节点只访问一次
    空间复杂度: O(n) - 哈希表和递归栈
    """
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:
        # cnt[s] 表示前缀和为 s 的路径数量
        cnt = defaultdict(int)
        cnt[0] = 1  # 前缀和为 0 的路径有 1 条（空路径）
        ans = 0

        def dfs(node: Optional[TreeNode], curr_sum: int) -> None:
            """
            深度优先搜索，计算以当前节点为终点的有效路径数
            """
            nonlocal ans
            if not node:
                return

            # 更新当前路径和
            curr_sum += node.val

            # 以当前节点为终点的有效路径数
            # 即存在多少条从祖先到当前节点的路径和为 targetSum
            ans += cnt[curr_sum - targetSum]

            # 将当前前缀和加入哈希表
            cnt[curr_sum] += 1

            # 递归处理左右子树
            dfs(node.left, curr_sum)
            dfs(node.right, curr_sum)

            # 回溯：恢复哈希表状态
            cnt[curr_sum] -= 1

        dfs(root, 0)
        return ans


# 其他解法：双重 DFS（时间复杂度 O(n^2)）
# class Solution:
#     def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:
#         """
#         以每个节点为起点，向下搜索所有路径
#         时间复杂度: O(n^2) - 最坏情况下退化为链表
#         """
#         if not root:
#             return 0
#
#         def dfs(node, remain):
#             if not node:
#                 return 0
#             count = 0
#             if node.val == remain:
#                 count += 1
#             count += dfs(node.left, remain - node.val)
#             count += dfs(node.right, remain - node.val)
#             return count
#
#         # 以当前节点为起点 + 以左右子树任意节点为起点
#         return dfs(root, targetSum) + \
#                self.pathSum(root.left, targetSum) + \
#                self.pathSum(root.right, targetSum)

# @lc code=end



#
# @lcpr case=start
# [10,5,-3,3,2,null,11,3,-2,null,1]\n8\n
# @lcpr case=end

# @lcpr case=start
# [5,4,8,11,null,13,4,7,2,null,null,5,1]\n22\n
# @lcpr case=end

#


def build_tree(values):
    """
    根据层序遍历列表构建二叉树
    None 表示空节点
    """
    if not values:
        return None

    root = TreeNode(values[0])
    queue = [root]
    i = 1

    while queue and i < len(values):
        node = queue.pop(0)

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


if __name__ == "__main__":
    sol = Solution()

    # 测试用例 1：基本示例
    #       10
    #      /  \
    #     5   -3
    #    / \    \
    #   3   2   11
    #  / \   \
    # 3  -2   1
    nums1 = [10, 5, -3, 3, 2, None, 11, 3, -2, None, 1]
    root1 = build_tree(nums1)
    target1 = 8
    result1 = sol.pathSum(root1, target1)
    print(f"Test 1: targetSum={target1}")
    print(f"Result: {result1}")
    # 路径：5->3, 5->2->1, -3->11, 10->5->-3->-3? 不对
    # 实际路径：5->3, 5->2->1, -3->11, 以及 3->5 不行（必须向下）
    # 正确路径：5->3, 5->2->1, -3->11
    # 还有 10->5->-3 不是 8
    assert result1 == 3, f"Expected 3, got {result1}"
    print("Passed!\n")

    # 测试用例 2
    nums2 = [5, 4, 8, 11, None, 13, 4, 7, 2, None, None, 5, 1]
    root2 = build_tree(nums2)
    target2 = 22
    result2 = sol.pathSum(root2, target2)
    print(f"Test 2: targetSum={target2}")
    print(f"Result: {result2}")
    assert result2 == 3, f"Expected 3, got {result2}"
    print("Passed!\n")

    # 测试用例 3：空树
    result3 = sol.pathSum(None, 1)
    print(f"Test 3: root=None, targetSum=1")
    print(f"Result: {result3}")
    assert result3 == 0, f"Expected 0, got {result3}"
    print("Passed!\n")

    # 测试用例 4：单节点
    root4 = build_tree([1])
    result4 = sol.pathSum(root4, 1)
    print(f"Test 4: root=[1], targetSum=1")
    print(f"Result: {result4}")
    assert result4 == 1, f"Expected 1, got {result4}"
    print("Passed!\n")

    # 测试用例 5：包含负数
    root5 = build_tree([1, -2, -3])
    result5 = sol.pathSum(root5, -1)
    print(f"Test 5: root=[1,-2,-3], targetSum=-1")
    print(f"Result: {result5}")
    # 路径：1->-2 = -1
    assert result5 == 1, f"Expected 1, got {result5}"
    print("Passed!\n")

    print("All tests passed!")
