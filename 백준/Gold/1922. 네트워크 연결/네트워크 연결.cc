#include <string>
#include <algorithm>
#include <queue>
#include <vector>
#include <iostream>
#define endl "\n"
#define MAX 1000000
#define ll long long


/*
DP 버전
*/
using namespace std;
int N, M;
//int primeArr[1000003];
int ans;
int a, b, c;
int arr[100001];
//ll dp[505];
//ll cost[1005];
vector<pair<int,pair<int,int>>> Edge; // 간선 정보 저장
queue <int> q;



int find(int tmp) {
	if (arr[tmp] < 0) return tmp;
	//arr[tmp] - find(arr[tmp]);
	return arr[tmp] = find(arr[tmp]);
}
bool myUnion(int x, int y) {
	int xRoot = find(x);
	int yRoot = find(y);
	if (xRoot == yRoot) return true;
	else return false;
}

void Union(int x, int y) {
	int xRoot = find(x);
	int yRoot = find(y);
	if (xRoot == yRoot) return;
	arr[yRoot] = xRoot;
}


int main() {
	ios::sync_with_stdio(false); cin.tie(NULL); cout.tie(NULL);
	
	cin >> N >> M;
	
	for (int i = 0; i <= N; i++) {
		arr[i] = -1;
	}

	for (int i = 1; i <= M; i++) {
		cin >> a >> b >> c;
		Edge.push_back(make_pair(c, (make_pair(a, b))));
	}

	sort(Edge.begin(), Edge.end());

	for (int i = 0; i < M; i++) {
		//cout << Edge[i].first.first << " and " << Edge[i].first.second << endl;
		if (myUnion(Edge[i].second.first, Edge[i].second.second) == false) {
			Union(Edge[i].second.first, Edge[i].second.second);
			ans = ans + Edge[i].first;
			//cout << ans << endl;
		}
	}
	cout << ans << endl;
	return 0;
}