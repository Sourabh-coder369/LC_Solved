# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        l1val,l2val=0,0
        exp=1
        while(l1):
            l1val+=(l1.val*exp)
            print(l1.val)
            l1=l1.next
            exp=exp*10
        
        exp=1
        while(l2):
            l2val+=(l2.val*exp)
            l2=l2.next
            exp=exp*10
        
        print(l1val,l2val)
        l3val=str(l1val+l2val)  
        print(l3val)
        head=None
        lstnd=None
        for c in l3val[::-1]:
            t=ListNode(int(c))
            if not head:
                head=t
                lstnd=t
            else:
                lstnd.next=t
                lstnd=t
        
        return head
        


