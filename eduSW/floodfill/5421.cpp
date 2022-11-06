#include <iostream>
using namespace std;
#define MAXN (100)
int N;
char map[MAXN+10][MAXN+10];
int mx[8] = {1, 1, 1, 0, -1, -1, -1, 0};
int my[8] = {1, 0, -1, -1, -1, 0, 1, 1};

void InputData(){
	cin >> N;
	for (int i=1; i<=N; i++){
        cin >> &map[i][1];
	}
}

void FloodFill(int h, int w){
    if (map[h][w] != '1')
        return ;
    
    map[h][w] = '2';

    for(int i=0; i<8; i++){
        FloodFill(h+my[i], w+mx[i]);
    }
}

int Solve(){
    int cnt = 0;

    for(int i=1; i <= N; i++){
        for(int j=1; j <= N ; j++){
            if (map[i][j] != '1')
                continue;
            FloodFill(i, j);
            cnt += 1;
        }
    }
    return cnt;
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