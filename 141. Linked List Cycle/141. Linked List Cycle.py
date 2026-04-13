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
        isCycle = False
        curr = head
        while curr:
            if curr.next == None:
                break
            elif curr.val == "":  # checking if node was traversed in the past, if it was,
                isCycle = True    # then we can say that this LinkedList has a cycle
                break
            else:
                curr.val = "" # marking traversed node as True
                curr = curr.next
        return isCycle

        