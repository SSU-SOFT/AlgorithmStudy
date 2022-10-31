#include <iostream>
#include <string.h>
using namespace std;
#define MAXN (20)
int N, K;//자연수 개수, 만들수
int A[MAXN+10];//자연수 값
bool visited[MAXN+10]; // 방문 값
string msg[] = {"NO", "YES"};

void InputData(){
	cin >> N >> K;
	for (int i=1; i<=N; i++){
		cin >> A[i];
        visited[i] = false;
	}
}

bool DFS(int cur, int goal) {
    if (goal == 0){
        return true;
    } else if (goal < 0){
        return false;
    }
    // cout << cur << ":" << goal << endl;
    for (int i=cur; i <= N; i++){
        if (!visited[i] && (goal - A[i] >= 0)){
            visited[i] = true;
            if (DFS(i, goal-A[i]))
                return true;
            visited[i] = false;
        }
    }
    return false;
}   

int main(){
	ios_base::sync_with_stdio(false);
	cin.tie(NULL);
	cout.tie(NULL);
	int T, ans = -1;
	cin >> T;
	for(int t=1; t<=T; t++){
		InputData();//입력
		//여기서부터 작성
        ans = DFS(1, K);

		cout << msg[ans] << "\n";//출력
	}
	return 0;
}