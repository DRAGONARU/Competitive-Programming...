#include <iostream>
using namespace std;
int main()
{
    int a = 0, b = 0, c = 0, d = 0, e = 0, f = 0;
    cin >> a >> b >> c >> d >> e >> f;
    cout << (d - a) * 3600 + (e - b) * 60 + (f - c);
    return 0;
}
