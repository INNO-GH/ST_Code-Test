#include <stdio.h>
#include <stdlib.h>
#include <iostream>
#include <algorithm>
#include <vector>
using namespace std;

// Global
int N;
vector<string> Mat;
vector<int> Num;

// DFS
void dfs(int i, int j)
{
    // 1. Change to F
    Mat[i][j] = 'F';
    Num[Num.size() - 1]++;

    // 2. Go Next
    if (i != 0 && Mat[i - 1][j] == '1') dfs(i - 1, j);
    if (j != 0 && Mat[i][j - 1] == '1') dfs(i, j - 1);
    if (i != N - 1 && Mat[i + 1][j] == '1') dfs(i + 1, j);
    if (j != N - 1 && Mat[i][j + 1] == '1') dfs(i, j + 1);
}

// Main
int main(int argc, char** argv)
{
    // 1. Input
    cin >> N;
    for (int i = 0; i < N; i++) {
        string MatE;
        cin >> MatE;
        Mat.push_back(MatE);
    }

    // 2. DFS
    for (int i = 0; i < N; i++) {
        for (int j = 0; j < N; j++) {
            if (Mat[i][j] == '1') {
                Num.push_back(0);
                dfs(i, j);
            }
        }
    }

    // 3. Result
    sort(Num.begin(), Num.end());
    cout << Num.size() << endl;
    for (int i = 0; i < Num.size(); i++) cout << Num[i] << endl;
    return 0;
}