#include <string>
#include <algorithm>
#include <queue>
#include <vector>
#include <iostream>
#define endl "\n"
using namespace std;
int N, M, a, b;
struct Data {
	int num;
	int order;
};
struct Comp {
	bool operator()(const Data& a, const Data& b) {
		return a.num > b.num;
	}
};
priority_queue<Data, vector<Data> ,Comp> pq;


int main() {
	ios::sync_with_stdio(false); cin.tie(NULL); cout.tie(NULL);
	cin >> N >> M;
	int k = 0;
	for (int i = 0; i < N; i++) {
		int a;
		cin >> a;
		pq.push({ a,i });

		while (pq.top().order < i - M + 1) {
			pq.pop();
		}
		cout << pq.top().num << ' ';
	
	}
	return 0;
}