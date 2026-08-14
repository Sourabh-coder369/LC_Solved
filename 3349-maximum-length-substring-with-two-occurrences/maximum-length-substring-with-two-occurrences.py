class Solution:
    def maximumLengthSubstring(self, s: str) -> int:
        # lets do it O(N)
        n=len(s)
        l,r=0,0
        mxlen=0
        mp=defaultdict(int)
        for r in range(n):
            mp[s[r]]+=1

            while mp[s[r]]>2:
                mp[s[l]]-=1
                l+=1
            
            mxlen=max(mxlen,r-l+1)
        
        return mxlen
