# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        # the prev node and the next node are important
        if not head:
            return head

        prevNode=None
        dummy=head
        n=0
        while dummy:
            dummy=dummy.next
            n+=1
        
        print(n)
        length=0
        # tail=None
        curr=head
        firstNode=None
        while n-length>=k:
            cntnd=0
            lstNode=curr
            tail=None
            while cntnd<k:
                nd=curr.next
                curr.next=tail
                tail=curr
                curr=nd
                cntnd+=1
            
            if not firstNode:
                firstNode=tail

            if(prevNode):
                prevNode.next=tail
            
            if(lstNode):
                prevNode=lstNode

            length+=cntnd
            print(length)

        prevNode.next=curr
        return firstNode






