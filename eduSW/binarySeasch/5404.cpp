#include <iostream>
using namespace std;
#define MAXN ((int)1e4)
int N, M;
int A[MAXN+10];
void InputData(){
	cin >> N;
	for (int i=0 ; i<N ; i++){
		cin >> A[i];
	}
	cin >> M;
}
int comp (const void * a, const void * b){
    return *(int *)a - * (int *)b;
}

int isPossible(int m) {
    long long sum = 0;
    for (int i = 0 ; i < N ; i++){
        if (A[i] > m) sum += m;
        else sum += A[i];
        if (sum > M) return false;
    }
    return true;
}

int bsUpper(int s, int e) {
    int result = 0;
    while (s <= e) {
        int m = (s + e) / 2;
        if (isPossible(m)){
            result = m;
            s = m+1;
        } else {
            e = m-1;
        }
        
    }
    return result;
} 

int Solve() {
    int max = 0;
    for (int i = 0 ; i < N ; i++){
        if (max < A[i]) max = A[i];
    }
    
    return bsUpper(0, max);
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