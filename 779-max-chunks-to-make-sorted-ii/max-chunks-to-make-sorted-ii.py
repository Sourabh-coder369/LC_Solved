class Solution:
    def maxChunksToSorted(self, arr: List[int]) -> int:
        chunk=0
        t=[d for d in arr]
        t.sort()
        mp=defaultdict(list)
        n=len(arr)
        for i in range(n):
            mp[t[i]].append(i)

        print(mp)
        tempmax,tempcnt=-1,1
        for i in range(n):
            if arr[i]==tempmax:
                tempcnt+=1
            
            if arr[i]>tempmax:
                tempmax=arr[i]
                tempcnt=1
            
            if tempmax in mp and i>=mp[tempmax][tempcnt-1]:
                chunk+=1

        return chunk