#include <iostream>
using namespace std;
#define MAXN ((int)3e4)
int N;//자료 개수
struct ST{
	int id, score;//아이디, 점수
};
ST A[MAXN + 10];//자료

void InputData(){
	cin >> N;
	for (int i = 0; i < N; i++) {
		cin >> A[i].score;
		A[i].id = i+1;
	}
}

void OutputData() {
	for (int i = 0; i < 3; i++) {
		cout << A[i].id << " ";
	}
	cout << "\n";
}

int main() {
	ios_base::sync_with_stdio(false);
	cin.tie(NULL);
	cout.tie(NULL);
	InputData();//입력
	//작성

    int cnt = 0;
    while (cnt < 3){
        int maxId = N;
        int maxScore = 0;
        int maxIdx = 0;
        for (int i = cnt; i < N ; i++){
            if (A[i].score > maxScore) {
                maxScore = A[i].score;
                maxId = A[i].id;
                maxIdx = i;
            } else if (A[i].score == maxScore && A[i].id < maxId) {
                maxId = A[i].id;
                maxIdx = i;
            }
        }
        ST tmp = A[cnt];
        A[cnt] = A[maxIdx];
        A[maxIdx] = tmp;
        cnt++;
    }


	OutputData();
	return 0;
}