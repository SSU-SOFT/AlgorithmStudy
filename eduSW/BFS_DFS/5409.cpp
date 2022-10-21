#include <iostream>
#include <queue>
#include <vector>

using namespace std;
#define MAXN (100)
int N, M;//지하철역수, 목적역
int S[MAXN+2][MAXN+2];//[s][e]=시간

// #define INF (int(2e9))
#define INF (1<<30)
int visited[MAXN+2];
int path[MAXN+2];

void InputData(){
	cin >> N >> M;
	for (int s=1; s<=N; s++){
		for (int e=1; e<=N; e++){
			cin >> S[s][e];
		}
	}
}

void PRT(int m) {
    if (m == 0) return;
    PRT(path[m]);
    printf("%d ", m);
}

void OutputData(int ans) {
    printf("%d\n", ans);
    PRT(M);
    printf("\n");
}

int BFS(void){
    //0. 초기화
    for(int i = 1 ; i <= N ; i++){
        visited[i] = INF;
        path[i] = 0;
    }
    queue<int> q;
    //1. 시작위치 큐에 저장
    q.push(1);
    visited[1] = 0;
    path[1] = 0;
    //2. 반복문 (큐가 빌 때 까지)
    while (!q.empty()){
        int cur = q.front(); q.pop();
        for (int e=2; e <= N ; e++){
            int ntime = visited[cur] + S[cur][e];
            if (ntime < visited[e]){
                visited[e] = ntime;
                path[e] = cur;
                q.push(e);
            }
        }
    }
    
    //3. 결과
    return visited[M];
}

int main(){
	ios_base::sync_with_stdio(false);
	cin.tie(NULL);
	cout.tie(NULL);
	InputData();//입력

	//여기서부터 작성
    OutputData(BFS());
	return 0;
}