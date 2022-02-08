# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head) -> bool:
        fast = head
        faster = head
        while faster and faster.next:
            fast = fast.next
            faster = faster.next.next
            if faster == fast:
                return True
            elif faster is None:
                return False