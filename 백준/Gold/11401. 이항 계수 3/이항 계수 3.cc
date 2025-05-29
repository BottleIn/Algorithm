	#include <string>
	#include <algorithm>
	#include <queue>
	#include <vector>
	#include <iostream>
	#define endl "\n"
	#define DIV	1000000007
	
/*
	페르마의 소정리
	A^(P-1) = 1 (mod P)
	P는 소수
	*/

	using namespace std;
	int N, M, K;
	int primeArr[10000];
	//long long DP[MAX][MAX];
	long long a=1, b=1, c=1;


	
	
	long long POW(long long A, long long B) {
		long long answer = 1;
		while (B) {
			if (B % 2) {
				answer = (answer * A) % DIV;
				//cout << A <<"  "<< B << endl;
			}
			A = (A * A) % DIV;
			B /= 2; // A ^ 2로 만들면서 B는 반으로 줄임
		}
		//cout << answer << endl;
		return answer % DIV;
	}
	

	int main() {
		ios::sync_with_stdio(false); cin.tie(NULL); cout.tie(NULL);
		
		long long n, k, ans;
		cin >> n >> k;

		long long A = 1, B = 1;
		for (int i = n; i >= n - k + 1; i--) A = (A * i) % DIV;
		for (int i = 1; i <= k; i++) B = (B * i) % DIV;
		ans = ((A % DIV) * POW(B, DIV - 2)) % DIV;
		
		cout << ans << endl;
		return 0;
	}