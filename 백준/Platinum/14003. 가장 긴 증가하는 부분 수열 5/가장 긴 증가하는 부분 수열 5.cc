#include <iostream>
#include <utility>
#include <queue>
#include <algorithm>
using namespace std;
const int MAX = 1000000;
typedef pair<int, int> pii; // pair < 위치, 값 >

int N;
int num[2 * MAX];
int len[2 * MAX];
int real[2 * MAX];
int Index_Arr[2 * MAX];
vector <int> tmp;
priority_queue<int, vector<int>, greater<int>> pq;
int main() {
	ios_base::sync_with_stdio(false); cout.tie(NULL); cin.tie(NULL);
	while (cin >> N) {
		tmp.clear();
		for (int i = 0; i < N; i++) {
			cin >> num[i];
		}
		
		tmp.push_back(num[0]); // 기저
		Index_Arr[0] = tmp.size();

		for (int i = 1; i < N; i++) {  
			//int bsize = tmp.size();
			if (tmp.back() < num[i]) { // 제일 큰 값인 경우 그냥 뒤에 넣기
				tmp.push_back(num[i]);
				Index_Arr[i] = tmp.size();
			}

			else {  //binary search를 통해 자리 바꿈
				int l = 0;
				int r = tmp.size() - 1;
				int ans = r;
				
				while (l <= r) { 
					int mid = (l + r) / 2;
					if (tmp[mid] >= num[i]) {
						r = mid - 1;
						ans = mid;
					}
					else l = mid + 1;
				}
				tmp[ans] = num[i];
				//cout << ans << endl;
				Index_Arr[i] = ans+1;
			}
			
		}
		cout << tmp.size() << endl;
		
		int bsize = tmp.size();

		for (int i = N-1; i >= 0; i--) {
			//cout << Index_Arr[i] << " AND " << bsize << endl;
			if (bsize == Index_Arr[i]) { 
				pq.push(num[i]);
			bsize--; 
			}
		}
		
		while (!pq.empty()) {
			cout << pq.top() << " ";
			pq.pop();
		}
	}

	return 0;
}