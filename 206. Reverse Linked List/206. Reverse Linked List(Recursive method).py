# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution(object):
    retNode = None

    def reverseList(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        
        def recurs(node):
            if node.next is None:
                self.retNode = ListNode(node.val, self.retNode)
            else:
                self.retNode = ListNode(node.val, self.retNode)
                recurs(node.next)
        if head:
            recurs(head)
        return self.retNode

            


        