# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def detectCycle(self, head):
        hashNodes = {}
        while head:
            if hashNodes.get(head) is None:
                hashNodes[head] = True
                head = head.next
            else:
                return head

# class Solution:
#     def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
#         turtle1 = rabbit = head
#         cycle = False
        
#         while rabbit and rabbit.next:
#             turtle1 = turtle1.next
#             rabbit = rabbit.next.next
#             if turtle1 == rabbit:
#                 cycle = True
#                 break
        
#         if not cycle:
#             return None
        
#         turtle2 = head
#         while turtle2 != turtle1:
#             turtle2 = turtle2.next
#             turtle1 = turtle1.next
#         return turtle1