# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head):
        len_list = 0
        node = head
        while node:
            node = node.next
            len_list += 1
        mid = len_list // 2
        i = 0
        node = head
        while node:
            if i == mid:
                return node
            i+=1
            node = node.next
            
# another solution
# class Solution:
#     def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
#         slow = fast = head
#         while fast and fast.next:
#             slow = slow.next
#             fast = fast.next.next
#         return slow