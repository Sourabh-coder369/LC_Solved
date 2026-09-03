class Solution:
    def avoidFlood(self, rains: List[int]) -> List[int]:
        # for a rain[i] i need to find a rain[0] index that is closest to it
        n=len(rains)
        ans=[-1 for i in range(n)]
        arr=SortedList()
        mp=defaultdict(int)
        for val in rains:
            mp[val]=-1

        for i in range(n):
            if rains[i]==0:
                arr.add(i)
            else:
                if mp[rains[i]]>-1:
                    # print(arr)
                    if len(arr)>0:
                        idx=arr.bisect_left(mp[rains[i]])
                        if(idx>=len(arr)):
                            return []
                        # print(idx,mp[rains[i]])
                        ans[arr[idx]]=rains[i]
                        mp[rains[i]]=i
                        arr.discard(arr[idx])

                    else:
                        return []
                else:
                    mp[rains[i]]=i

        for x in arr:
            ans[x]=1
        
        return ans