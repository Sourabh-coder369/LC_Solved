class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        # nested binary loop will solve this
        # if wanted to use 
        def bs(reqpos):
            low=0
            high=m
            print(reqpos)
            while(low<high):
                mid=(low+high)//2
                cnt=bisect_left(nums2,nums1[mid])
                if cnt+mid+1==reqpos:
                    return nums1[mid]
                elif cnt+mid+1<reqpos:
                    low=mid+1
                else:
                    high=mid
                print(low,high,mid)

            if low==high:
                low=0
                high=n
                print(reqpos)
                while(low<high):
                    mid=(low+high)//2
                    cnt=bisect_left(nums1,nums2[mid])
                    if cnt+mid+1==reqpos:
                        return nums2[mid]
                    elif cnt+mid+1<reqpos:
                        low=mid+1
                    else:
                        high=mid
            
            return nums1[0]


        m,n=len(nums1),len(nums2)
        print(m,n)
        if (m+n)%2:
            return bs((m+n)//2+1)
        else:
            val1=bs((m+n)//2)
            val2=bs(((m+n)//2)+1)
            return (val1+val2)/2