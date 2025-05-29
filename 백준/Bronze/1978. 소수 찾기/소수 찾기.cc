#include <iostream>
#include <vector>
using namespace std;

int main() {
    const int MAX_NUM = 1000;
    vector<bool> prime(MAX_NUM + 1, true);

    prime[0] = prime[1] = false;

    for (int i = 2; i * i <= MAX_NUM; ++i) {
        if (prime[i]) {
            for (int j = i * i; j <= MAX_NUM; j += i) {
                prime[j] = false;
            }
        }
    }

    int num;
    int sum = 0;
    cin >> num;
    for (int a = 0; a < num; ++a) {
        int k;
        cin >> k;
        if (prime[k]) sum++;
    }
    cout << sum << endl;

    return 0;
}
