#include <iostream>
using namespace std;

#define MAX ((int)2e5)

int N;
int A[MAX+10];
int M;
int B[MAX+10];

void InputData(){
	cin >> N;
	for(int i=0 ; i<N ; i++) {
		cin >> A[i];
	}
	cin >> M;
	for(int i=0 ; i<M ; i++) {
		cin >> B[i];
	}
}

void OutputData(){
	for(int i=0 ; i<M ; i++) {
		cout << B[i] << " ";
	}
	cout << "\n";
}

int bsUpper(int s, int e, int d){
    int result = -1;
    while (s <= e) {
        int m = (s + e) / 2;
        if (A[m] <= d) {
            result = m;
            s = m+1;
        } else {
            e = m-1;
        }
    }
    return result;
}

int bsLower(int s, int e, int d){
    int result = -1;
    while (s <= e) {
        int m = (s + e) / 2;
        if (A[m] >= d) {
            result = m;
            e = m-1;
        } else {
            s = m+1;
        }
    }
    return result;
}

int main(void){
	ios_base::sync_with_stdio(false);
	cin.tie(NULL);
	cout.tie(NULL);
	// 입력받는 부분
	InputData();

	// 여기서부터 작성
    for (int i = 0; i < M ; i++) {
        int lower = bsLower(0, N-1, B[i]);
        int upper = bsUpper(0, N-1, B[i]);
        // cout << lower << ", " << upper << endl;
        B[i] = upper-lower+1;
    }

	// 출력하는 부분
	OutputData();
	return 0;
}