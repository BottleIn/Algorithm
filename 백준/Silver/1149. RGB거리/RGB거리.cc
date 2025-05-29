#include <iostream>
#include <algorithm>
#include <vector>
#define FAST cin.tie(NULL); ios::sync_with_stdio(false);
//#define min(x,y) x < y ? x : y
using namespace std;

int main()
{
	int cases;
	int cost[3];
	cin >> cases;

	int house[1001][3];
	house[0][0] = 0;
	house[0][1] = 0;
	house[0][2] = 0;

	for (int i = 1; i <= cases; i++)
	{
		cin >> cost[0] >> cost[1] >> cost[2];
		house[i][0] = min(house[i-1][1], house[i-1][2]) + cost[0];
		house[i][1] = min(house[i-1][0], house[i-1][2]) + cost[1];
		house[i][2] = min(house[i-1][1], house[i-1][0]) + cost[2];

	}

	cout<<min(house[cases][2],min(house[cases][1],house[cases][0]));
}