# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution(object):
    def mergeTwoLists(self, list1, list2):

        dummy = ListNode()

        curr = dummy

        while list1 or list2:
            if list1 and list2:

                if list1.val > list2.val:
                    curr.next = list2
                    list2 = list2.next
                    curr = curr.next
                else:
                    curr.next = list1
                    list1 = list1.next
                    curr = curr.next
                continue

            if list1:
                curr.next = list1
                return dummy.next
            if list2:
                curr.next = list2
                return dummy.next

        """
        :type list1: Optional[ListNode]
        :type list2: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        