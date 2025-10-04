#include <iostream>
using namespace std;
int main() {
    int king_row, king_collum, pos_row, pos_collum;
    cin >> king_row >> king_collum >> pos_row >> pos_collum;
    if (abs(king_row - pos_row) == 1 && abs(king_collum - pos_collum) == 0) {
        cout << "YES";
    }
    else if (abs(king_row - pos_row) == 0 && abs(king_collum - pos_collum) == 1) {
        cout << "YES";
    }
    else if (abs(king_row - pos_row) == 1 && abs(king_collum - pos_collum) == 1) {
        cout << "YES";
    }
    else {
        cout << "NO";
	}
    return 0;
}
