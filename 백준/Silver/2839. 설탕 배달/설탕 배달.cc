#include <iostream>
#include <string>

using namespace std;

int main(void) {
    int n;
    cin >> n;
    int result = -1;

    for(int i = n / 5; i >= 0; i-- ){
        int remain = n - ( i * 5 );

        if(remain % 3 == 0){
            result = i + (remain / 3);
            break;
        }
    }

    cout << result << '\n';



    return 0;
}