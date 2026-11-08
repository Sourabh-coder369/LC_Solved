class Solution:
    def canRemoveAll(self, types: list[int], colors: list[int], groupSize: list[int]) -> bool:
        stk=[]
        n=len(colors)
        for i in range(n):
            tp=[types[i],colors[i],1]
            if stk and stk[-1][0]==types[i] and stk[-1][1]==colors[i]:
                tp[-1]=stk[-1][2]+1

            stk.append(tp)
            if groupSize[types[i]]==stk[-1][2]:
                for _ in range(groupSize[types[i]]):
                    stk.pop()

        if stk:
            return False
        
        return True