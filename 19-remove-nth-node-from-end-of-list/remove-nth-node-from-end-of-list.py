# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        '''size=0 wrong so check
        curr=head
        while curr:
            size+=1
            curr=curr.next
            idx=size-n
            for i in range(idx):
                curr.next'''
        dummy=ListNode(0,head)
        fast=dummy
        slow=dummy
        for i in range(n):
            fast=fast.next
        while fast.next:
            slow=slow.next
            fast=fast.next
        slow.next=slow.next.next   
        return dummy.next



        