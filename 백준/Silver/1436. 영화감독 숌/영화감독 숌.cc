#include <iostream>
#include <vector>
#include <string>

using namespace std;

int main(void){

    int result = 665;
    int N;
    cin >> N;

    for(int i = 0; i < N; i++){
        while(1){
            result++;
            string temp = to_string(result);
            if(temp.find("666") != -1) break;
        }
        
    }
    cout << result;
    return 0;
}