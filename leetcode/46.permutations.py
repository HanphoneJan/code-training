#
# @lc app=leetcode.cn id=46 lang=python3
# @lcpr version=30204
#
# [46] 全排列
#


# @lcpr-template-start

# @lcpr-template-end
# @lc code=start
from typing import List

class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        """
        全排列 - 回溯算法（DFS）

        回溯框架：
        def backtrack(路径, 选择列表):
            if 满足结束条件:
                收集结果
                return
            for 选择 in 选择列表:
                if 选择不合法: continue
                做选择        # 将选择加入路径，标记为已使用
                backtrack(新路径, 新选择列表)
                撤销选择      # 恢复现场，撤销标记

        本题特点：
        - 每个元素只能用一次，需要 visited 数组标记
        - 排列要求顺序不同算不同结果
        - 路径长度等于 n 时得到一个完整排列

        时间复杂度：O(n!) - n个元素的全排列数量
        空间复杂度：O(n) - 递归深度
        """
        ans = []      # 存储所有排列结果
        path = []     # 当前路径（一个排列的构建过程）
        n = len(nums)
        visited = [False] * n  # 标记哪些元素已被使用

        def dfs() -> None:
            """深度优先搜索构建排列"""
            # 结束条件：路径长度等于 n，得到一个完整排列
            if len(path) == n:
                ans.append(path[:])  # 必须复制，否则 path 变化会影响已保存的结果
                return

            # 遍历所有选择
            for i in range(n):
                if visited[i]:
                    continue  # 已使用的元素跳过

                # 做选择：将 nums[i] 加入路径
                visited[i] = True
                path.append(nums[i])

                # 递归进入下一层决策树
                dfs()

                # 撤销选择：恢复现场（回溯的关键）
                path.pop()
                visited[i] = False

        dfs()
        return ans

    def permuteSwap(self, nums: List[int]) -> List[List[int]]:
        """
        交换法实现全排列
        通过交换元素位置来生成排列，不需要 visited 数组
        """
        ans = []
        n = len(nums)

        def dfs(start: int) -> None:
            # 结束条件：到达最后一个位置
            if start == n:
                ans.append(nums[:])
                return

            # 从 start 开始，每个位置都可以放 start 及其后面的任意元素
            for i in range(start, n):
                # 交换：将 nums[i] 放到 start 位置
                nums[start], nums[i] = nums[i], nums[start]
                # 递归处理下一个位置
                dfs(start + 1)
                # 恢复：交换回来
                nums[start], nums[i] = nums[i], nums[start]

        dfs(0)
        return ans
# @lc code=end



#
# @lcpr case=start
# [1,2,3]\n
# @lcpr case=end

# @lcpr case=start
# [0,1]\n
# @lcpr case=end

# @lcpr case=start
# [1]\n
# @lcpr case=end

#

if __name__ == "__main__":
    sol = Solution()

    tests = [
        [1, 2, 3],
        [0, 1],
        [1],
    ]

    for nums in tests:
        result = sol.permute(nums)
        print(f"permute({nums}) = {result}")

