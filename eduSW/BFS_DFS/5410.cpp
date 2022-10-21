#include <iostream>
#include <vector>
#include <deque>
#include <utility>
using namespace std;
#define MAXN (100)
#define INF (1<<30)

int N;//가로, 세로 크기
char map[MAXN+10][MAXN+10];//지도정보
int W[MAXN+10][MAXN+10];//가중치 정보
pair<int, int> path[MAXN+10][MAXN+10];

void InputData(){
	cin >> N;
	for (int i=1; i<=N; i++){
		cin >> &map[i][1];
	}
}

int BFS(pair<int, int> start){
    deque<pair<int, int>> q;
    q.push_back(start);

    int mx[4] = {1, 0, -1, 0};
    int my[4] = {0, 1, 0, -1};

    while (!q.empty()){
        pair<int, int> cur = q.front(); q.pop_front();
        // cout << "cur" << endl;
        // cout << cur.first << ", " << cur.second << endl;
        // cout << "iterator" << endl;

        for (int i = 0 ; i < 4 ; i++){
            int tx = cur.first + mx[i];
            int ty = cur.second + my[i];

            if (tx < 1 || N < tx || ty < 1 || N < ty)
                continue;
            // cout << tx << "," << ty << endl;
            int budget = W[cur.second][cur.first] + (int)map[ty][tx]-'0';

            if (budget < W[ty][tx]){
                // cout << budget << " < " << W[ty][tx] << endl;
                q.push_back({tx, ty});
                W[ty][tx] = budget;
            }
        }
    }
    // for (int i = 1; i <= N; i++){
    //     for (int j = 1; j <= N ; j++){
    //         cout << W[i][j] << " ";
    //     }
    //     cout << endl;
    // }
    return W[N][N];
}

int Solve(){
    //Initial
    for (int i = 1; i <= N; i++){
        for (int j = 1; j <= N ; j++){
            W[i][j] = INF;
            path[i][j] = {0, 0};
        }
    }
    W[1][1] = (int)map[1][1]-'0';

    return BFS({1, 1});
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