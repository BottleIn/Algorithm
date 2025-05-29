#include <iostream>
#include <algorithm>
#include <vector>
#define FAST cin.tie(NULL); ios::sync_with_stdio(false);
#define MAX_NUM 9
using namespace std;

int main()
{
	vector<long long> arr = {1,1,1,2,2, };
	int cases,num;
	long long temp;
	cin >> cases;

	for(int i=5; i<=100; i++)
	{
		temp = 0;
		temp = arr[i-1] + arr[i-5];
		arr.push_back(temp);
	}
	while(cases)
	{
		cin >> num;
		cout<<arr[num-1]<<"\n";
		cases--;
	}
	
	return 0;
}


