#include <iostream>
#include <cstring>
using namespace std;
#define MAXN ((int)1e4)
int N;
int X[MAXN+10];
int Y[MAXN+10];

int map[100+10][100+10];
int mx[4] = {1, 0, -1, 0};
int my[4] = {0, 1, 0, -1};
int SH, SW, EH, EW;
int len;

void InputData(){
	cin >> N;
	for (int i=0 ; i<N ; i++){
		cin >> X[i] >> Y[i];
        map[Y[i]][X[i]] = 1;
	}
}
void FloodFill(int h , int w){
    if (h < SH || h > EH || w < SW || w > EW) return ;
    if (map[h][w] == 1){
        len++;
        return ;
    }
    if (map[h][w] != 0) return ;

    map[h][w] = 2;

    for(int i = 0; i < 4; i++){
        FloodFill(h+my[i], w+mx[i]);
    }

}

int Solve(void){
    SH = SW = 100;
    EH = EW = 0;
    for (int i =0; i<N;i++){
        if (SH > Y[i]) SH = Y[i];
        if (SW > X[i]) SW = X[i];
        if (EH < Y[i]) EH = Y[i];
        if (EW < X[i]) EW = X[i];
    }
    SH--; SW--; EH++; EW++;
    len = 0;
    FloodFill(SH, SW);
    return len;
}

int main(){
	ios_base::sync_with_stdio(false);
	cin.tie(NULL);
	cout.tie(NULL);
	int ans = -1;
	InputData();// 입력받는 부분

	// 여기서부터 작성
    ans = Solve();

	cout << ans << "\n";// 출력하는 부분
	return 0;
}