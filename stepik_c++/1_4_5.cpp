#include <iostream>
using namespace std;
int main() {
  // put your code here
  int a, b, c;
  cin>>a>>b>>c;
  if (a == b and b == c){
    cout << 3;
  }
  else if(a == b or a == c or c == b){
      cout << 2;
  }
  else{
      cout<<0;
  }
  return 0;
}
