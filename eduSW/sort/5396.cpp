#include <iostream>
#include <cstdlib>
#include <algorithm>
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

void OutputData(){
    for (int i=0; i<N; i++){
        cout << A[i] << " ";
    }
    cout << "\n";
}

int compare(const void * a, const void * b) {
    return *(int *)a-*(int *)b;
}

int main(){
    ios_base::sync_with_stdio(false);
	cin.tie(NULL);
	cout.tie(NULL);
    InputData();//입력 받는 부분
    
    //여기서부터 작성
    qsort(A, N, sizeof(int), compare);
    
    OutputData();//출력 하는 부분
    return 0;
}