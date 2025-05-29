#include <iostream>
#include <string>
#include <vector>
#include <algorithm>

using namespace std;

int main(void) {
    int input;
    cin >> input;

    vector<pair<int,int>> arr(input);


    for(int i = 0; i < input; i++){
        cin >> arr[i].first >> arr[i].second;
    }

    sort(arr.begin(),arr.end());

     for (const auto& point : arr) {
        cout << point.first << " " << point.second << '\n';
    }

    return 0;
}