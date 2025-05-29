#include <iostream>
#include <string>
#include <algorithm>
#include <queue>
#include <vector>
using namespace std;
int N;
int arr[10003];
string str[10003];
int k = 0;
string tmp;
int main() {
	ios::sync_with_stdio(false); cin.tie(NULL); cout.tie(NULL);
	cin >> N;
	while (N--) {
		cin >> tmp;
		if (tmp == "push") {
			int a;
			cin >> a;
			arr[k++] = a;
		}
		else if (tmp == "top") {
			if (k == 0) {
				cout << -1 << "\n";
				continue;
			}
			cout << arr[k-1] << "\n";
			//cout << k << endl;
		}
		else if (tmp == "size") {
			cout << k <<"\n";
		}
		else if (tmp == "empty") {
			if (k == 0) cout << 1 << "\n";
			else cout << 0 << "\n";
		}
		else if(tmp =="pop"){
			if (k == 0) {
				cout << -1 << "\n";
				continue;
			}
			cout << arr[k - 1] << "\n";
			k--;
		}
	}
	return 0;
}
