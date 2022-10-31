#include <iostream>
using namespace std;
#define MAXN (12)
#define INF (1<<30)
int N;//대회수
int A[MAXN+10][MAXN+10];//[출발][도착]=항공료
int visited[MAXN+10];
int sol;
void InputData(){
	cin >> N;
	for (int i=1; i<=N; i++){
		for (int j=1; j<=N; j++){
			cin >> A[i][j];
		}
	}
}
void DFS(int cur, int cnt, int budget) {
    if (sol <= budget) return;
    if (cnt >= N){
        if (A[cur][1] != 0){
            if ((sol > budget + A[cur][1]))
                sol = budget + A[cur][1];
        }
        return ;
    }

    for (int i = 2; i <=N ; i++){
        if (A[cur][i] != 0 && !visited[i]){
            visited[i] = true;
            DFS(i, cnt+1, budget + A[cur][i]);
            visited[i] = false;
        }
    }

}

int Solve(){
    sol = INF;
    DFS(1, 1, 0); // start city, 
    return sol;
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