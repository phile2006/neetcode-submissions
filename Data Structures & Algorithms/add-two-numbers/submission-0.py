# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        l1_val = ""
        while l1:
            l1_val += str(l1.val)
            l1 = l1.next
        
        l2_val = ""
        while l2:
            l2_val += str(l2.val)
            l2 = l2.next
        
        val1 = int(l1_val[::-1])
        val2 = int(l2_val[::-1])

        val3 = str(val1 + val2)[::-1]
        ret = head = ListNode(int(val3[0]))
        for i in val3[1:]:
            head.next = ListNode(int(i))
            head = head.next
        
        return ret