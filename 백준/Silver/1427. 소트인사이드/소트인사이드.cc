#include <iostream>
#include <string>
#include <vector>
#include <algorithm>

using namespace std;

int main(void) {
    int input;
    cin >> input;
    
    int a = to_string(input).length();
    
    vector<int> arr(a);
    int i = 0;
    while(input / 10 != 0){
        arr[i] = input % 10;
        input = input / 10; 
        i++;       
    }
    arr[i] = input % 10;
    sort(arr.begin(),arr.end());

    for(int j = a-1; j >=0; j--){
        cout << arr[j];
    }

    return 0;
}