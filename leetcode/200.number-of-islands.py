#
# @lc app=leetcode.cn id=200 lang=python3
# @lcpr version=30204
#
# [200] 岛屿数量
#


# @lcpr-template-start
from typing import List
from collections import deque
# @lcpr-template-end
# @lc code=start
class Solution:
    """
    岛屿数量 - DFS/BFS

    问题描述：
    给你一个由 '1'（陆地）和 '0'（水）组成的的二维网格，请你计算网格中岛屿的数量。
    岛屿总是被水包围，并且每座岛屿只能由水平方向和/或竖直方向上相邻的陆地连接形成。
    此外，你可以假设该网格的四条边均被水包围。

    核心思路：
    遍历整个网格，当遇到 '1'（未访问的陆地）时，发现一个新岛屿。
    然后使用 DFS 或 BFS 将与这块陆地相连的所有陆地标记为已访问（改为 '2' 或其他标记）。
    继续遍历，直到整个网格都被处理完毕。

    为什么标记为 '2' 而不是 '0'？
    - 标记为 '0' 也可以，但会改变原始数据的语义（'0' 原本表示水）
    - 使用 '2' 可以区分"水"和"已访问的陆地"，便于调试

    时间复杂度：O(m×n) - 每个格子最多被访问一次
    空间复杂度：O(m×n) - DFS 递归栈或 BFS 队列的最坏情况
    """

    def numIslands(self, grid: List[List[str]]) -> int:
        """
        计算网格中岛屿的数量
        """
        if not grid or not grid[0]:
            return 0

        rows = len(grid)
        cols = len(grid[0])
        count = 0

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == '1':
                    count += 1
                    # 使用 DFS 或 BFS 标记整个岛屿
                    self._dfs(grid, r, c)
                    # self._bfs(grid, r, c)

        return count

    def _dfs(self, grid: List[List[str]], r: int, c: int) -> None:
        """
        DFS 深度优先搜索：标记与 (r, c) 相连的所有陆地

        参数：
            grid: 二维网格数组，'1'=未访问的陆地，'0'=水，'2'=已访问的陆地
            r, c: 当前格子的行号和列号
        """
        # 1. 判断 base case：坐标超出网格范围，或不是未访问的陆地
        if r < 0 or r >= len(grid) or c < 0 or c >= len(grid[0]) or grid[r][c] != '1':
            return

        # 2. 标记当前格子为「已遍历」，避免重复访问
        grid[r][c] = '2'

        # 3. 递归访问上、下、左、右四个相邻格子
        self._dfs(grid, r - 1, c)  # 上
        self._dfs(grid, r + 1, c)  # 下
        self._dfs(grid, r, c - 1)  # 左
        self._dfs(grid, r, c + 1)  # 右

    def _bfs(self, grid: List[List[str]], r: int, c: int) -> None:
        """
        BFS 广度优先搜索：标记与 (r, c) 相连的所有陆地
        """
        rows, cols = len(grid), len(grid[0])
        queue = deque([(r, c)])
        grid[r][c] = '2'  # 标记起点

        while queue:
            curr_r, curr_c = queue.popleft()

            # 检查四个方向
            for dr, dc in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                nr, nc = curr_r + dr, curr_c + dc
                if 0 <= nr < rows and 0 <= nc < cols and grid[nr][nc] == '1':
                    grid[nr][nc] = '2'
                    queue.append((nr, nc))


# @lc code=end



#
# @lcpr case=start
# [['1','1','1','1','0'],['1','1','0','1','0'],['1','1','0','0','0'],['0','0','0','0','0']]\n
# @lcpr case=end

# @lcpr case=start
# [['1','1','0','0','0'],['1','1','0','0','0'],['0','0','1','0','0'],['0','0','0','1','1']]\n
# @lcpr case=end

#

if __name__ == "__main__":
    sol = Solution()

    # 测试用例 1：单个岛屿
    grid1 = [
        ['1', '1', '1', '1', '0'],
        ['1', '1', '0', '1', '0'],
        ['1', '1', '0', '0', '0'],
        ['0', '0', '0', '0', '0']
    ]
    result1 = sol.numIslands([row[:] for row in grid1])  # 深拷贝
    print(f"Test 1: numIslands(grid1) = {result1}")
    assert result1 == 1, f"Expected 1, got {result1}"

    # 测试用例 2：三个岛屿
    grid2 = [
        ['1', '1', '0', '0', '0'],
        ['1', '1', '0', '0', '0'],
        ['0', '0', '1', '0', '0'],
        ['0', '0', '0', '1', '1']
    ]
    result2 = sol.numIslands([row[:] for row in grid2])
    print(f"Test 2: numIslands(grid2) = {result2}")
    assert result2 == 3, f"Expected 3, got {result2}"

    # 测试用例 3：空网格
    grid3 = []
    result3 = sol.numIslands(grid3)
    print(f"Test 3: numIslands([]) = {result3}")
    assert result3 == 0, f"Expected 0, got {result3}"

    # 测试用例 4：全是水
    grid4 = [
        ['0', '0', '0'],
        ['0', '0', '0']
    ]
    result4 = sol.numIslands([row[:] for row in grid4])
    print(f"Test 4: numIslands(all water) = {result4}")
    assert result4 == 0, f"Expected 0, got {result4}"

    # 测试用例 5：全是陆地（一个岛屿）
    grid5 = [
        ['1', '1'],
        ['1', '1']
    ]
    result5 = sol.numIslands([row[:] for row in grid5])
    print(f"Test 5: numIslands(all land) = {result5}")
    assert result5 == 1, f"Expected 1, got {result5}"

    # 测试用例 6：对角线不是相邻
    grid6 = [
        ['1', '0', '1'],
        ['0', '1', '0'],
        ['1', '0', '1']
    ]
    result6 = sol.numIslands([row[:] for row in grid6])
    print(f"Test 6: numIslands(diagonal) = {result6}")
    assert result6 == 5, f"Expected 5, got {result6}"
    # 对角线不相连，所以是 5 个独立岛屿

    print("\nAll tests passed!")
