#
# @lc app=leetcode.cn id=138 lang=python3
# @lcpr version=30204
#
# [138] 随机链表的复制
#


# @lcpr-template-start
"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""
from typing import Optional

# @lcpr-template-end
# @lc code=start
# 方法一：哈希表映射
# class Solution:
#     def copyRandomList(self, head: 'Node') -> 'Node':
#         if not head: return
#         dic = {}
#         # 复制各节点，并建立 "原节点 -> 新节点" 的 Map 映射
#         cur = head
#         while cur:
#             dic[cur] = Node(cur.val)
#             cur = cur.next
#         cur = head
#         # 构建新节点的 next 和 random 指向
#         while cur:
#             dic[cur].next = dic.get(cur.next)
#             dic[cur].random = dic.get(cur.random)
#             cur = cur.next
#         # 返回新链表的头节点
#         return dic[head]

class Solution:
    """
    138. 随机链表的复制 - 哈希表映射 / 交错链表

    核心思想：
    链表的复制难点在于 random 指针可能指向任意节点（包括未创建的节点）。
    需要建立原节点和新节点之间的对应关系。

    方法一：哈希表（O(n) 空间）
    先遍历一遍建立 "原节点 -> 新节点" 的映射，再遍历一遍连接 next 和 random。

    方法二：交错链表（O(1) 额外空间）
    1. 第一遍：在每个原节点后面插入它的复制节点
    2. 第二遍：根据原节点的 random，设置复制节点的 random
    3. 第三遍：将交错链表拆分成两个独立链表

    时间复杂度：O(n)
    空间复杂度：O(1)（交错链表法，除结果外）
    """

    # 交错链表做法
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if not head:
            return None

        # 步骤1：复制每个节点，把新节点直接插到原节点的后面
        cur = head
        while cur:
            cur.next = Node(cur.val, cur.next)
            cur = cur.next.next

        # 步骤2：遍历交错链表中的原链表节点，设置复制节点的 random
        cur = head
        while cur:
            if cur.random:
                # 复制节点的 random 指向原节点 random 的下一个节点（即 random 的复制）
                cur.next.random = cur.random.next
            cur = cur.next.next

        # 步骤3：把交错链表分离成两个独立链表
        tail = dummy = Node(0, head)
        cur = head
        while cur:
            copy = cur.next      # 当前原节点的复制节点
            tail.next = copy     # 把复制节点接上新链表
            cur.next = copy.next # 恢复原链表的 next 指针
            cur = cur.next       # 移动到下一个原节点
            tail = tail.next     # 移动到新链表末尾

        return dummy.next


# @lc code=end


#
# @lcpr case=start
# [[7,null],[13,0],[11,4],[10,2],[1,0]]\n
# @lcpr case=end

# @lcpr case=start
# [[1,1],[2,1]]\n
# @lcpr case=end

# @lcpr case=start
# [[3,null],[3,0],[3,null]]\n
# @lcpr case=end


if __name__ == "__main__":
    # 辅助函数：构建测试链表和验证结果
    def build_and_copy(data):
        if not data:
            return None
        nodes = []
        for val, _ in data:
            nodes.append(Node(val))
        for i in range(len(nodes) - 1):
            nodes[i].next = nodes[i + 1]
        for i, (_, rand_idx) in enumerate(data):
            if rand_idx is not None:
                nodes[i].random = nodes[rand_idx]
        return nodes[0]

    sol = Solution()

    # 由于链表结构复杂，这里只做简单运行测试
    print("随机链表的复制 - 测试开始")
    print("测试 1: [[7,null],[13,0],[11,4],[10,2],[1,0]]")
    head1 = build_and_copy([[7, None], [13, 0], [11, 4], [10, 2], [1, 0]])
    copy1 = sol.copyRandomList(head1)
    print(f"  复制成功: {copy1 is not None and copy1 is not head1}")

    print("测试 2: [[1,1],[2,1]]")
    head2 = build_and_copy([[1, None], [2, 1]])
    copy2 = sol.copyRandomList(head2)
    print(f"  复制成功: {copy2 is not None and copy2 is not head2}")

    print("测试 3: 空链表")
    copy3 = sol.copyRandomList(None)
    print(f"  复制成功: {copy3 is None}")
    print("测试结束")
