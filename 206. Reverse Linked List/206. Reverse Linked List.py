# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def reverseList(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        # while node.next not None:
        #     node.val, node.next = node.next, node.val
        #     node = node.next
        l = list()
        node = head
        if head:
            while node.next is not None:
                l.append(node.val)
                node = node.next
            l.append(node.val)
        return l[::-1]

            


        