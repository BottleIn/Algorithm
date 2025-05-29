#include <iostream>
#include <vector>
#include <algorithm>
#include <cmath>

using namespace std;

int main() {
    int n;
    cin >> n;

    if (n == 0) {
        cout << 0 << endl;
        return 0;
    }

    vector<int> opinions(n);
    for (int i = 0; i < n; ++i) {
        cin >> opinions[i];
    }

    // 정렬된 상태에서 30% 절사평균을 계산
    sort(opinions.begin(), opinions.end());

    // 15%를 반올림하여 위, 아래로 제외할 개수 계산
    int exclude = round(n * 0.15);

    // 제외한 나머지 의견의 합을 계산
    int sum = 0;
    for (int i = exclude; i < n - exclude; ++i) {
        sum += opinions[i];
    }

    // 나머지 의견의 개수로 평균을 계산
    int remaining = n - 2 * exclude;
    double trimmed_mean = static_cast<double>(sum) / remaining;

    // 평균을 반올림하여 출력
    cout << round(trimmed_mean) << endl;

    return 0;
}
