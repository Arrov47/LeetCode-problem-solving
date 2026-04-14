# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution(object):
    def mergeTwoLists(self, list1, list2):
        """
        :type list1: Optional[ListNode]
        :type list2: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        list3 = ListNode()
        if not list1 and not list2:
            return None

        ptr1, ptr2 = list1, list2
        if not ptr1:
            list3.val = ptr2.val
            ptr2 = ptr2.next if ptr2 else ptr2
        elif not ptr2:
            list3.val = ptr1.val
            ptr1 = ptr1.next if ptr1 else ptr1
        else:
            if ptr1.val < ptr2.val:
                list3.val = ptr1.val
                ptr1 = ptr1.next if ptr1 else ptr1
            else:
                list3.val = ptr2.val
                ptr2 = ptr2.next if ptr2 else ptr2

        ptr3 = list3

        while ptr1 or ptr2:
            if ptr1 and ptr2:
                ptr3.next = ptr1 if ptr1.val < ptr2.val else ptr2
            else:
                ptr3.next  = ptr1 if ptr1 else ptr2
            
            if ptr3.next == ptr1:
                ptr1 = ptr1.next if ptr1 else ptr1
            else:
                ptr2 = ptr2.next if ptr2 else ptr2
            ptr3 = ptr3.next if ptr3 else ptr3
        return list3

        
        
        

        