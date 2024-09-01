#include<iostream>
#include<vector>
#include<unordered_map>
using namespace std; 

void display(vector<vector<int>> &adj){
    int n = adj.size();
    for (int i = 0;i<n;i++){
        cout << i << "->";
        for (auto neighbor : adj[i]){
            cout << neighbor << " ";
        }
        cout << endl;
    }
}

int main(){
    int n, m;
    cout << "Number of vertices: ";
    cin >> n;  
    cout << "Number of edges: ";
    cin >> m;
    vector<vector<int>> adj(n+1);    

    cout << "Enter the Edges " << endl;
    for (int i = 0;i<m;i++){
        int u,v;
        cin>>u>>v;

        adj[u].push_back(v);
        adj[v].push_back(u);
    }

    display(adj);
    
}