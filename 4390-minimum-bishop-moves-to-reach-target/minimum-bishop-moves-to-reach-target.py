class Solution:
    def minBishopMoves(self, source: list[int], target: list[int]) -> int:
        s1=sum(source)
        s2=sum(target)

        if s1%2!=s2%2:
            return -1

        x,y=source[0],source[1]
        for i in range(8):
            x+=1
            y-=1
            if x>8 or y<1:
                break

            if x==target[0] and y==target[1]:
                return 1

        x,y=source[0],source[1]
        for i in range(8):
            x-=1
            y+=1

            if x<1 or y>8:
                break

            if x==target[0] and y==target[1]:
                return 1   

        x,y=source[0],source[1]
        for i in range(8-max(source[0],source[1])):
            x+=1
            y+=1
            if x==target[0] and y==target[1]:
                return 1

        x,y=source[0],source[1]
        for i in range(min(source[0],source[1])-1):
            x-=1
            y-=1
            if x==target[0] and y==target[1]:
                return 1
            
        return 2