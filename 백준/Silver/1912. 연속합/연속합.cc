#include <iostream>
#include <algorithm>
#include <vector>
#define FAST cin.tie(NULL); ios::sync_with_stdio(false);
#define max(x,y) x > y ? x : y
using namespace std;

int main()
{
	int arr[100100]; 
	int dp[100100];
	int cases,num;
	int temp;
	cin >> cases;

	for(int i=0; i<cases; i++)
	{	
		cin >> temp;
		arr[i] = temp;
	}

		int ret = arr[0];
		dp[0] = arr[0];

	for(int i=1; i<cases; i++)
	{	
		dp[i] = max(dp[i-1]+arr[i], arr[i]);
		ret = max(ret,dp[i]);
	}
	cout<<ret;
	return 0;
}


