
#include <iostream>
#include <stdio.h>
#include <string>
using namespace std;

int main()
{
	while (1) {
	int a, b, c;
	cin >> a >> b >> c;
	if (a == b &&  b == c && c == 0) break;
	int a1 = a * a;
	int b1 = b * b;
	int c1 = c * c;

	if (a1 + b1 == c1 || b1 + c1 == a1 || c1 + a1 == b1) {
		cout << "right" << "\n";
	}
	else cout << "wrong" << "\n";
	}

}