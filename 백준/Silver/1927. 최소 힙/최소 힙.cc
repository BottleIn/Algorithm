#include <iostream>
#include <string>
#include <algorithm>
#include <queue>
#include <vector>
#define endl "\n"
using namespace std;

struct node {
	char left;
	char right;
};

vector<node> v(1000);

int main() {
	ios::sync_with_stdio(false); cin.tie(NULL); cout.tie(NULL);
	priority_queue<int, vector<int>, greater<int>> pq;
	int N; cin >> N;
	while (N--) {
		int a;
		cin >> a;

		if (a == 0) {
			if (pq.empty()) cout << 0 << "\n";
			else {
				cout << pq.top() << "\n";
				pq.pop();
			}
		}
		else {
			pq.push(a);
		}
	}
	return 0;
}
