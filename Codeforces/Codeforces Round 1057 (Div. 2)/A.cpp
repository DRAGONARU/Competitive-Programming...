#include <iostream>
#include <string>
#include <set>
#include <vector>
using namespace std;
 
 
int main() {
 
	int t, n, a;
	vector<int> ans;
	set<int> numbers;
	cin >> t;
	for (int j = 0; j < t; j++) {
		cin >> n;
		numbers = {};
		for (int i = 0; i < n; i++) {
			cin >> a;
			numbers.insert(a);
		}
		ans.push_back(numbers.size());
	}
	for (int j = 0; j < t; j++) {
		cout << ans[j] << "\n";
	}
	return 0;
}
