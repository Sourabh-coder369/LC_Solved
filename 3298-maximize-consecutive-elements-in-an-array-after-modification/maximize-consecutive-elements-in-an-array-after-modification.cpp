class Solution {
public:
    int maxSelectedElements(vector<int>& nums) {
        // 1 2 5
        // 1 2 3 5 6
        // each entry in the dp array , i could have with correction and one without
        int n=nums.size();
        sort(nums.begin(),nums.end());
        vector<int> arr;
        map<int,int> freq;
        int maxlen=1;
        for(int i=0;i<n;i++){
            freq[nums[i]]++;
            if(freq[nums[i]]==1){
                arr.push_back(nums[i]);
            }
        }

        n=arr.size();
        vector<vector<int>> dp(n,vector<int>(2,0));
        for(int num:arr){
            cout<<num<<" ";
        }
        cout<<endl;
        dp[0][0]=1;
        dp[0][1]=1;
        if(freq[arr[0]]>1){
            dp[0][1]=2;
        }
        maxlen=max(maxlen,dp[0][1]);
        for(int i=1;i<n;i++){
            if(arr[i]-arr[i-1]>2){
                dp[i][0]=1;
                dp[i][1]=1;
                if(freq[arr[i]]>1){
                    dp[i][1]=2;
                }
            }
            else if(arr[i]-arr[i-1]==1){
                dp[i][1]=dp[i-1][1]+1;
                dp[i][0]=dp[i-1][0]+1;
                if(freq[arr[i]]>1){
                    dp[i][1]=max(dp[i][1],dp[i][0]+1);
                }
            }
            else{
                dp[i][0]=dp[i-1][1]+1;
                dp[i][1]=1;
                if(freq[arr[i]]>1){
                    dp[i][1]=dp[i][0]+1;
                }
            }

            maxlen=max(maxlen,max(dp[i][0],dp[i][1]));
        }

        for(int i=0;i<n;i++){
            cout<<dp[i][0]<<" ";
        }
        // if(maxlen==dp[n-1][0] && freq[arr[n-1]]>1){
        //     maxlen++;
        // }
        return maxlen;
    }
};