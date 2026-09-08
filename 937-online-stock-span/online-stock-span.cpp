class StockSpanner {
public:
    vector<pair<int,int>> min_st;
    int idx=0;
    StockSpanner() {
        
    }
    
    // if i am using stack then
    // best way to solve this is using the minst
    int next(int price) {
        min_st.push_back({price,idx});
        idx+=1;

        int i=min_st.size()-1;
        while(i>-1){
            if(min_st[i].first>price){
                break;
            }
            i--;
        }
        // cout<<i<<endl;
        return idx-i-1;
    }
};

/**
 * Your StockSpanner object will be instantiated and called as such:
 * StockSpanner* obj = new StockSpanner();
 * int param_1 = obj->next(price);
 */