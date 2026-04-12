# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution(object):

    def reverseList(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        
        if not head or not head.next:
            return head
        
        newHead = self.reverseList(head.next)
        
        head.next.next = head
        head.next = None
        
        return newHead
if __name__ == "__main__":
    testCase = ListNode(1, ListNode(2, ListNode(3,ListNode(4, ListNode(5, None)))))
    a = Solution()
    l = list()
    curr = testCase
    while curr:
        l.append(curr.val)
        curr = curr.next
    print(l[::-1])
            


        