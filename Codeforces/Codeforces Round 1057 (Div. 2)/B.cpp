#include <iostream>
#include <string>
#include <vector>
using namespace std;
 
int main() {
 
	int t, x, y, z;
	vector<string> ans;
	cin >> t;
	for (int j = 0; j < t; j++) {
		cin >> x >> y >> z;
		if ((x & y) == (x & z) && (x & z) == (y & z)) {
			ans.push_back("YES");
		}
		else {
			ans.push_back("NO");
		}
	}
	for (int j = 0; j < t; j++) {
		cout << ans[j] << "\n";
	}
	return 0;
}
