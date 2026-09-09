class Solution:
    def countGroups(self, position: list[int], speed: list[int], distance: int) -> int:
        # from last i traverse , and check tht
        # t=(position[i+1]-position[i])//(speedDiff)
        # either speedDiff*(t+1) should be inBetween them or speedDiff*(t)
        n=len(position)
        st=[]
        for i in range(n):
            if st and position[i]-position[st[-1]]<=distance:
                # grps-=1
                st.pop()
            
            # grps+=1
            st.append(i)

        grps=0
        print(st)
        rgrp=len(st)-1
        maxspeed=speed[st[-1]]
        for i in range(len(st)-2,-1,-1):
            if speed[st[i]]<=maxspeed:
                grps+=1
                maxspeed=speed[st[i]]
        
        return grps+1