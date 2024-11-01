#include <stdio.h>
#include <stdlib.h>
#include <iostream>
#include <algorithm>
#include <vector>
using namespace std;

// Main
int main(int argc, char** argv)
{

    // 1. Input
    int BW, GN, GW, GP;
    vector<vector<int>> GL;
    cin >> BW >> GN;
    for (int i = 0; i < GN; i++) {
        cin >> GW >> GP;
        GL.push_back({ GP, GW });
    }

    // 2. Calculate
    int Answer = 0;
    sort(GL.begin(), GL.end());
    while (1) {
        if (BW > GL[GL.size() - 1][1]) {
            Answer += GL[GL.size() - 1][0] * GL[GL.size() - 1][1];
            BW -= GL[GL.size() - 1][1];
            GL.pop_back();
            if (GL.size() == 0) break;
        }
        else {
            Answer += GL[GL.size() - 1][0] * BW;
            BW -= BW;
            GL.pop_back();
            if (BW == 0) break;
        }
    }

    // 3. Result
    cout << Answer << endl;
    return 0;

}