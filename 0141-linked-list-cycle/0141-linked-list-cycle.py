# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        if head is None:
            return False
        arr = [head]
        head = head.next
        while head:
            if head.next in arr: 
                return True
            else:
                arr.append(head)
                head = head.next
        return False