#include <iostream>
using namespace std;
int main() {
    int king_row, king_collum, pos_row, pos_collum;
    cin >> king_row >> king_collum >> pos_row >> pos_collum;
    if (abs(king_row - pos_row) ==  abs(king_collum - pos_collum)) {
        cout << "YES";
    }
    else {
        cout << "NO";
	}
    return 0;
}
