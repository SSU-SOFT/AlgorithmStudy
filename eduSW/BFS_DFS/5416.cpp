#include <iostream>
#include <cmath>
using namespace std;
#define MAXN (20)
#define INF (1<<30)
int N;
int sl, sr;
int M;
int seq[MAXN+10];
int sol;
void InputData(){
	cin >> N;
	cin >> sl >> sr;
	cin >> M;
	for (int i=0; i<M; i++){
		cin >> seq[i];
	}
}
void BinaryTree(int idx, int sl, int sr, int mv){
    if (sol <= mv)
        return ;
    
    if (idx >= M){
        sol = mv;
        return ;
    }

    if (seq[idx] <= sr){
        BinaryTree(idx+1, seq[idx], sr, mv + abs(seq[idx] - sl));
    }
    if (sl <= seq[idx]){
        BinaryTree(idx+1, sl, seq[idx], mv + abs(seq[idx] - sr));
    }
}

int Solve(){
    sol = INF;
    BinaryTree(0, sl, sr, 0);
    return sol;
}

int main(){
	ios_base::sync_with_stdio(false);
	cin.tie(NULL);
	cout.tie(NULL);
	int ans = -1;
	InputData();//입력받는 부분

	//여기서부터 작성
    ans = Solve();

	cout << ans << endl;//출력하는 부분
	return 0;
}