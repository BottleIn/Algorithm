#include <iostream>
#include <string>
#include <algorithm>
using namespace std;

int main()
{
	ios_base::sync_with_stdio(false); cin.tie(0);
	
	int a, b;
	cin >> a;
	int arr[100001];
	for (int i = 0; i < a; i++) {
		int num;
		cin >> num;
		arr[i] = num;
	}
	sort(arr, arr + a);

	cin >> b;
	//int arr[100001];
	for (int i = 0; i < b; i++) {
		int temp;
		cin >> temp;

		int start = 0, end = a - 1;
		int half = end / 2;
		//cout << half << " " << start << " " << end << "\n";
		int ans = 0;

		while (start <= end) {
			if (temp < arr[half]) end = half - 1;
			else if (temp > arr[half]) start = half + 1;
			else if (temp == arr[half]) {
				ans = 1;
				break;
			}
			half = (end + start) / 2;
		}

		cout << ans << "\n";
	}
	return 0;
}