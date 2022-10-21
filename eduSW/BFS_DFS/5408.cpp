#include <iostream>
#include <deque>
#include <vector>
using namespace std;
#define MAXN ((int)1e3)
int M, N;//상자의 가로, 세로 칸 수
int map[MAXN+10][MAXN+10];//토마토 정보
deque<vector<int>> q;
void InputData(){
	cin >> M >> N;
	for (int i=0; i<N; i++){
		for (int j=0; j<M; j++){
			cin >> map[i][j];
            if (map[i][j] == 1){
                q.push_back({i, j, 0});
            }
		}
	}
}

bool isTomato(){
    for(int i = 0 ; i < N ; i++){
        for (int j = 0 ; j < M ; j++) {
            if (map[i][j] == 0){
                return false;
            }
        }
    }
    return true;
}


int Solve(){
    int max = 0;
    int mx[4] = {1, 0, -1, 0};
    int my[4] = {0, 1, 0, -1};

    while (!q.empty()){
        vector<int> cur = q.front(); 
        q.pop_front();

        if (max < cur[2]){
            max = cur[2];
        }

        // q print
        // for (deque<vector<int>>::iterator iter = q.begin(); iter != q.end(); iter++ ){
        //     vector<int> tmp = *iter;
        //     cout << tmp[0] << " " << tmp[1] << " " << tmp[2] << " | ";
        // }
        // cout << endl;

        for(int i = 0 ; i < 4 ; i++){
            int tx = cur[0] + mx[i];
            int ty = cur[1] + my[i];

            if (tx < 0 || N <= tx || ty < 0 || M <= ty)
                continue;

            if (map[tx][ty] == 0){
                map[tx][ty] = cur[2]+1;
                q.push_back({tx, ty, cur[2]+1});
            } else if (map[tx][ty] > 0 && map[tx][ty] > (cur[2] + 1)){
                map[tx][ty] = cur[2]+1;
                q.push_back({tx, ty, cur[2]+1});
            } 
        }
    }
    return isTomato() ? max : -1;
}

int main(){
	ios_base::sync_with_stdio(false);
	cin.tie(NULL);
	cout.tie(NULL);
	int ans = -1;
	InputData();//입력

	//여기서부터 작성
    ans = Solve();

	cout << ans << "\n";//출력
	return 0;
}