#Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution(object):
    def isPalindrome(self, head):
        if not head or not head.next:
            return True
        slow, fast = head, head
        while fast and fast.next is not None:
            slow = slow.next
            fast = fast.next.next
        prev = None
        cur = slow

        while cur is not None:
            nxt = cur.next
            cur.next = prev
            prev = cur
            cur = nxt
        left = head
        right = prev
        while right:
            if left.val != right.val:
                return False
            left = left.next
            right = right.next
        return True

        