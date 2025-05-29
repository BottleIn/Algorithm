#include <iostream>
#include <algorithm>
#include <vector>
#define FAST cin.tie(NULL); ios::sync_with_stdio(false);

using namespace std;

int main()
{
	int num, sum, count = 0;
	vector<int> coins;
	cin >> num >> sum;

	for(int i = 0; i < num; i++)
	{
		int k;
		cin >> k;
		coins.push_back(k);
	}

	
	for(int i = num-1; i >= 0; i--)
	{
		count += sum / coins[i];
		sum = sum % coins[i];
	}

	cout<<count<<endl;
}