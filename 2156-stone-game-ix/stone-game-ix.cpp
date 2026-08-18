class Solution {
public:
    // type1==type2 , alice wins
    // type2+1=type1
    // alice chose 2, and type2>type1 alice wins , but when type2%3==odd,then
    // 2,4,1
    // 112121,
    // if typex is more alice wants that type to be given to the bob
    bool stoneGameIX(vector<int>& stones) {
        map<int,int> mp;
        int n=stones.size();
        for(int i=0;i<n;i++){
            mp[stones[i]%3]+=1;
        }

        if(mp[0]%2==0){
            return mp[1]>0 && mp[2]>0;
        }
        cout<<mp[3]<<endl;
        return abs(mp[1]-mp[2])>2;
    }
};