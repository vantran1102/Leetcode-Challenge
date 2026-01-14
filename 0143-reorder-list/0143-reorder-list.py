# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        if not head or not head.next:
            return
        prev = None
        slow, fast = head, head
        #Split in 2 halves
        while fast and fast.next:
            prev = slow
            slow = slow.next
            fast = fast.next.next
        prev.next = None
        l1 = head
        l2 = slow
        #Reverse second halves
        prev2 = None
        cur = l2
        while cur:
            nxt = cur.next
            cur.next = prev2
            prev2 = cur
            cur = nxt
        l2 = prev2
        #Merge two halves
        tail = None
        while l1 and l2:
            n1 = l1.next
            n2 = l2.next
            l1.next = l2
            l2.next = n1
            tail = l2
            l1 = n1
            l2 = n2
        if l2 and tail:
            tail.next = l2
        return

        