class Solution {
public:
    bool sumGame(string num) {
        int total=0,lefthf=0,n=num.size();
        int leftq=0,rightq=0;
        for(int i=0;i<n;i++){
            if(num[i]!='?'){
                int digit=num[i]-'0';
                total+=digit;
                if(i<n/2){lefthf+=digit;}
            }
        }

        for(int i=0;i<n;i++){
            if(num[i]=='?'){
                if(i<n/2){leftq++;}
                else{rightq++;}
            }
        }

        int righthf=total-lefthf;
        return 2*(righthf-lefthf)==9*(leftq-rightq) ? false:true;
    }
};