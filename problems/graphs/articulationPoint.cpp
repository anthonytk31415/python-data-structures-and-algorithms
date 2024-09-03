#include <iostream>
#include <vector> 
// #include <algorithm> 

using namespace std; 

int n = 6; // number of nodes
vector<vector<int>> adj(n); // adjacency list of graph
vector<bool> visited;
vector<int> tin, low;
int timer;


void addEdgesToAdj(vector<vector<int>> &edges){
    for (vector<int> edge : edges) {    
        adj[edge[0]].push_back(edge[1]); 
    }
}

void IS_CUTPOINT(int v) {
    cout << "cutpoint: " << v << endl;
}

void dfs(int v, int p = -1) {
    visited[v] = true;
    tin[v] = low[v] = timer++;
    int children=0;
    for (int to : adj[v]) {
        if (to == p) continue;
        if (visited[to]) {
            low[v] = min(low[v], tin[to]);
        } else {
            dfs(to, v);
            low[v] = min(low[v], low[to]);
            if (low[to] >= tin[v] && p!=-1)
                cout << "v: " << v << "parent p: " << p << endl;
                IS_CUTPOINT(v);
            ++children;
        }
    }
    if(p == -1 && children > 1)
        IS_CUTPOINT(v);
}

void find_cutpoints() {
    timer = 0;
    visited.assign(n, false);
    tin.assign(n, -1);
    low.assign(n, -1);
    for (int i = 0; i < n; ++i) {
        if (!visited[i])
            dfs (i);
    }
}


void printAdjList(vector<vector<int>> &adj){
    for (int i = 0; i < adj.size(); i++){
        cout << "i: " << i << "; [";
        for (int x : adj[i]){
            cout << x << ",";
        }
        cout << "]; " << endl;
    }
}

int main() {
    cout << "hello world" << endl;
    vector<vector<int>> edges = {{0,1}, {1,2}, {2,0}, {2, 3}, {3,4 }, {4,5 }, {5,3}}; 
    addEdgesToAdj(edges); 
    // printAdjList(adj);

    find_cutpoints(); 
    // for (auto x : tin){
    //     cout << x << endl;
    // }
    for (auto x : low){
        cout << x << endl;
    }
    return 0;

}