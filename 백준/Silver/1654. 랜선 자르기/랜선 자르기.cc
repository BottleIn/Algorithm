#include <iostream>
#include <vector>

using namespace std;

int main() {
    int K, N;
    cin >> K >> N;
    
    vector<int> lengths(K);
    int max_length = 0;

    for(int i = 0; i < K; i++) {
        cin >> lengths[i];
        if(lengths[i] > max_length) {
            max_length = lengths[i];
        }
    }

    long long first = 1, last = max_length, result = 0;

    while(first <= last) {
        long long mid = (first + last) / 2;
        long long total = 0;

        for(int i = 0; i < K; i++) {
            total += lengths[i] / mid;
        }

        if(total >= N) {
            result = mid;
            first = mid + 1;
        }
        else {
            last = mid - 1;
        }
    }
    
    cout << result;
    return 0;
}
