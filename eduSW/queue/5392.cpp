#include <iostream>
#include <stack>
#include <deque>
#include <vector>
#include <utility>

using namespace std;

#define MAXN (100)
int N, M;//문서수, 궁금한 문서 번호
int P[MAXN+10];//문서 우선순위
void InputData() {
    cin >> N >> M;
    for (int i=0; i<N; i++){
        cin >> P[i];
    }
}

int main() {
    int ans = -1;
    int T;
    ios_base::sync_with_stdio(false);
	cin.tie(NULL);
	cout.tie(NULL);
    cin >> T;
    for (int t=1; t<=T; t++){
        InputData();//입력받는 부분

        //여기서부터 작성
        ans = 0;
        int max = 0;
        deque<pair<int, int>> q;
        for (int i = 0; i < N ; i++){
            if (max < P[i]){
                max = P[i];
            }
            q.push_back({P[i], i});
        }
        

        while(!q.empty()) {
            pair<int, int> cur = q.front();
            q.pop_front();

            if (cur.first < max){
                q.push_back(cur);
                continue;
            } else {
                ans++;
                max = 0;
                for(auto it = q.begin(); it < q.end(); it++){
                    pair<int, int> ptcur = *it;
                    if(max < ptcur.first){
                        max = ptcur.first;
                    }
                }
            }

            if (cur.second == M){
                break;
            }
        }
        


        cout << ans << "\n";//출력하는 부분
    }
    return 0;
}