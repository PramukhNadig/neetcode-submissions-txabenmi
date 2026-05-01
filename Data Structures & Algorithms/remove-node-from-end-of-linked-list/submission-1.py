# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        sent = head
        N = n
        while n:
            sent = sent.next
            n -= 1
        remove = head
        prev = None
        while sent:
            prev = remove
            remove = remove.next
            sent = sent.next
        if remove == head:
            return head.next
        if remove and remove.next:
            prev.next = remove.next
        else:
            prev.next = None
        return head