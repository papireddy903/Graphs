#include<iostream>
#include<vector>
#include<queue>
#include<unordered_map>
using namespace std;

void bfs(unordered_map<int,vector<int>> &adjList, int n){
    queue<int> q;
    vector<bool> visited(n,false);
    q.push(0);
    visited[0] = true;
    while(!q.empty()){
        int node = q.front();
        q.pop();
        cout << node << " ";

        for (auto it : adjList[node]){
            if (!visited[it]){
                visited[it] = true;
                q.push(it);
            }
        }
    }
}

int main(){
    int n = 5;  
    int m = 6;  

    unordered_map<int, vector<int>> adjList;
    vector<pair<int, int>> edges = {
        {0, 1}, {0, 2}, {1, 3}, {1, 4}, {2, 3}, {3, 4}
    };


    for (auto edge : edges) {
        int u = edge.first;
        int v = edge.second;

        adjList[u].push_back(v);
        adjList[v].push_back(u);
    }

    // Display the adjacency list
    bfs(adjList,n);

    return 0;
}