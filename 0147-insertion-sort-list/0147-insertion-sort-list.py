# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def insertionSortList(self, head):
        dummy = ListNode(0,head)
        prev,cur = head,head.next
        while cur:
            if cur.val >= prev.val:
                prev,cur = cur,cur.next
                continue
            #if cur < prev
            temp = dummy
            #if cur > temp, move cur and temp to next node
            while cur.val > temp.next.val:
                temp = temp.next
            #else cur < temp
            prev.next = cur.next
            cur.next = temp.next
            temp.next = cur
            cur = prev.next
        return dummy.next
        