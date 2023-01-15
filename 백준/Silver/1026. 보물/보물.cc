#include <iostream>
#include <algorithm>
#include <vector>
 
using namespace std;
 
vector<int> A, B;
 
int main(void) {
    int n, k;
    cin >> n;
 
    for (int i = 0; i < n; i++) { cin >> k; A.push_back(k); }
    for (int i = 0; i < n; i++) { cin >> k; B.push_back(k); }
 
    sort(A.begin(), A.end());
    sort(B.begin(), B.end(), greater<>());
 
    int result = 0;
 
    for (int i = 0; i < n; i++) result += A[i] * B[i];
 
    cout << result << endl;
 
    return 0;
}
