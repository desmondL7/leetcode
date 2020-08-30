# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None
class Solution:
    def deleteNode(self, head: ListNode, val: int) -> ListNode:
        tmp = head

        if head.val == val:
            return head.next

        p1 = head.next
        p2 = head

        while p1:
            if p1.val == val:
                p2.next = p1.next
                return head
            p1 = p1.next
            p2 = p2.next
        return head