#include <iostream>
#include <string>
#include <algorithm>
using namespace std;

int main()
{
    int temp = 0, max = 1;
    int num[40][2] = { {1, 0}, {0, 1}, };

    int input_num, test;
    cin >> input_num;

    for (int i = 0; i < input_num; i++) {
        cin >> test;
        if (test > max) {
            for (int j = max + 1; j <= test; j++) {
                num[j][0] = num[j - 1][0] + num[j - 2][0];
                num[j][1] = num[j - 1][1] + num[j - 2][1];
            }
            max = test;
        }
        cout << num[test][0] << " " << num[test][1] << endl;
    }
    return 0;
}
