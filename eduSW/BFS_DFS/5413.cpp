#include <iostream>
#include <string>
using namespace std;
int N;//던진횟수
int M;//출력모양

void InputData(){
	cin >> N >> M;
}

// 주사위를 N번 던져서 나올 수 있는 모든 경우의 수
void P1(int N, string str=""){
    if (N <= 0){
        cout << str << endl;
        return ;
    }
    for (int i = 1; i <= 6 ; i++){
        P1(N-1, str + to_string(i)+" ");
    }
}

// 주사위를 N번 던져서 중복이 되는 경우를 제외하고 나올 수 있는 모든 경우
void P2(int N, string str="", int cur=1){
    if (N <= 0){
        cout << str << endl;
        return ;
    }
    for (int i = cur; i <= 6 ; i++){
        P2(N-1, str+to_string(i)+" ", i);
    }
}

bool visited[7] = {false};
// 주사위를 N번 던져서 모두 다른 수가 나올 수 있는 모든 경우
void P3(int N, int cur=0, string str=""){
    if (N <= 0){
        cout << str << endl;
        return ;
    }

    visited[cur] = true; //check in

    for (int i = 1; i <= 6 ; i++){
        if (!visited[i]){
            P3(N-1, i, str+to_string(i)+" ");   
        }
    }
    visited[cur] = false; //check out
}

void Solve(int N, int type){
    switch(type) {
        case 1:
            P1(N);
            break;
        case 2:
            P2(N);
            break;
        case 3:
            P3(N);
            break;
        default:
            break;
    }
}

int main(){
	ios_base::sync_with_stdio(false);
	cin.tie(NULL);
	cout.tie(NULL);
	InputData();//입력

	//여기서부터 작성
    Solve(N, M);
	return 0;
}