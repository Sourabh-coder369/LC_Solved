class Solution {
public:
    bool isPossible(vector<int>& nums,int maxsum,int k){
        int n=nums.size(),tempsum=0,parts=0;
        for(int i=0;i<n;i++){
            if(tempsum+nums[i]>maxsum){
                parts++;
                tempsum=nums[i];
            }
            else{
                tempsum+=nums[i];
            }
        }
        parts++;
        // cout<<parts<<" "<<maxsum<<endl;
        return parts<=k ? true:false;
    }

    int splitArray(vector<int>& nums, int k) {
        int r=1,n=nums.size(),l=0;
        int maxele=*max_element(nums.begin(),nums.end());
        for(int i=0;i<n;i++){
            r+=nums[i];
        }

        l=maxele;
        while(l<r){
            int mid=(l+r)/2;
            bool ans=isPossible(nums,mid,k);
            if(ans){r=mid;}
            else{l=mid+1;}
        }

        return l;

    }
};