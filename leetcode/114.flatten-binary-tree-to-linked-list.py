#
# @lc app=leetcode.cn id=114 lang=python3
# @lcpr version=30204
#
# [114] 二叉树展开为链表
#

# @lcpr-template-start
from typing import Optional, List


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
    二叉树展开为链表 - O(1)空间复杂度

    核心思想：
    将二叉树展开为链表，展开后的链表应该与二叉树的前序遍历顺序相同。
    要求使用 O(1) 额外空间（不考虑递归栈），即原地修改。

    算法步骤（Morris遍历的变种）：
    1. 对于当前节点curr，如果它有左子树：
       a. 找到左子树的最右节点（前驱节点，即左子树中序遍历的最后一个节点）
       b. 将curr的右子树接到前驱节点的右边
       c. 将curr的左子树变为右子树，左子树置空
    2. curr移动到右子节点
    3. 重复直到curr为空

    为什么这样是正确的？
    - 前序遍历顺序：根 -> 左 -> 右
    - 左子树的最右节点是左子树前序遍历的最后一个节点
    - 将该节点的右指针指向原来的右子树，就能将"左子树前序序列"和"右子树前序序列"连起来
    - 然后将左子树移到右边，实现了原地展开

    时间复杂度：O(n)，每个节点访问常数次
    空间复杂度：O(1)，只使用常数额外空间
    """

    def flatten(self, root: Optional[TreeNode]) -> None:
        """
        将二叉树原地展开为链表（按前序遍历顺序）

        Args:
            root: 二叉树的根节点

        Returns:
            None（原地修改，不返回任何值）
        """
        curr = root

        while curr:
            if curr.left:
                # 找到左子树的最右节点（前驱节点）
                # 这个节点是左子树按照中序遍历的最后一个节点
                # 也是左子树前序遍历的最后一个节点
                predecessor = curr.left
                while predecessor.right:
                    predecessor = predecessor.right

                # 将当前节点的右子树接到前驱节点的右边
                # 这样左子树的前序遍历序列后面就能接上右子树
                predecessor.right = curr.right

                # 将左子树移到右边
                curr.right = curr.left
                # 左子树置空（链表只有右指针）
                curr.left = None

            # 移动到下一个节点（右子节点）
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


# 可运行测试用例
if __name__ == "__main__":
    sol = Solution()

    # 辅助函数：根据层序遍历列表构建二叉树
    from collections import deque

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

    # 辅助函数：获取链表形式的结果（按右指针遍历）
    def get_linked_list(root: Optional[TreeNode]) -> List[int]:
        """获取展开后的链表值序列"""
        result: List[int] = []
        curr = root
        while curr:
            result.append(curr.val)
            # 验证：展开后的链表应该只有右指针，左指针为None
            if curr.left is not None:
                raise ValueError(f"节点 {curr.val} 的左子节点不为空！")
            curr = curr.right
        return result

    # 辅助函数：获取二叉树的前序遍历
    def get_preorder(root: Optional[TreeNode]) -> List[int]:
        """获取二叉树的前序遍历序列"""
        if not root:
            return []
        return [root.val] + get_preorder(root.left) + get_preorder(root.right)

    # 测试用例列表：(输入树, 预期链表)
    tests = [
        # 测试用例 1：标准二叉树 [1,2,5,3,4,null,6]
        #       1
        #      / \
        #     2   5
        #    / \   \
        #   3   4   6
        # 前序遍历: [1,2,3,4,5,6]
        # 展开后的链表: 1 -> 2 -> 3 -> 4 -> 5 -> 6
        ([1, 2, 5, 3, 4, None, 6], [1, 2, 3, 4, 5, 6]),
        # 测试用例 2：空树 []
        ([], []),
        # 测试用例 3：单节点 [0]
        ([0], [0]),
        # 测试用例 4：只有左子树 [1,2,null,3,null]
        #       1
        #      /
        #     2
        #    /
        #   3
        # 前序遍历: [1,2,3]
        ([1, 2, None, 3], [1, 2, 3]),
        # 测试用例 5：只有右子树 [1,null,2,null,3]
        #       1
        #        \
        #         2
        #          \
        #           3
        # 前序遍历: [1,2,3]
        ([1, None, 2, None, 3], [1, 2, 3]),
        # 测试用例 6：复杂树 [1,2,3,4,5,6,7]
        #        1
        #       / \
        #      2   3
        #     / \  / \
        #    4  5 6  7
        # 前序遍历: [1,2,4,5,3,6,7]
        ([1, 2, 3, 4, 5, 6, 7], [1, 2, 4, 5, 3, 6, 7]),
    ]

    print("=" * 50)
    print("二叉树展开为链表 - 测试开始")
    print("=" * 50)

    all_passed = True
    for i, (values, expected) in enumerate(tests, 1):
        # 构建树
        root = build_tree(values)

        # 获取原始前序遍历（用于验证）
        original_preorder = get_preorder(root) if root else []

        # 执行展开
        sol.flatten(root)

        # 获取展开后的链表
        try:
            result = get_linked_list(root)
        except ValueError as e:
            result = []
            print(f"  错误: {e}")

        # 验证：链表结果应该等于原始前序遍历
        passed = result == expected and (not root or result == original_preorder)
        all_passed = all_passed and passed
        status = "✓ PASS" if passed else "✗ FAIL"

        print(f"\n测试 {i}: {status}")
        print(f"  输入树: {values}")
        print(f"  原始前序: {original_preorder}")
        print(f"  输出链表: {result}")
        print(f"  预期链表: {expected}")

    print("\n" + "=" * 50)
    print(f"所有测试 {'通过' if all_passed else '未通过'}！")
    print("=" * 50)