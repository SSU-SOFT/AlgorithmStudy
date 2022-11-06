#include <iostream>
#include <cstdlib>

using namespace std;

#define MAXN (25)
int N;
char map[MAXN+10][MAXN+10];
int count[MAXN * MAXN];
int mx[4] = {1, 0,-1, 0};
int my[4] = {0, 1, 0, -1};
int house = 0;
void InputData(){
	cin >> N;
	for (int i=1; i<=N; i++){
		cin >> &map[i][1];
	}
}

void FloodFill(int h, int w){
    if (map[h][w] != '1') return;

    map[h][w] = '2';
    house++;

    for (int i=0; i<4;i++ ){
        FloodFill(h+my[i], w+mx[i]);
    }

}

int Solve(){
    int cnt = 0;
    for(int i=1; i<=N;i++){
        for(int j=1; j<=N; j++){
            if (map[i][j] != '1') continue;
            house = 0;
            FloodFill(i, j);
            count[cnt] = house;
            cnt++;
        }
    }
    return cnt;
}

int compare(const void * a, const void * b){
    return *(int *)a - *(int *)b;
}

int main(){
	ios_base::sync_with_stdio(false);
	cin.tie(NULL);
	cout.tie(NULL);
	InputData();//입력

	//여기서부터 작성
    int result = Solve();
    cout << result << endl;
    qsort(count, result, sizeof(int), compare);
    for(int i=0; i<result ; i++){
        cout << count[i] << endl;
    }


    // for(int i=1; i <=N; i++){
    //     for(int j=1; j<=N ; j++){
    //         cout << visited[i][j]?'1':'0';
    //     }
    //     cout << endl;
    // }

	return 0;
}