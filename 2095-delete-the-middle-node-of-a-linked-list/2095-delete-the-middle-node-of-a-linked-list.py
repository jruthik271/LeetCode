# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def deleteMiddle(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: Optional[ListNode]
        """

        if not head.next:
            return None
        
        n=0
        curr=head
        while curr:
            n+=1
            curr=curr.next

        curr=head
        for i in range(n//2-1):
            curr=curr.next
        
        curr.next=curr.next.next
        

        return head