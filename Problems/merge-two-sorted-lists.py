# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def mergeTwoLists(self, list1, list2):
        if list1 is None:
            return list2
        elif list2 is None:
            return list1
        head = None
        while list1 or list2:
            if list1 and list2:
                if list1.val <= list2.val:
                    node = ListNode(list1.val)
                    list1 = list1.next
                else:
                    node = ListNode(list2.val)
                    list2 = list2.next

            elif list1 is None:
                node = ListNode(list2.val)
                list2 = list2.next
            else:
                node = ListNode(list1.val)
                list1 = list1.next
            if head is None:
                head = node
                root = node
            else:
                root.next = node
                root = node
        return head
