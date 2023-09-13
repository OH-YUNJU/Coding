//Silver II

#include <bits/stdc++.h>
using namespace std;


int N;
map<int,int> pos;
vector<int> cmp;

int point = 0;

int main(){
    ios_base::sync_with_stdio(false);
    cin.tie(NULL); cout.tie(NULL);

    cin >> N;
    int k = 0;

    for(int i = 0; i<N; i++){
        cin >> k;
        pos.insert(make_pair(i,k));
        cmp.push_back(k);
    }

    sort(cmp.begin(), cmp.end());
    cmp.erase(unique(cmp.begin(),cmp.end()),cmp.end());

    for(int i = 0; i<N;i++){
        cout << lower_bound(cmp.begin(),cmp.end(), pos[i]) - cmp.begin()<< " ";
    }

    return 0;
}