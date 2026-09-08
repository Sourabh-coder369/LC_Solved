class Solution {
public:
    vector<int> findClosestElements(vector<int>& arr, int k, int x) {
        sort(arr.begin(),arr.end());
        int i=0;
        while(i<arr.size() && arr[i]<x){
            i++;
        }

        int l=i-1,r=i,n=arr.size(),cnt=0;
        vector<int> res;
        while((l>-1 || r<n) && cnt<k){
            if(l>-1 && r<n){
                int diff1=abs(x-arr[l]);
                int diff2=abs(x-arr[r]);

                if(diff1<=diff2){
                    res.push_back(arr[l]);
                    l--;
                }
                else{
                    res.push_back(arr[r]);
                    r++;
                }
            }
            else if(l==-1){
                res.push_back(arr[r]);
                r++;
            }
            else{
                res.push_back(arr[l]);
                l--;
            }
            cnt++;
        }
        sort(res.begin(),res.end());
        return res;
    }
};