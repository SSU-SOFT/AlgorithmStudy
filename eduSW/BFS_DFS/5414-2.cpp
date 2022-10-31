#include <iostream>
using namespace std;
#define MAXN (20)
int N, K;//자연수 개수, 만들수
int A[MAXN+10];//자연수 값
int prefixSum[MAXN+10];

string msg[] = {"NO", "YES"};

void InputData(){
	cin >> N >> K;
	for (int i=1; i<=N; i++){
		cin >> A[i];
	}
}

int DFSmulti(int s , int sum){
    if (sum > prefixSum[N] - prefixSum[s-1]) return 0;
    if (sum == 0) return 1;
    if (sum < 0) return 0;

    for (int i = s; i <= N; i++){
        if (DFSmulti(i+1, sum-A[i])) return 1;
    }
    return 0;
}

int DFSbinary(int s, int sum){
    if (sum > prefixSum[N]-prefixSum[s-1]) return 0;
    if (sum == 0) return 1;
    if (sum < 0) return 0;
    if (s > N) return 0;
    if (DFSbinary(s+1, sum-A[s])) return 1;
    if (DFSbinary(s+1, sum)) return 1;
    return 0;
}

int Solve(){
    for (int i = 1 ; i <= N; i++){
        prefixSum[i] = prefixSum[i-1]+A[i];
    }
    // return DFSmulti(1,K);
    return DFSbinary(1, K);
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
        ans = Solve();

		cout << msg[ans] << "\n";//출력
	}
	return 0;
}