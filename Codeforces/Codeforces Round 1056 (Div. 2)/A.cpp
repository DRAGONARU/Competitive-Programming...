#include <iostream>
using namespace std;
int main() {
    int t, n;
    int hg, lg, rc, h;
    cin >> t;
    int ans[500];
    for (int i = 0; i < t; i++) {
        cin >> n;
        hg = n;
        lg = 0;
        rc = 0;
        while (lg != 1 or hg != 1) {
            h = hg;
            rc = rc + hg / 2 + lg / 2;
            hg = hg / 2 + hg % 2;
            lg = h / 2 + lg / 2 + lg % 2;
        }
        ans[i] = rc + 1;
    }
    for (int i = 0; i < t; i++) {
        cout << ans[i] << endl;
    }
    return 0;
}
