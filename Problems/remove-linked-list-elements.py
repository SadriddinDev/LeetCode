# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def removeElements(self, head, val: int):
        mylist = []
        root = head
        while root:
            mylist.append(root)
            root = root.next
        mylist = [i for i in mylist if i.val != val]
        for i in range(len(mylist) - 1):
            mylist[i].next = mylist[i + 1]
        if len(mylist) > 0:
            mylist[-1].next = None
            return mylist[0]
        else:
            return None
    # recursive method but memory take a lot
    # def removeElements(self, head, val: int):
    #     if head is None: return None
    #     head.next = self.removeElements(head.next, val)
    #     return head.next if head.val == val else head
              