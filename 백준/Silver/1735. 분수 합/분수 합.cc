#include <iostream>
#include <string>
#include <algorithm>
#include <queue>
#include <unordered_map>
#include <vector>
#include <set>
#include <cmath>
#define endl "\n"
using namespace std;
int N,M,a,b;
int r;
int temp;
const int dy[] = { -1, -1, 0, 1, 1, 1, 0, -1 };
const int dx[] = { 0, 1, 1, 1, 0, -1, -1, -1 };


int main() {
	ios::sync_with_stdio(false); cin.tie(NULL); cout.tie(NULL);
	cin >> N >> M >> a >> b;		
	int A = a * M + N * b;
	int B = M * b;
	int ta = A;
	int tb = B;
	//cout << A << B << endl;
	while (B !=0) {
		r = A % B;
		A = B;
		B = r;
	}
	cout << ta / A <<" " << tb / A << endl;
	return 0;
}