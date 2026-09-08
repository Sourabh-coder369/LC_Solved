class Solution {
public:
    int countGoodRotations(vector<int>& nums) {
        // way simpler method to do this
        int n=nums.size(),ans=0;
        long long totalsum=0,halfsum=0;
        for(int i=0;i<n;i++){
            totalsum+=nums[i];
            if(i<n/2){halfsum+=nums[i];}
        }

        int l=0,r=(n/2),op=0;
        while(r<n){
            halfsum-=nums[l];
            halfsum+=nums[r];
            l++;
            r++;
            if(halfsum>totalsum-halfsum){
                ans++;
            }
            else if(l>0 && halfsum!=totalsum-halfsum){op++;}
        }
        cout<<ans<<" "<<op<<endl;
        return ans+op;


    }
};