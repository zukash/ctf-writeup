#include <algorithm>
#include <iostream>
#include <vector>
#define int long long
using namespace std;

int INF = 1e18;
int n;
int L[4123];
int U[4123];
int V[4123];
int D[4123];
vector<int> G[4123];
vector<int> ans;

int dfs(int u, int p, int x) {
  if (D[u] == 1) return -L[u];
  if (ans[u] != INF and L[u] < x) return ans[u];
  vector<int> C;
  for (auto v : G[u]) {
    if (v == p) continue;
    C.push_back(dfs(v, u, x));
  }
  return x + *min_element(C.begin(), C.end());
}

signed main() {
  cin >> n;
  for (int i = 0; i < n; i++) {
    cin >> L[i];
  }

  for (int i = 0; i < n - 1; i++) {
    int u, v;
    cin >> u >> v;
    u--, v--;
    U[i] = u;
    V[i] = v;
    D[u] += 1;
    D[v] += 1;
    G[u].push_back(v);
    G[v].push_back(u);
  }
  ans.assign(n, INF);

  vector<pair<int, int>> LI(n);
  for (int i = 0; i < n; i++) {
    LI[i].first = L[i];
    LI[i].second = i;
  }
  sort(LI.begin(), LI.end());

  for (auto [l, u] : LI) {
    if (D[u] == 1)
      ans[u] = -L[u];
    else
      ans[u] = dfs(u, -1, L[u]) + 1;
  }

  for (int i = 0; i < n; i++) {
    cout << ans[i] << " \n"[i == n - 1];
  }
}
