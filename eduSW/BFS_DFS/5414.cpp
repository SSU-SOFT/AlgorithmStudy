#include <iostream>
using namespace std;
#define MAXN (20)
int N, K;//자연수 개수, 만들수
int A[MAXN+10];//자연수 값
string msg[] = {"NO", "YES"};
bool visited[MAXN+10]; // 방문 값
void InputData(){
	cin >> N >> K;
	for (int i=1; i<=N; i++){
		cin >> A[i];
        visited[i] = false;
	}
}

bool DFS(int cur) {
    if (cur == K){
        return true;
    } else if (cur > K){
        return false;
    }
    
    for (int i=1; i <= N; i++){
        if (!visited[A[i]]){
            visited[A[i]] = true;
            if (DFS(cur + A[i]))
                return true;
            visited[A[i]] = false;
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
        ans = DFS(0);

		cout << msg[ans] << "\n";//출력
	}
	return 0;
}