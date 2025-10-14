#include <iostream>
#include <vector>
using namespace std;
int main()
{
	int t;
	int x, n;
	vector<int> ans;
	cin >> t;
	for (int i = 0; i < t; i++) {
		cin >> x >> n;
		if (n % 2 == 0) {
			ans.push_back(0);
		}
		else {
			ans.push_back(x);
		}
	}
	for (int i = 0; i < ans.size(); i++) {
		cout << ans[i] << endl;
	}
}
