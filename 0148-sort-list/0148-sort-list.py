# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def sortList(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        # Solution 1 (n^2 timecomplexity)
        # if head is None or head.next is None:
        #     return head

        # cur = head
        # while cur.next is not None:
        #     min, temp = cur, cur.next
        #     while temp is not None:
        #         if min.val > temp.val:
        #             min = temp
        #         temp = temp.next
        #     cur.val, min.val = min.val, cur.val
        #     cur = cur.next
        # return head

        # Solution 2 nlogn
        if head is None or head.next is None:
            return head
        arr = []
        while head is not None:
            arr.append(head.val)
            head = head.next
        arr.sort()
        head = ListNode(arr[0])
        cur = head
        for num in arr[1:]:
            newNode = ListNode(num)
            cur.next = newNode
            cur = cur.next
        return head

