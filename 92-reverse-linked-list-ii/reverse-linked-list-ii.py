# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        l=1
        hd=head
        prevhd=None
        while l<left:
            prevhd=hd
            hd=hd.next
            l+=1
        
        prev=None
        curr=hd
        r=l
        while l<=right:
            nd=curr.next
            curr.next=prev
            prev=curr
            curr=nd
            l+=1

        if(prevhd):
            prevhd.next=prev
            
        hd.next=curr
        if(r==1):
            return prev
        return head
        


