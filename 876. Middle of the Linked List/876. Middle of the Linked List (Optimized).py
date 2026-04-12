# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def middleNode(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        slowNode, fastNode = head, head
        # the slowNode moves by 1 step. 
        # On the other hand, the fastNode moves by 2 steps
        while fastNode:
            if not fastNode.next:     # When fastNode reaches the end of the list,
                break                 # slowNode will be in the middle of the list
            slowNode = slowNode.next
            fastNode = fastNode.next.next
        return slowNode





        