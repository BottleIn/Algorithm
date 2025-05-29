
#include <iostream>
#include <stdio.h>
#include <string>
using namespace std;

int main()
{
    int inp = 0;
    int height, weight, num;
    cin >> inp;

    for (int i = 0; i < inp; i++) {
        int count = 1;
        cin >> height >> weight >> num;

        int a = num % height ; //0
        int b = num / height ; //1

        if (a > 0) {
            b++;
        }
        else
            a = height;

        cout << a * 100 + b << "\n";
    }

}