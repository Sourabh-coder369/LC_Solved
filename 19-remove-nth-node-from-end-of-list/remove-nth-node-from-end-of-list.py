# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        if(not head):
            return head
        
        # dummy=ListNode(-1,head)
        dummy=head
        cnt=0
        while dummy:
            dummy=dummy.next
            cnt+=1

        cnt1=1
        dummy=head
        prev=None
        print(cnt)
        while cnt1<cnt-n+1:
            prev=dummy
            dummy=dummy.next
            cnt1+=1

        temp=dummy.next
        if(not prev and not temp):
            return None

        if(cnt1==1):
            return head.next
        if(prev):
            prev.next=temp

        return head
