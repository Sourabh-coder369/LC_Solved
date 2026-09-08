class dataPoint{
    public:
        int count;
        int op;
        int val;
    
    dataPoint(int count,int op,int val){
        this->count=count;
        this->op=op;
        this->val=val;
    }
};

struct cmp{
    bool operator()(dataPoint& a,dataPoint&b){
        if(a.count==b.count){
            return a.op<b.op;
        }
        return a.count<b.count;
    }
};

class FreqStack {
public:
    priority_queue<dataPoint,vector<dataPoint>,cmp> pq;
    map<int,int> mp1;
    map<int,vector<int>> mp2;
    int op=0;
    FreqStack() {
        // to maps , one to store the count of the given element present in the stack
        // to store the number of operations begin done on that element
        // and a heap which stores the {count,operations,value}
    }
    
    void push(int val) {
        op+=1;
        mp2[val].push_back(op);
        mp1[val]++;
        dataPoint d(mp1[val],op,val);
        pq.push(d);
    }
    
    int pop() {
        // while(!pq.empty()){
        //     if(pq.top().op!=mp2[pq.top().val]){
        //         pq.pop();
        //     }
        //     else{
        //         break;
        //     }
        // }

        int val=pq.top().val;
        mp1[val]--;
        mp2[val].pop_back();
        pq.pop();
        // dataPoint d(mp1[val],mp2[val].back(),val);
        // pq.push(d);

        return val;
    }
};

/**
 * Your FreqStack object will be instantiated and called as such:
 * FreqStack* obj = new FreqStack();
 * obj->push(val);
 * int param_2 = obj->pop();
 */