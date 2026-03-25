#
# @lc app=leetcode.cn id=102 lang=python3
# @lcpr version=30204
#
# [102] 二叉树的层序遍历
#


# 可运行测试用例
if __name__ == "__main__":
    sol = Solution()

    # 构建测试树: [3,9,20,null,null,15,7]
    root1 = TreeNode(3)
    root1.left = TreeNode(9)
    root1.right = TreeNode(20)
    root1.right.left = TreeNode(15)
    root1.right.right = TreeNode(7)

    # 构建测试树: [1]
    root2 = TreeNode(1)

    tests = [
        (root1, [[3], [9, 20], [15, 7]]),
        (root2, [[1]]),
        (None, []),
    ]

    print("二叉树的层序遍历 - 测试开始")
    for i, (root, expected) in enumerate(tests, 1):
        result = sol.levelOrder(root)
        passed = result == expected
        status = "✓ PASS" if passed else "✗ FAIL"
        print(f"测试 {i}: {status}")
    print("测试结束") @lcpr-template-start

# @lcpr-template-end
# @lc code=start
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

from typing import List, Optional
from collections import deque


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
        if not root:
            return []

        res = []
        cur = deque([root])  # 当前层的节点队列

        while cur:
            value = []  # 当前层的节点值
            # 遍历当前层的所有节点
            for _ in range(len(cur)):
                node = cur.popleft()
                value.append(node.val)
                # 将子节点加入队列，准备下一层遍历
                if node.left:
                    cur.append(node.left)
                if node.right:
                    cur.append(node.right)
            res.append(list(value))

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

