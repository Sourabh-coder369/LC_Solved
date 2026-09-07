# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return head
        mp={}
        nd=head
        idx=0
        while nd:
            mp[idx]=nd
            nd=nd.next
            idx+=1
        
        l,r=0,idx-1
        prevr=None
        prevl=None
        while abs(l-r)>1:
            ndl=mp[l]
            ndr=mp[r]

            nd1=ndl.next
            ndr.next=nd1
            ndl.next=prevr
            if(prevl):
                prevl.next=ndr

            prevr=ndl
            prevl=ndr

            l+=1
            r-=1
            # print(mp[idx-1])
        
        if l==r:
            mp[l].next=prevr
        
        else:
            ndl=mp[l]
            ndr=mp[r]
            ndl.next=prevr
            ndr.next=ndl
            if(prevl):
                prevl.next=ndr

        return mp[idx-1]

            

