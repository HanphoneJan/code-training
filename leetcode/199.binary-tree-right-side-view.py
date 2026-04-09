#
# @lc app=leetcode.cn id=199 lang=python3
# @lcpr version=30204
#
# [199] 二叉树的右视图
#


# @lcpr-template-start
from typing import List, Optional
from collections import deque

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
    二叉树的右视图 - BFS层序遍历

    问题描述：
    给定一个二叉树的根节点 root，想象自己站在它的右侧，
    按照从顶部到底部的顺序，返回从右侧所能看到的节点值。

    核心思路：
    本质上是返回每一层最右侧的节点。
    使用 BFS 层序遍历，对于每一层，最后一个出队的节点就是该层最右侧的节点。

    为什么用 BFS？
    BFS 天然按层遍历，可以方便地获取每一层的所有节点，然后取最后一个。

    时间复杂度：O(n) - 每个节点访问一次
    空间复杂度：O(w) - w 为树的最大宽度，队列最多存储一层的节点数
    """

    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        """
        返回二叉树的右视图
        """
        if not root:
            return []

        result = []
        queue = deque([root])

        while queue:
            current_level_size = len(queue)

            for i in range(current_level_size):
                node = queue.popleft()

                # 当前层的最后一个节点，加入结果
                if i == current_level_size - 1:
                    result.append(node.val)

                # 将子节点加入队列（先左后右不影响结果，因为我们只取最后一个）
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)

        return result


# @lc code=end



#
# @lcpr case=start
# [1,2,3,null,5,null,4]\n
# @lcpr case=end

# @lcpr case=start
# [1,2,3,4,null,null,null,5]\n
# @lcpr case=end

# @lcpr case=start
# [1,null,3]\n
# @lcpr case=end

# @lcpr case=start
# []\n
# @lcpr case=end

#

if __name__ == "__main__":
    sol = Solution()

    # 辅助函数：根据层序遍历列表构建二叉树
    def build_tree(values):
        """根据层序遍历列表构建二叉树，None 表示空节点"""
        if not values or values[0] is None:
            return None

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
    #       1
    #      / \
    #     2   3
    #      \   \
    #       5   4
    root1 = build_tree([1, 2, 3, None, 5, None, 4])
    result1 = sol.rightSideView(root1)
    print(f"Test 1: rightSideView([1,2,3,null,5,null,4]) = {result1}")
    assert result1 == [1, 3, 4], f"Expected [1, 3, 4], got {result1}"

    # 测试用例 2：左子树很深
    #       1
    #      / \
    #     2   3
    #    /
    #   4
    #  /
    # 5
    root2 = build_tree([1, 2, 3, 4, None, None, None, 5])
    result2 = sol.rightSideView(root2)
    print(f"Test 2: rightSideView([1,2,3,4,null,null,null,5]) = {result2}")
    assert result2 == [1, 3, 4, 5], f"Expected [1, 3, 4, 5], got {result2}"

    # 测试用例 3：只有右子树
    #   1
    #    \
    #     3
    root3 = build_tree([1, None, 3])
    result3 = sol.rightSideView(root3)
    print(f"Test 3: rightSideView([1,null,3]) = {result3}")
    assert result3 == [1, 3], f"Expected [1, 3], got {result3}"

    # 测试用例 4：空树
    root4 = build_tree([])
    result4 = sol.rightSideView(root4)
    print(f"Test 4: rightSideView([]) = {result4}")
    assert result4 == [], f"Expected [], got {result4}"

    # 测试用例 5：单节点
    root5 = build_tree([1])
    result5 = sol.rightSideView(root5)
    print(f"Test 5: rightSideView([1]) = {result5}")
    assert result5 == [1], f"Expected [1], got {result5}"

    print("\nAll tests passed!")
