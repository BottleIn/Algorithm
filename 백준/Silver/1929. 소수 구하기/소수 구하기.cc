#include <iostream>
#include <vector>

using namespace std;

int main(void) {
    int min, max;
    cin >> min >> max;

    vector<int> num(max + 1, 1);  // 인덱스를 0부터 max까지 사용하기 위해 크기를 max + 1로 설정

    // 0과 1은 소수가 아님
    num[0] = num[1] = 0;

    // 에라토스테네스의 체 알고리즘 적용
    for (int i = 2; i * i <= max; i++) {
        if (num[i]) {  // num[i]가 1이면 소수
            for (int j = i; j*i <= max; j++) {
                num[j * i] = 0;  // i의 배수들을 소수가 아니라고 표시
            }
        }
    }
    
    for(int k = min; k <=max; k++){
        if(num[k]) cout<<k<<'\n';
    }
    return 0;
}
