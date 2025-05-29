#include <iostream>
#include <string>
#include <vector>

using namespace std;

int main(void) {
    int num;
    cin >> num;

    for(int i = 2; i <= num; i++){
        if (i > num) break;

        while(num % i == 0){
            cout << i << '\n';
            num = num / i;
        }
    }

    return 0;
}