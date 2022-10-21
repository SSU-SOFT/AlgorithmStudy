#include <iostream>
using namespace std;

#define MAXN ((int)1e4)
int N;//명령개수
int cmd[MAXN + 10];
int a[MAXN + 10];

int stk[MAXN + 10];
int sp;

void push(int d){
 	if (sp < MAXN+10)
		stk[sp++] = d;
	return;
}
void pop() {
 	if (sp > 0)
		stk[--sp] = 0;
	return;
}
int top() {
	return stk[sp-1];
}
bool empty() {
	return sp==0;
}
int size() {
	return sp;
}
void Solve(){
	sp = 0;//초기화
	for (int i=0; i<N; i++){
		switch(cmd[i]){
		case 0://읽고 제거
			if (empty()) {
				cout << "E" << "\n";
			}
			else{
				cout << top() << "\n";
				pop();
			}
			break;
		case 1://저장
			push(a[i]);
			break;
		default://2 : 저장 개수
			cout << size() << "\n";
		}
	}
}
void InputData(){
	cin >> N;
	for (int i=0; i<N; i++){
		cin >> cmd[i];
		if (cmd[i] == 1){
			cin >> a[i];
		}
	}
}
int main(){
	ios_base::sync_with_stdio(false);
	cin.tie(NULL);
	cout.tie(NULL);
	InputData();
	Solve();
	return 0;
}
