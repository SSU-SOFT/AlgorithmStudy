#include <iostream>
#include <cstring>
#include <cstdio>
#include <vector>
#include <queue>
using namespace std;
int N, M;//장기판 행의 수, 열의 수
int R, C, S, K;//말 행과 열, 졸 행과 열

void InputData(){
	cin >> N >> M;
	cin >> R >> C >> S >> K;
}

int Solve() {
    int map[N+1][M+1] = {};

    map[R][C] = 1;
    map[S][K] = -1;

    // for (int n=1; n <= N ; n++){
    //     for (int m=1; m <= M ; m++){
    //         cout << map[n][m] << " ";
    //     }
    //     cout << endl;
    // }
    // cout << endl;

    queue<vector<int>> q;
    q.push({C, R, 0});
    int tx[8] = {-2, -1, 1, 2, 2, 1, -1, -2};
    int ty[8] = {1, 2, 2, 1, -1, -2, -2, -1};

    while (!q.empty()){
        vector<int> cur = q.front();
        q.pop();

        for(int i = 0 ; i < 8 ; i++){
            int mx = cur[0] + tx[i];
            int my = cur[1] + ty[i];

            if (mx < 1 || M < mx || my < 1 || N < my) {
                continue;
            }

            if (map[my][mx] < 0){
                return cur[2]+1;  // cnt
            } else if (map[my][mx] == 0){
                map[my][mx] = 1;
                q.push({mx, my, cur[2]+1});
            }
        }

        // for (int n=1; n <= N ; n++){
        //     for (int m=1; m <= M ; m++){
        //         cout << map[n][m] << " ";
        //     }
        //     cout << endl;
        // }
        // cout << endl;

    }


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