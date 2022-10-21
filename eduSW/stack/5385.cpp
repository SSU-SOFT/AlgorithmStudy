#include <iostream>
#include <stack>
#include <vector>

using namespace std;
#define MAXN ((int)1e5)

int N;//빌딩수
int H[MAXN+10];//빌딩높이
int sol[MAXN+10];//각 빌딩에서 보이는 빌딩 번호

void InputData() {
	cin >> N;
	for (int i=1; i<=N; i++){
		cin >> H[i];
	}
}
void OutputData() {
	for (int i=1; i<=N; i++){
		cout << sol[i] << "\n";
	}
}

int main() {
	ios_base::sync_with_stdio(false);
	cin.tie(NULL);
	cout.tie(NULL);

	InputData();//입력받는 부분
    
	//여기서부터 작성
    stack<vector<int>> st;
	st.push({H[0], 0});
	int max = H[0];
    
	for(int i=1 ; i <= N; i++){
		while(!st.empty() && st.top()[0] < H[i]){
			vector<int> cur = st.top();
			st.pop();
			if (cur[0] < H[i]){
				sol[cur[1]] = i;
			}
		}
		st.push({H[i], i});
    }

	while(!st.empty()){
		vector<int> cur = st.top();
		st.pop();
		sol[cur[1]] = 0;
	}

	OutputData();//출력하는 부분
	return 0;
}