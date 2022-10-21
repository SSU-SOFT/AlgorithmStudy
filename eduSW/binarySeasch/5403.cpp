#include <iostream>
#include <cstdlib>

using namespace std;
#define MAXN ((int)1e3)
int N;//연잎수
int A[MAXN+10];//연잎좌표

void InputData(){
	cin >> N;
	for (int i=0; i<N; i++){
		cin >> A[i];
	}
}
int compare(const void *a, const void *b) {
	return *(int *)a - *(int *)b;
}

int SolveN3() {
	int cnt = 0;
	qsort(A, N, sizeof(int), compare);
	for (int a = 0; a < N-2; a++){
		for (int b = a+1 ; b < N-1; b++){
			int first = A[b] - A[a];
			for (int c = b+1; c < N ; c++) {
				int second = A[c] - A[b];
				// if ((first<=second) && (second <= 2*first)) cnt++;
				if (second < first) continue;
				if (second > 2*first) break;
				cnt++;
			}
		}
	}
	return cnt;
}

int bsLower(int s, int e, int d) { //d값보다 크거나 같은 값중에 제일 작은 인덱스
	int result = -1;
	while (s <= e) {
		int m = (s+e) / 2;
		if (A[m] >= d) {
			result = m;
			e = m-1;
		} else {
			s = m+1;
		}
	}	
	return result;
}

int bsUpper(int s, int e, int d) { // d값보다 작거나 같은 값중에 제일 큰 인덱스
	int result = -1;
	while (s <= e) {
		int m = (s+e) / 2;
		if (A[m] <= d) {
			result = m;
			s = m+1;
		} else {
			e = m-1;
		}
	}	
	return result;
}

int Solve() {
	int cnt = 0;
	qsort(A, N, sizeof(int), compare);
	for (int a = 0; a < N-2; a++){
		for (int b = a+1 ; b < N-1; b++){
			int first = A[b] - A[a];
			int low = bsLower(0, N-1, A[b] + first);
			if (low < 0) break;
			int up = bsUpper(0, N-1, A[b] + 2*first);
			cnt += up - low + 1;
		}
	}
	return cnt;
}

int main(){
	ios_base::sync_with_stdio(false);
	cin.tie(NULL);
	cout.tie(NULL);
	int ans = -1;
	InputData();//입력받는 부분

	//여기서부터 작성
    // ans = SolveN3();
	ans = Solve();
	cout << ans << "\n";//출력하는 부분
	return 0;
}