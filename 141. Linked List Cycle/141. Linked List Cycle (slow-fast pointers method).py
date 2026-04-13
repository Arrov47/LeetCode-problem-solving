# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def hasCycle(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        if head is None:
            return False
        sPtr = fPtr = head
        while fPtr and fPtr.next:
            sPtr = sPtr.next
            fPtr = fPtr.next.next
            if sPtr == fPtr:
                return True
        return False

        