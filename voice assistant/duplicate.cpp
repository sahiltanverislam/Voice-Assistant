#include <bits/stdc++.h>
using namespace std;

int main() {
  int size;
  cout<<"size of vector";
  cin>>size;  
  vector<int>ans(size);
  for (int i = 0; i < size; i++)
  {
     cin>>ans[i];
  }

  sort(ans.begin(),ans.end());
   int Min =0,Max =0;
  cout<<"index for min"<<endl;
  cin>>Min;
  cout<<"index for max"<<endl;
  cin>>Max;
  cout<<ans[Min];
  cout<<ans[size-Max];
  
  return 0;
}