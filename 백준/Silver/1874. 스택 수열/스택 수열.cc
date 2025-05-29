#include <iostream>
#include <string>
#include <stack>
using namespace std;

int main(void) {
    int num, input;
    string op = ""; // 문자열을 빈 문자열로 초기화
    int tmp = 1;
    stack<int> i;

    cin >> num;

    for(int j = 0; j < num; j++){
        cin >> input;
        if(tmp <= input){
            while(tmp <= input){ // tmp가 input보다 작거나 같은 동안
                i.push(tmp);
                op += '+';
                tmp++;
            }
            op += '-';
            i.pop();
        } else {
            if(i.empty() || i.top() != input){
                cout << "NO";
                return 0;
            }
            op += '-';
            i.pop();
        }
    }

    for (int j = 0; j < op.length(); j++)
    {
        cout << op[j] << "\n";
    }

    return 0;
}
