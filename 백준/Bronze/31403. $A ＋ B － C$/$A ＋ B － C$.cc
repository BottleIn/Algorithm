#include <iostream>
#include <string>

using namespace std;

int main(void) {
    int a,b,c;
    cin >> a >> b >> c;

    cout << a+b-c<<endl;
    string tmp = to_string(a) + to_string(b);
    cout << stoi(tmp) - c;


    return 0;
}