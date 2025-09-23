#include <iostream>
using namespace std;
int main()
{
    int a = 0, b = 0, n = 0;
    cin >> a >> b >> n;
    cout << a * n + b * n / 100 <<' ' << b * n % 100;
}
