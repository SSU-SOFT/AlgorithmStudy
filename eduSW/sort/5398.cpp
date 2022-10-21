#include <iostream>
using namespace std;
#define MAXN ((int)3e4)
int N;
int A[MAXN + 10];

void InputData(){
	cin >> N;
	for (int i=0; i<N; i++){
		cin >> A[i];
	}
}

void OutputData(){
	for (int i=0; i<4; i++){
		cout << A[i] << " ";
	}
	cout << "\n";
}

int main(){
	ios_base::sync_with_stdio(false);
	cin.tie(NULL);
	cout.tie(NULL);
	InputData();//입력 받는 부분

	//여기서부터 작성
    int cnt = 0;
    while (cnt < 4){
        int min = MAXN;
        int minIdx = 0;
        for(int i = cnt ; i < N ; i++){
            if (min > A[i]) {
                min = A[i];
                minIdx = i;
            }
        }
        // cout<< min << ", " << minIdx << endl;

        int tmp = A[cnt];
        A[cnt] = A[minIdx];
        A[minIdx] = tmp;
        cnt++;
    }

	OutputData();//출력 하는 부분
	return 0;
}