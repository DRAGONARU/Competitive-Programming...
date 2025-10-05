#include <iostream>
using namespace std;
int main() {
    int n, m, k;
    cin >> n >> m >> k;
    if ((k % m == 0 or k % n == 0) and k <= n * m) {
        cout << "YES";
    }
    else {
        cout << "NO";
	}
    return 0;
}
