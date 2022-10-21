#include <iostream>
#include <stdlib.h>

using namespace std;

#define MAXN ((int)5e3)
int N;
int A[MAXN + 10];

void InputData(){
	cin >> N;
	for (int i=0; i<N; i++){
		cin >> A[i];
	}
}

void simplesort(int s, int e){
	for (int i=s; i < s+2 ; i++){
		for (int j = i+1; j<=e ; j++){
			if (A[i] > A[j]) {
				int tmp = A[i];
				A[i] = A[j];
				A[j] = tmp;
			}
		}
	}
}

int compare(const void * a, const void * b){
	return *(int * )a - *(int * )b;
}

int Solve(void) {
	int sum = 0;
	for (int i = 0; i < N-1 ; i++){
		// qsort(&A[i], N-i, sizeof(int), compare);
		simplesort(i, N-1);
		A[i+1] = A[i] + A[i+1];
		sum += A[i+1];
	}
	return sum;
}


int main(){
	int ans = 0;
	ios_base::sync_with_stdio(false);
	cin.tie(NULL);
	cout.tie(NULL);
	InputData();//입력

	//여기서부터 작성
	ans = Solve();
	
	cout << ans << "\n";
	return 0;
}