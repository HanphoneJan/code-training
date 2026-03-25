#
# @lc app=leetcode.cn id=102 lang=python3
# @lcpr version=30204
#
# [102] 二叉树的层序遍历
#

# @lcpr-template-start
from typing import List, Optional
from collections import deque


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
    二叉树的层序遍历 - BFS

    核心思想：
    使用队列（BFS）按层遍历二叉树。每一轮处理当前层的所有节点，
    并将它们的子节点加入队列，供下一轮处理。

    算法步骤：
    1. 初始化队列，加入根节点
    2. 当队列不为空时：
       a. 记录当前队列长度（即当前层的节点数）
       b. 依次处理当前层的所有节点，将值存入当前层结果
       c. 将子节点加入队列
    3. 返回按层组织的结果

    时间复杂度：O(n)，每个节点访问一次
    空间复杂度：O(n)，队列最多存储一层的节点数
    """

    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        """
        执行二叉树的层序遍历

        Args:
            root: 二叉树的根节点

        Returns:
            按层组织的节点值列表，例如 [[3], [9, 20], [15, 7]]
        """
        # 空树处理：如果根节点为空，直接返回空列表
        if not root:
            return []

        res: List[List[int]] = []  # 存储最终结果
        cur: deque[TreeNode] = deque([root])  # 初始化队列，加入根节点

        # BFS 遍历：当队列不为空时继续
        while cur:
            level_size = len(cur)  # 当前层的节点数量
            level_values: List[int] = []  # 存储当前层的节点值

            # 遍历当前层的所有节点（共 level_size 个）
            for _ in range(level_size):
                # 从队列左侧取出节点
                node = cur.popleft()
                # 记录当前节点的值
                level_values.append(node.val)

                # 将左子节点加入队列（如果存在）
                if node.left:
                    cur.append(node.left)
                # 将右子节点加入队列（如果存在）
                if node.right:
                    cur.append(node.right)

            # 当前层遍历完成，将结果加入最终列表
            res.append(level_values)

        return res


# @lc code=end


#
# @lcpr case=start
# [3,9,20,null,null,15,7]\n
# @lcpr case=end

# @lcpr case=start
# [1]\n
# @lcpr case=end

# @lcpr case=start
# []\n
# @lcpr case=end

#


# 可运行测试用例
if __name__ == "__main__":
    sol = Solution()

    # 辅助函数：根据层序遍历列表构建二叉树
    def build_tree(values: List[Optional[int]]) -> Optional[TreeNode]:
        """根据层序遍历列表构建二叉树

        Args:
            values: 层序遍历列表，None 表示空节点

        Returns:
            构建好的二叉树根节点
        """
        if not values or values[0] is None:
            return None

        root = TreeNode(values[0])
        queue: deque[TreeNode] = deque([root])
        i = 1

        while queue and i < len(values):
            node = queue.popleft()

            # 处理左子节点
            if i < len(values) and values[i] is not None:
                left_val: int = values[i]  # type: ignore
                node.left = TreeNode(left_val)
                queue.append(node.left)
            i += 1

            # 处理右子节点
            if i < len(values) and values[i] is not None:
                right_val: int = values[i]  # type: ignore
                node.right = TreeNode(right_val)
                queue.append(node.right)
            i += 1

        return root

    # 测试用例列表：(输入树, 预期输出)
    tests = [
        # 测试用例 1：完整二叉树 [3,9,20,null,null,15,7]
        #       3
        #      / \
        #     9  20
        #       /  \
        #      15   7
        # 预期输出：[[3], [9, 20], [15, 7]]
        ([3, 9, 20, None, None, 15, 7], [[3], [9, 20], [15, 7]]),
        # 测试用例 2：单节点树 [1]
        #       1
        # 预期输出：[[1]]
        ([1], [[1]]),
        # 测试用例 3：空树 []
        # 预期输出：[]
        ([], []),
        # 测试用例 4：只有左子树 [1,2,null,3,null]
        #       1
        #      /
        #     2
        #    /
        #   3
        # 预期输出：[[1], [2], [3]]
        ([1, 2, None, 3], [[1], [2], [3]]),
        # 测试用例 5：只有右子树 [1,null,2,null,3]
        #       1
        #        \
        #         2
        #          \
        #           3
        # 预期输出：[[1], [2], [3]]
        ([1, None, 2, None, 3], [[1], [2], [3]]),
    ]

    print("=" * 50)
    print("二叉树的层序遍历 - 测试开始")
    print("=" * 50)

    all_passed = True
    for i, (values, expected) in enumerate(tests, 1):
        root = build_tree(values)
        result = sol.levelOrder(root)
        passed = result == expected
        all_passed = all_passed and passed
        status = "✓ PASS" if passed else "✗ FAIL"
        print(f"\n测试 {i}: {status}")
        print(f"  输入: {values}")
        print(f"  输出: {result}")
        print(f"  预期: {expected}")

    print("\n" + "=" * 50)
    print(f"所有测试 {'通过' if all_passed else '未通过'}！")
    print("=" * 50)