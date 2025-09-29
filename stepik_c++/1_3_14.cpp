#include <iostream>
using namespace std;
int main()
{
    int a, h, b ;
    cin >> h>>a>>b;
    cout <<  (h - a +(a - b) - 1) / (a - b) + 1;
}
