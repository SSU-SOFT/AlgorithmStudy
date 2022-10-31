#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;
#define MAXN (10)
#define INF (1<<30)
int N;//빌딩개수(장소개수)
int A[MAXN+10][MAXN+10];//[빌딩][장소]=비용
bool visited[MAXN+10];
int minValue = INF;

void InputData(){
	cin >> N;
	for (int i=1; i<=N; i++){
		for (int j=1; j<=N; j++){
			cin >> A[i][j];
		}
	}
}

void DFS(int b, int p, int sum) {
    //check in
    visited[p] = true;
    // cout << b << "," << p << endl;

    //isGoal?
    if (b == N){
        // cout << "sum : " << sum << endl;
        if (sum < minValue){
            minValue = sum;
        }
    }
    // Iterate
    for (int i = 1; i <= N ; i++){
        int tmp = sum + A[b+1][i];
        if (!visited[i] && tmp < minValue){
            DFS(b+1, i, tmp);
        }
    }
    //check out
    visited[p] = false;
}

int Solve(){
    for (int i = 1 ; i <= N ; i++){
        DFS(1, i, A[1][i]);
    }
    return minValue;
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