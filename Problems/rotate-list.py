# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head, k: int):
        if head is None:
            return head
        n = 1
        root = head
        while root.next:
            n += 1
            root = root.next
        k = k % n
        root.next = head
        root = head
        for _ in range(n-k-1):
            root = root.next
        ans = root.next
        root.next = None
        return ans
        
                