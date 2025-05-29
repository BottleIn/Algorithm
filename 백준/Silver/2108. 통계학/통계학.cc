#include <iostream>
#include <cmath>
#include <algorithm>
#include <vector>

using namespace std;

int main() {
    int total = 0;
    int N;
    cin >> N;
    vector<int> nums(N);
    vector<int> count(8001, 0);  // 절댓값이 4000을 넘지 않기 때문에 범위는 8001

    for (int i = 0; i < N; i++) {
        cin >> nums[i];
        total += nums[i];
        count[4000 + nums[i]]++;
    }

    sort(nums.begin(), nums.end());

    // 산술평균
    cout << static_cast<int>(floor(static_cast<double>(total) / N + 0.5)) << endl;

    // 중앙값
    cout << nums[N / 2] << endl;

    // 최빈값 계산
    int max_freq = 0;
    vector<int> mode_candidates;

    for (int i = 0; i < 8001; i++) {
        if (count[i] > max_freq) {
            max_freq = count[i];
            mode_candidates = {i - 4000};
        } else if (count[i] == max_freq) {
            mode_candidates.push_back(i - 4000);
        }
    }

    int mode;
    if (mode_candidates.size() == 1) {
        mode = mode_candidates[0];
    } else {
        sort(mode_candidates.begin(), mode_candidates.end());
        mode = mode_candidates[1];  // 두 번째로 작은 값
    }

    cout << mode << endl;

    // 범위
    cout << nums.back() - nums.front() << endl;

    return 0;
}
