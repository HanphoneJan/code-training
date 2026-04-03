#
# @lc app=leetcode.cn id=207 lang=python3
# @lcpr version=30204
#
# [207] 课程表
#


# @lcpr-template-start

# @lcpr-template-end
# @lc code=start
# 拓扑排序
# 题意：给你一个有向图，判断图中是否有环。
# 题目限定0 <= ai, bi < numCourses；则课程编号严格在 0 到 numCourses-1 范围内。
# prerequisites 只给出了有依赖关系的课程对，numsCourses是必须的，因为可能有孤立节点
from typing import List
class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        g = [[] for _ in range(numCourses)]
        for a, b in prerequisites:
            g[b].append(a)

        colors = [0] * numCourses
        # 返回 True 表示找到了环
        def dfs(x: int) -> bool:
            colors[x] = 1  # x 正在访问中
            for y in g[x]:
                # 情况一：colors[y] == 1，表示发生循环依赖，找到了环
                # 情况二：colors[y] == 0，没有访问过 y，继续递归 y 获取信息
                # 情况三：colors[y] == 2，重复访问 y 只会重蹈覆辙，和之前一样无法找到环，跳过
                if colors[y] == 1 or colors[y] == 0 and dfs(y):
                    return True  # 找到了环
            colors[x] = 2  # x 完全访问完毕，从 x 出发无法找到环
            return False  # 没有找到环

        for i, c in enumerate(colors):
            if c == 0 and dfs(i):
                return False  # 有环
        return True  # 没有环

# @lc code=end



#
# @lcpr case=start
# 2\n[[1,0]]\n
# @lcpr case=end

# @lcpr case=start
# 2\n[[1,0],[0,1]]\n
# @lcpr case=end

#

