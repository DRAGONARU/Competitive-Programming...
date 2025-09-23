#include <iostream>
using namespace std;
int main()
{
    int a = 0, b = 0, c = 0, n = 0, co = 0;
    cin >> n;
    for (int i = 0; i < n; i++) {
        cin >> a >> b >> c;
        if ((a + b + c) >= 2) {
            co++;
        }
    }
    cout << co;
}
