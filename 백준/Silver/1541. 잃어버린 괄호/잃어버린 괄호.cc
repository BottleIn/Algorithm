#include <iostream>
#include <string>
#include <algorithm>
#define FAST cin.tie(NULL); ios::sync_with_stdio(false);
using namespace std;
/*
struct meet_time
{
	int start, end;
};

bool cmp(meet_time a, meet_time b)
{
	if(a.end == b.end) return a.start < b.start;
	return a.end < b.end;
}*/

int main()
{
	string str;
	cin >> str;
	int num = 0;
	bool minus = false;
    int result = 0;

	for (int i = 0; i < str.size(); i++) 
	{	
		char c = str[i];
		
		if(c == '+' || c == '-' || c == '\0')
		{
			if(minus == false)
			{
				result += num;
				num = 0;
			}
			else if(minus == true)
			{
				result -=num;
				num = 0;
			}
			if(c == '-') minus = true;
		}
		else {
			num = num * 10 + (c - '0');
		}
	}

	if (minus == false)
    {
        result += num;
    }
    else if (minus == true)
    {
        result -= num;
    }
	cout << result;
}