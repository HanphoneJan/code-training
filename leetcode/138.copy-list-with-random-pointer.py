#
# @lc app=leetcode.cn id=138 lang=python3
# @lcpr version=30204
#
# [138] 随机链表的复制
#


# @lcpr-template-start

# @lcpr-template-end
# @lc code=start
"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

# 早早直接上哈希，不要犹豫
# class Solution:
#     def copyRandomList(self, head: 'Node') -> 'Node':
#         if not head: return
#         dic = {}
#         # 复制各节点，并建立 “原节点 -> 新节点” 的 Map 映射
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
    
# 交错链表做法
class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        # 复制每个节点，把新节点直接插到原节点的后面
        cur = head
        while cur:
            cur.next = Node(cur.val, cur.next)
            cur = cur.next.next

        # 遍历交错链表中的原链表节点
        cur = head
        while cur:
            if cur.random:
                # 要复制的 random 是 cur.random 的下一个节点
                cur.next.random = cur.random.next
            cur = cur.next.next

        # 把交错链表分离成两个链表
        tail = dummy = Node(0, head)
        cur = head
        while cur:
            copy = cur.next  # 新节点
            tail.next = copy  # 把新节点插在 tail 的后面，构建新的链表
            cur.next = copy.next  # 恢复原节点的 next
            cur = cur.next
            tail = tail.next

        return dummy.next  # what，只改变了一次？这能想到，是人？


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

#

