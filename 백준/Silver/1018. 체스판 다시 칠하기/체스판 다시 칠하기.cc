#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

const vector<string> pattern1 = {
    "WBWBWBWB",
    "BWBWBWBW",
    "WBWBWBWB",
    "BWBWBWBW",
    "WBWBWBWB",
    "BWBWBWBW",
    "WBWBWBWB",
    "BWBWBWBW"
};

const vector<string> pattern2 = {
    "BWBWBWBW",
    "WBWBWBWB",
    "BWBWBWBW",
    "WBWBWBWB",
    "BWBWBWBW",
    "WBWBWBWB",
    "BWBWBWBW",
    "WBWBWBWB"
};

int calculate_repaints(const vector<string>& board, int start_row, int start_col, const vector<string>& pattern) {
    int repaint_count = 0;
    for (int i = 0; i < 8; ++i) {
        for (int j = 0; j < 8; ++j) {
            if (board[start_row + i][start_col + j] != pattern[i][j]) {
                ++repaint_count;
            }
        }
    }
    return repaint_count;
}

int min_repaints_to_chessboard(const vector<string>& board, int N, int M) {
    int min_repaints = 2147483647;
    
    for (int i = 0; i <= N - 8; ++i) {
        for (int j = 0; j <= M - 8; ++j) {
            int repaints1 = calculate_repaints(board, i, j, pattern1);
            int repaints2 = calculate_repaints(board, i, j, pattern2);
            min_repaints = min(min_repaints, min(repaints1, repaints2));
        }
    }
    
    return min_repaints;
}

int main() {
    int N, M;
    cin >> N >> M;
    vector<string> board(N);
    for (int i = 0; i < N; ++i) {
        cin >> board[i];
    }
    
    int result = min_repaints_to_chessboard(board, N, M);
    cout << result << endl;
    
    return 0;
}
