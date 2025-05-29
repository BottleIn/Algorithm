
#include <iostream>
#include <stdio.h>
using namespace std;

int main()
{
    int person_Num;
    int sum = 0;
    int num[10] = { 0,1,4,9,6,5,6,9,4,1 };
    for (int a = 0; a < 5; a++) {
        cin >> person_Num;
        sum += num[person_Num];
     /*   cout << sum << endl;*/
    }

    cout << sum % 10<< endl;
}