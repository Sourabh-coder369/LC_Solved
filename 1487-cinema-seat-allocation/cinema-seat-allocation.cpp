class Solution {
public:
    int maxNumberOfFamilies(int n, vector<vector<int>>& reservedSeats) {
        map<int,vector<int>> mp;
        int blocks=0;
        int m=reservedSeats.size();
        for(int i=0;i<m;i++){
            mp[reservedSeats[i][0]].push_back(reservedSeats[i][1]);
        }

        int prevKey=0;
        for(auto& [key,value]:mp){
            blocks+=(key-prevKey-1)*2;
            prevKey=key;
            sort(value.begin(),value.end());
            int prevSeat=1,currSeat=1;
            for(int i=0;i<value.size();i++){
                currSeat=value[i];
                bool picked=false;
                if(currSeat<2 && value.size()-1==i){blocks+=2;}
                else if(currSeat<6 && value.size()-1==i){blocks++;}

                if(currSeat>5 && prevSeat<2){blocks++;}
                else if(currSeat>7 && prevSeat<4){blocks++;picked=true;}

                if(!picked && currSeat>9 && prevSeat<6){blocks++;}
                prevSeat=currSeat;
            }
        }

        blocks+=(n-prevKey)*2;
        return blocks;
    }
};