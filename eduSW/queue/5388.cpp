#include <iostream>
#include <deque>
using namespace std;

#define MAXN (100)
int N;
int sol[MAXN + 10];

void InputData(){
	cin >> N;
}

void OutputData(){
	for (int i=0; i<N; i++){
		cout << sol[i] << "\n";
	}
}

int main(){
	ios_base::sync_with_stdio(false);
	cin.tie(NULL);
	cout.tie(NULL);
	InputData();//입력
	//여기서부터 작성
    deque<int> dq;
    for(int i=1; i <= N; i++){
        dq.push_back(i);
    }
    int idx = 0;

    for (int j = 0; j < N ; j++){
        // 1.
        int back = dq.back();
        for (int i = 0 ; i < back/2 ; i++){
            int front = dq.front();
            dq.pop_front();
            dq.push_back(front);
        }
        // 2
        sol[idx++] = dq.front();
        dq.pop_front();
    }
    sol[idx++] = dq.front();
    dq.pop_front();

	OutputData();//출력
	return 0;
}