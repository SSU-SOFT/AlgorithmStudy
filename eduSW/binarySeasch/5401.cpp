#include <iostream>
using namespace std;
#define MAXN ((int)5e4)
#define MAXT ((int)1e4)
int N;
int A[MAXN+10];
int T;
int B[MAXT+10];

void InputData(){
	cin >> N;
	for(int i=1 ; i<=N ; i++){
		cin >> A[i];
	}
	cin >> T;
	for(int i=0 ; i<T ; i++){
		cin >> B[i];
	}
}
void OutputData(){
	for(int i=0; i<T ; i++){
		cout << B[i] << "\n";
	}
}
int BinarySearch(int s, int e, int d){
    int result = 0;
    while (s <= e) {
        int m = (s + e) / 2;

        if (A[m] == d) return m;
        else if (A[m] < d) s = m+1;
        else e = m - 1; 
    }
    return result;
}

void Solve(){
    for (int i = 0 ; i < T; i++){
        B[i] = BinarySearch(0, N, B[i]);
    }
}

int main(){
	ios_base::sync_with_stdio(false);
	cin.tie(NULL);
	cout.tie(NULL);
	InputData();// 입력받는 부분

	// 여기서부터 작성
    Solve();

	OutputData();// 출력하는 부분
	return 0;
}