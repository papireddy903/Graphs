#include<iostream>
#include<vector>
#include<unordered_map>
using namespace std; 

void display(unordered_map<int,vector<int>> mp){
    for (auto it:mp){
        cout << it.first << " -> ";
        for (auto neighbor : it.second){
            cout << neighbor << " "; 
        }
        cout << endl;
    }
}

int main(){
    unordered_map<int, vector<int>>adjList;
    
    int n, m;
    cout << "Number of vertices: ";
    cin >> n;  
    cout << "Number of edges: ";
    cin >> m;

    cout << "Enter the Edges " << endl;
    for (int i = 0;i<m;i++){
        int u,v;
        cin>>u>>v;

        adjList[u].push_back(v);
        adjList[v].push_back(u);
    }

    display(adjList);
    
}