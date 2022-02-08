# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def reverseList(self, head):
        if head is None:
            return head
        if head.next is None:
            return head
        node1 = self.reverseList(head.next)
        head.next.next = head
        head.next = None
        return node1

    # simply way
    # def reverseList(self, head):
    #     prev = None
    #     while head:
    #         curr = head
    #         head = head.next
    #         curr.next = prev
    #         prev = curr
    #     return prev
