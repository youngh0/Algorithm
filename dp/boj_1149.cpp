// RGB거리

#include <iostream>
#include <algorithm>

using namespace std;

int main()
{
    int arr[1001][3] = {0};

    int n;
    cin >> n;

    for (int i = 1; i <= n; i++)
    {
        int r, g, b;
        cin >> r >> g >> b;
        arr[i][0] = r;
        arr[i][1] = g;
        arr[i][2] = b;
    }

    for (int i = 2; i <= n; i++)
    {
        arr[i][0] = min(arr[i - 1][1], arr[i - 1][2]) + arr[i][0];
        arr[i][1] = min(arr[i - 1][0], arr[i - 1][2]) + arr[i][1];
        arr[i][2] = min(arr[i - 1][0], arr[i - 1][1]) + arr[i][2];
    }
    int ans = min(min(arr[n][0], arr[n][1]), arr[n][2]);
    cout << ans;
    // if (arr[n][0] < arr[n][1] && arr[n][0] < arr[n][2])
    //     cout << arr[n][0];
    // else if (arr[n][1] < arr[n][0] && arr[n][1] < arr[n][2])
    //     cout << arr[n][1];
    // else
    //     cout << arr[n][2];

    return 0;
}