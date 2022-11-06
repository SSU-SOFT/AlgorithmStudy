#include <iostream>
#include <cstring>
using namespace std;
#define MAXN (100)
int N;//그림크기(정사각형)
char map[MAXN+10][MAXN+10];
int sol1, sol2;
int visited[MAXN+10][MAXN+10];
int mx[4] = {1, 0, -1, 0};
int my[4] = {0, 1, 0, -1};

void InputData(){
	cin >> N;
	for (int h=1; h<=N; h++){
		cin >> &map[h][1]; }
}

void FloodFill(int h, int w, char color){
    if(map[h][w] != color) return ;
    if(visited[h][w]) return ;

    visited[h][w] = 1;

    for(int i = 0 ; i < 4; i++){
        FloodFill(h+my[i], w+mx[i], color);
    }
}

void Solve(){
    // 1. normal compitetion
    sol1 = 0; sol2 = 0;
    memset(visited, 0, sizeof(visited));
    for(int i=1; i<=N; i++){
        for(int j=1; j<=N; j++){
            if(visited[i][j])
                continue;
            sol1++;
            FloodFill(i, j, map[i][j]);
        }
    }
    
    // 2. red-green compitetion
    for(int i=1; i<=N; i++){
        for(int j=1; j<=N; j++){
            if (map[i][j] == 'G'){
                map[i][j] = 'R';
            }
        }
    }
    memset(visited, 0, sizeof(visited));
    for(int i=1; i<=N; i++){
        for(int j=1; j<=N; j++){
            if(visited[i][j])
                continue;
            sol2++;
            FloodFill(i, j, map[i][j]);
        }
    }
}

int main(){
	ios_base::sync_with_stdio(false);
	cin.tie(NULL);
	cout.tie(NULL);
	InputData();// 입력받는 부분

	// 여기서부터 작성
    Solve();

	cout << sol1 << " " <<  sol2 << "\n";// 출력하는 부분
	return 0;
}