#include<iostream>
#include<vector>
using namespace std;

void display(const vector<vector<int>>& adj) {
    for (int i = 0; i < adj.size(); i++) {
        for (int j = 0; j < adj[i].size(); j++) {
            cout << adj[i][j] << " ";
        }
        cout << endl;
    }
}

int main() {
    int n, m;
    cout << "Number of vertices: ";
    cin >> n;  
    cout << "Number of edges: ";
    cin >> m;

    vector<vector<int>> adj(n+1, vector<int>(n+1, 0));

    cout << "Enter the edges (0-based indexing):" << endl;
    for (int i = 0; i < m; i++) {
        int u, v;
        cin >> u >> v;

        adj[u][v] = 1;
        adj[v][u] = 1;
    }

    display(adj);

    return 0;
}
