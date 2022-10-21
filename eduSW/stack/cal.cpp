#include <iostream>
#include <stdio.h>
#include <stack>

using namespace std;

#define MAX (20)
int N;
int M[MAX + 10];
char op[MAX + 10];

void InputData(){
	cin >> N;
	cin >> M[0];
	for(int i=1; i<N; i++){
		cin >> op[i] >> M[i];
	}
}

int main(){
	int ans = 0;
	stack<int> nums;
	ios_base::sync_with_stdio(false);
	cin.tie(NULL);
	cout.tie(NULL);

	InputData();//입력

	//여기서부터 작성
	int d;
	nums.push(M[0]);
	for(int i = 1; i < N ; i++){
		switch(op[i]){
			case '+':
				nums.push(M[i]);
				break;
			case '-':
				nums.push(-M[i]);
				break;
			case '*':
				d = nums.top() * M[i];
				nums.pop();
				nums.push(d);
				break;
			case '/':
				d = nums.top() / M[i];
				nums.pop();
				nums.push(d);
				break;
			default :
				break;
		}
	}
	
	// for(int i = 1; i < N ; i++){
	// 	if (op[i] == '*'){
	// 		int tmp = nums.top();
	// 		nums.pop();
	// 		nums.push(tmp * M[i]);
	// 	} else if (op[i] == '/'){
	// 		int tmp = nums.top();
	// 		nums.pop();
	// 		nums.push((int) (tmp / M[i]));
	// 	} else {
	// 		if (op[i] == '-'){
	// 			M[i] *= -1;
	// 		}
	// 		nums.push(M[i]);
	// 	}
	// }

	while (!nums.empty()){
		int cur = nums.top();
		ans += cur;
		nums.pop();
	}

	cout << ans << "\n";

	return 0;
}
