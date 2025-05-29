
#include <iostream>
#include <stdio.h>
#include <string>
using namespace std;

int main()
{
    int person_Num;
    int sum = 1;
    int num[8] = {0, };
    for (int a = 0; a < 8; a++) {
        cin >> person_Num;
        num[a] = person_Num;
       /* cout << num[a] << endl;*/
    }
    //if (num[0] != 1 || num[0] != 8) {
    //    cout << "mixed" << "\n";
    //    return 0;
    //}

    if (num[0] == 1) {
        for (int b = 1; b < 8; b++) {
            if (num[b] != num[b - 1] + 1) {
                cout << "mixed" << "\n";
                return 0;
            }
        }
        cout<<"ascending" << "\n";
    }
    else if (num[0] == 8) {
        for (int b = 1; b < 8; b++) {
            if (num[b] != num[b - 1] - 1) {
                cout << "mixed" << "\n";
                return 0;
            }
        }
        cout << "descending" << "\n";
    }
    else cout << "mixed" << "\n";

}