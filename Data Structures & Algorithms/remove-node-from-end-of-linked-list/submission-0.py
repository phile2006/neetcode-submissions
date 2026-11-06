# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        cur = head
        lst = []
        while cur:
            lst.append(cur)
            cur = cur.next

        l = len(lst)
        ind = l - n #where it has to add the value next.next, meaning 1 value before the val removed

        if ind == 0:
            return head.next
        lst[ind - 1].next =lst[ind].next
        return head