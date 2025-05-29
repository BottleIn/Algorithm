#include <iostream>
#include <cstring>
#include <algorithm>
using namespace std;


const int IMPOSSIBLE = 1000000000;
int N, W[16][16], dp[16][1 << 16]; // dp[x][방문상태] : x 마을에 있고, 방문 상태일 때 순회 최소 비용


int TSP(int current, int visited) { // dp[x][방문상태] 리턴 ( x 마을에 있고, 방문 상태일 때 순회 최소 비용 )
	
	
	int &ret = dp[current][visited];
	if (ret != -1)  return ret; // 이미 탐색 완료 -> 저장된 값 리턴 (중복 제거 -> 피보나치 수열 생각)
	if (visited == (1 << N) - 1) {// (1<<N) -1 : 1111111 : 모든 마을 방문 상태  
		if (W[current][0] != 0) // 마지막으로 current -> 0 도시간 이동 가능한지 : 순회니까.
			return W[current][0];
		return IMPOSSIBLE; // current -> 0 이동 불가
	}

	ret = IMPOSSIBLE;

	for (int i = 0; i < N; ++i) {
		if (visited & (1 << i) || W[current][i] == 0) // i 마을 방문 완료 (상태로 i번째 마을 판단) or 가는 길 없음
			continue;
		ret = min(ret, TSP(i, visited | (1 << i)) + W[current][i]); // i 마을로 탐색 ㄱㄱ (상태에 i번째 마을 추가)
	}
	return ret;
}


int main() {
	ios_base::sync_with_stdio(false); cout.tie(NULL); cin.tie(NULL);
	cin >> N;


	for (int i = 0; i < N; ++i) {
		for (int j = 0; j < N; ++j)
			cin >> W[i][j];
	}

	memset(dp, -1, sizeof(dp)); // 초기화


	cout << TSP(0, 1) << '\n';


	return 0;
}