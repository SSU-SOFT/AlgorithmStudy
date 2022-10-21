#include <iostream>
#include <vector>
#include <queue>
using namespace std;

#define MAXN (100)
int W, H;//가로, 세로 크기
int sw, sh, ew, eh;//출발 가로세로, 도착 가로세로 좌표
char map[MAXN+10][MAXN+10];//지도정보

void InputData(){
	cin >> W >> H;
	cin >> sw >> sh >> ew >> eh;
	for (int i=1; i<=H; i++){
		cin >> &map[i][1];
	}
}

int Solve() {
    int result = 0;

    int tx[4] = {1, 0, -1, 0};
    int ty[4] = {0, 1, 0, -1};
    
    queue<vector<int>> q;
    q.push({sw, sh, 0});
    
    while (!q.empty()) {
        vector<int> cur = q.front();
        int x = cur[0],y=cur[1],cnt=cur[2];
        // cout << x << ", " << y << ", " << cnt << endl;
        q.pop();

        if (cur[0] == ew && cur[1] == eh){
            result = cnt;
            break;
        }
        
        for(int i = 0 ; i < 4 ; i++){
            int mx = cur[0] + tx[i];
            int my = cur[1] + ty[i];
            if (1 <= mx && mx <= W && 1 <= my && my <= H){
                // cout << mx << ", " << my << ", " << map[my][mx] << endl;
                if (map[my][mx] == '0'){
                    // cout << "clear" << endl;
                    map[my][mx] = '1';
                    q.push({mx, my, cnt+1});
                }
            }
        }
    }
    return result;
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