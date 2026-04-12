# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution(object):
    def middleNode(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        curr = head
        count, mid = 0,0
        while curr:
            count+=1
            curr = curr.next
        if count % 2 == 0:
            mid = count/2
            mid += 1
        else:
            mid = (count+1) / 2
        curr = head
        while curr:
            if mid == 1:
                return curr
            mid -= 1
            curr = curr.next



        