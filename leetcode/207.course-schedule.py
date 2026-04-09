#
# @lc app=leetcode.cn id=207 lang=python3
# @lcpr version=30204
#
# [207] 课程表
#


# @lcpr-template-start
from typing import List
# @lcpr-template-end
# @lc code=start
class Solution:
    """
    课程表 - 拓扑排序（DFS判环）

    问题描述：
    你这个学期必须选修 numCourses 门课程，记为 0 到 numCourses-1。
    在选修某些课程之前需要一些先修课程。先修课程按数组 prerequisites 给出，
    其中 prerequisites[i] = [ai, bi]，表示如果要学习课程 ai 则必须先学习课程 bi。
    请你判断是否可能完成所有课程的学习？

    核心思路：
    本题本质上是判断有向图中是否存在环。
    - 课程作为节点
    - 先修关系作为有向边（bi -> ai 表示必须先学 bi 才能学 ai）
    - 如果能完成所有课程，说明图中无环（存在拓扑排序）

    算法选择：
    1. DFS + 三色标记法：检测是否存在后向边（环）
    2. Kahn算法（BFS + 入度）：不断移除入度为0的节点

    三色标记法：
    - 0（白色）：未访问
    - 1（灰色）：正在访问中（在当前DFS路径上）
    - 2（黑色）：已访问完毕

    如果发现指向灰色节点的边，说明存在环。

    时间复杂度：O(V + E) - V为课程数，E为先修关系数
    空间复杂度：O(V + E) - 邻接表和访问标记数组
    """

    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        """
        判断是否可能完成所有课程的学习

        参数：
            numCourses: 课程总数
            prerequisites: 先修关系列表，[a, b] 表示学a前必须先学b
        """
        # 题意：给你一个有向图，判断图中是否有环。
        # 题目限定 0 <= ai, bi < numCourses，则课程编号严格在 0 到 numCourses-1 范围内。
        # prerequisites 只给出了有依赖关系的课程对，numCourses 是必须的，因为可能有孤立节点

        # 构建邻接表（有向图）
        # g[b] 表示学完课程 b 后可以学的课程列表
        g = [[] for _ in range(numCourses)]
        for a, b in prerequisites:
            g[b].append(a)  # b -> a 的边

        # 三色标记法
        # colors[i] = 0: 未访问（白色）
        # colors[i] = 1: 正在访问中（灰色）
        # colors[i] = 2: 已访问完毕（黑色）
        colors = [0] * numCourses

        def dfs(x: int) -> bool:
            """
            DFS 遍历节点 x
            返回 True 表示找到了环
            """
            colors[x] = 1  # x 正在访问中（标记为灰色）

            for y in g[x]:
                # 情况一：colors[y] == 1，表示 y 在当前 DFS 路径上，发现环
                # 情况二：colors[y] == 0，没有访问过 y，继续递归 y
                # 情况三：colors[y] == 2，y 已完全访问，从 y 出发无法找到环，跳过
                if colors[y] == 1 or (colors[y] == 0 and dfs(y)):
                    return True  # 找到了环

            colors[x] = 2  # x 完全访问完毕（标记为黑色）
            return False  # 从 x 出发没有找到环

        # 遍历所有课程，对每个未访问的课程进行 DFS
        for i in range(numCourses):
            if colors[i] == 0 and dfs(i):
                return False  # 有环，无法完成所有课程

        return True  # 无环，可以完成所有课程

    def canFinishKahn(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        """
        Kahn算法（BFS + 入度）

        核心思想：
        不断找到入度为0的节点（没有先修要求的课程），移除它并更新相关边的入度。
        如果最终能移除所有节点，说明无环。
        """
        from collections import deque

        # 构建邻接表和入度数组
        g = [[] for _ in range(numCourses)]
        in_degree = [0] * numCourses

        for a, b in prerequisites:
            g[b].append(a)
            in_degree[a] += 1

        # 将所有入度为0的节点加入队列
        queue = deque()
        for i in range(numCourses):
            if in_degree[i] == 0:
                queue.append(i)

        visited = 0  # 记录访问过的节点数

        while queue:
            x = queue.popleft()
            visited += 1

            for y in g[x]:
                in_degree[y] -= 1
                if in_degree[y] == 0:
                    queue.append(y)

        # 如果所有节点都被访问过，说明无环
        return visited == numCourses


# @lc code=end



#
# @lcpr case=start
# 2\n[[1,0]]\n
# @lcpr case=end

# @lcpr case=start
# 2\n[[1,0],[0,1]]\n
# @lcpr case=end

#

if __name__ == "__main__":
    sol = Solution()

    # 测试用例 1：可以完成
    # 课程 0 是课程 1 的先修，无环
    numCourses1 = 2
    prerequisites1 = [[1, 0]]
    result1 = sol.canFinish(numCourses1, prerequisites1)
    print(f"Test 1: canFinish(2, [[1,0]]) = {result1}")
    assert result1 == True, f"Expected True, got {result1}"

    # 测试用例 2：有环，无法完成
    # 课程 0 依赖 1，课程 1 又依赖 0，形成环
    numCourses2 = 2
    prerequisites2 = [[1, 0], [0, 1]]
    result2 = sol.canFinish(numCourses2, prerequisites2)
    print(f"Test 2: canFinish(2, [[1,0],[0,1]]) = {result2}")
    assert result2 == False, f"Expected False, got {result2}"

    # 测试用例 3：无先修要求
    numCourses3 = 3
    prerequisites3 = []
    result3 = sol.canFinish(numCourses3, prerequisites3)
    print(f"Test 3: canFinish(3, []) = {result3}")
    assert result3 == True, f"Expected True, got {result3}"

    # 测试用例 4：链式依赖
    # 0 -> 1 -> 2 -> 3
    numCourses4 = 4
    prerequisites4 = [[1, 0], [2, 1], [3, 2]]
    result4 = sol.canFinish(numCourses4, prerequisites4)
    print(f"Test 4: canFinish(4, [[1,0],[2,1],[3,2]]) = {result4}")
    assert result4 == True, f"Expected True, got {result4}"

    # 测试用例 5：复杂有环
    # 0 -> 1 -> 2 -> 0 (环)
    numCourses5 = 3
    prerequisites5 = [[1, 0], [2, 1], [0, 2]]
    result5 = sol.canFinish(numCourses5, prerequisites5)
    print(f"Test 5: canFinish(3, [[1,0],[2,1],[0,2]]) = {result5}")
    assert result5 == False, f"Expected False, got {result5}"

    # 测试用例 6：Kahn算法测试
    result6 = sol.canFinishKahn(2, [[1, 0]])
    print(f"Test 6 (Kahn): canFinishKahn(2, [[1,0]]) = {result6}")
    assert result6 == True, f"Expected True, got {result6}"

    print("\nAll tests passed!")
