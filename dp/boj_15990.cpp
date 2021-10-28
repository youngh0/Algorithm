#include <iostream>

using namespace std;

int main()
{
    int t;
    cin >> t;

    long long arr[100001][4] = {0};

    arr[1][1] = 1;
    arr[1][2] = 0;
    arr[1][3] = 0;

    arr[2][1] = 0;
    arr[2][2] = 1;
    arr[2][3] = 0;

    arr[3][1] = 1;
    arr[3][2] = 1;
    arr[3][3] = 1;

    for (int i = 4; i <= 100000; i++)
    {
        // 끝이 1이라 i-1
        arr[i][1] = (arr[i - 1][2] + arr[i - 1][3]) % 1000000009;

        // 끝이 2라 i-2
        arr[i][2] = (arr[i - 2][1] + arr[i - 2][3]) % 1000000009;

        // 끝이 3이라 i-3
        arr[i][3] = (arr[i - 3][1] + arr[i - 3][2]) % 1000000009;
    }

    while (t--)
    {
        int n;
        cin >> n;

        cout << (arr[n][1] + arr[n][2] + arr[n][3]) % 1000000009 << endl;
    }

    return 0;
}