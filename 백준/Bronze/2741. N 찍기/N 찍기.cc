
#include <iostream>
#include <stdio.h>
#include <string>
using namespace std;

int main()
{
    int person_Num;
    int sum = 1;
    cin >> person_Num;
    for (int i = 1; i <= person_Num; i++) {
        cout << i << "\n";
    }
   /* int num[10] = {0, };
    for (int a = 0; a < 3; a++) {
        cin >> person_Num;
        sum *= person_Num;
    }
    while (sum > 0) {
        num[sum % 10]++;
        sum /= 10;
   }
    for (int a = 0; a < 10;  a++) {
        cout << num[a] << endl;
    }*/
}