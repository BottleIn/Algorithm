#include <iostream>
#include <algorithm>
#include <cstring>
using namespace std;
typedef long long ll;
const ll INF = 123456789123456789;

int N, K, color[222];
ll dp[222][222]; // dp[i][j] : i~j 를 같은색으로 바꿀 때 최소 경우의 수 ( 맨 앞의 색으로 맞춰줬다 생각) 
int main() {ios_base::sync_with_stdio(false); cout.tie(NULL); cin.tie(NULL);
    cin >> N >> K;
    for (int i = 1; i <= N; ++i) cin >> color[i];
    for (int i = 1; i <= N; ++i) {
        for (int j = 1; j <= N; ++j) {
            if (i!=j) dp[i][j] = INF; // i!=j 이면 INF (초기화)
        }
    }
    for (int i = 1; i < N; ++i) { // 전구 2개 묶음 (i ~ i+1) 만들기 (기저)
        dp[i][i + 1] =  color[i] == color[i + 1] ? 0LL : 1LL; // 기저 만들기
    }       
    for (int t = 2; t <= N; ++t) { // 전구 3개 묶음 (i ~ i+2) 부터 N개 묶음까지 (i ~ i+N-1) bottom up
        for (int i = 1; i <= N; ++i) { // i 이상 i + t 이하
            if (i + t > N) break;
            for (int a = 0; a < t; ++a) { // [i, i + a] , [i + a + 1, i + t] 2 그룹 합치기로 생각
                ll temp = dp[i][i + a] + dp[i + a + 1][i + t]; // 두 그룹 비용 합쳐서 받아옴
                if (color[i] != color[i + a + 1]) temp++; // 두 그룹 대표색(맨 앞 색)이 다르면 합쳐주기 (+1)
                dp[i][i + t] = min(dp[i][i + t], temp); // dp값 갱신 (점화식)
            }
        }
    }
    cout << dp[1][N] << '\n';

    return 0;
}