# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

def reverseList( head):
    pre = None
    while head:
        tmp = head
        head = head.next
        tmp.next = pre
        pre = tmp

    return pre
