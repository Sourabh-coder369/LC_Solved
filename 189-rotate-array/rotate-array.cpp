class Solution {
public:
    void rotate(vector<int>& nums, int k) {
        // lets see how i solve this question??
        // can i do in 0(1) space???
        int n=nums.size();
        k=k%n;
        vector<int> lastEle;
        // 8-3=5
        for(int i=n-1;i>n-k-1;i--){
            lastEle.push_back(nums[i]);
        }

        int r=n-k-1;
        while(r>-1){
            nums[r+k]=nums[r];
            r--;
        }

        cout<<lastEle.size();
        for(int i=0;i<k;i++){
            nums[i]=lastEle[k-i-1];
        }

        // return nums;
    }
};