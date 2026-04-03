#
# @lc app=leetcode.cn id=200 lang=python3
# @lcpr version=30204
#
# [200] 岛屿数量
#


# @lcpr-template-start

# @lcpr-template-end
# @lc code=start
def dfs(grid: List[List[str]], r: int, c: int) -> None:
    # param grid: 二维网格数组，1=未访问的岛屿，0=海洋/障碍，2=已访问的岛屿
    # 1. 判断 base case：坐标超出网格范围,不是未访问的岛屿（是海洋/已遍历）则返回
    if (not (0 <= r < len(grid) and 0 <= c < len(grid[0]))) or grid[r][c] != '1':
        return
    # 2. 标记当前格子为「已遍历」，避免重复访问
    grid[r][c] = '2'
    
    # 3. 递归访问上、下、左、右四个相邻结点
    dfs(grid, r - 1, c)  # 上
    dfs(grid, r + 1, c)  # 下
    dfs(grid, r, c - 1)  # 左
    dfs(grid, r, c + 1)  # 右

def bfs(grid, i, j):
    queue = deque()
    queue.extend([[i, j]])
    while queue:
        i, j = queue.popleft()
        if 0 <= i < len(grid) and 0 <= j < len(grid[0]) and grid[i][j] == '1':
            grid[i][j] = '2'  
            queue.extend([[i + 1, j], [i - 1, j], [i, j - 1], [i, j + 1]])

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        rows = len(grid)
        if rows == 0:
            return 0
        cols = len(grid[0])
        ans = 0
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == '1':
                    ans += 1
                    # 二选一运行即可
                    # bfs(grid,r,c)
                    dfs(grid,r,c)
        return ans


# @lc code=end



#
# @lcpr case=start
# [['1','1','1','1','0'],['1','1','0','1','0'],['1','1','0','0','0'],['0','0','0','0','0']]\n
# @lcpr case=end

# @lcpr case=start
# [['1','1','0','0','0'],['1','1','0','0','0'],['0','0','1','0','0'],['0','0','0','1','1']]\n
# @lcpr case=end

#

