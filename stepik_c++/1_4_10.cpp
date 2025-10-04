#include <iostream>
using namespace std;
int main() {
    int king_row, king_collum, pos_row, pos_collum;
    cin >> king_row >> king_collum >> pos_row >> pos_collum;
    if (abs(king_row - pos_row) == 2 and abs(king_collum - pos_collum) == 1 or abs(king_row - pos_row) == 1 and abs(king_collum - pos_collum) == 2) {
        cout << "YES";
    }
    else {
        cout << "NO";
	}
    return 0;
}
