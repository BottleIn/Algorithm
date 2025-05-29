#include <iostream>
#include <string>
#include <queue>
#include <vector>

using namespace std;

int main(void) {
    int N;
    cin >> N;

    while(N--){
        int A, B;
        cin >> A >> B;

        queue<pair<int, int>> q;
        priority_queue<int> pq;

        for(int i = 0; i < A; i++){
            int priority;
            cin >> priority;
            q.push({priority,i});
            pq.push(priority);
        }
        int print_order = 0;

        while(!q.empty()){
            int currentPriority = q.front().first;
            int currentIndex = q.front().second;
            q.pop();

            if (currentPriority == pq.top()) {
                ++print_order;
                pq.pop();  

                if (currentIndex == B) {
                    cout << print_order << endl;
                    break;
                }
            } else {
                q.push({currentPriority, currentIndex});
            }
        }

    }
    return 0;
}