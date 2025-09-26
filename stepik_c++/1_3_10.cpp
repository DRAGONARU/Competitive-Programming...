#include <iostream>
using namespace std;
int main()
{
    int time = 0;
    cin >> time;
    cout << time / 3600 % 24  << ':' << time % 3600 / 60 / 10 << time % 3600 / 60 % 10 << ':' << time % 60 / 10 << time % 60 % 10;
    return 0;
}
