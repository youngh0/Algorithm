#include <iostream>
#include <vector>

using namespace std;

int arr[101][100001] = {0};

int main()
{

    int n, k;

    cin >> n >> k;

    vector<int> w(n + 1);
    vector<int> v(n + 1);

    for (int i = 1; i <= n; i++)
    {
        cin >> w[i] >> v[i];
    }

    for (int i = 1; i <= n; i++)
    {
        for (int j = 1; j <= k; j++)
        {

            if (w[i] <= j)

            {

                arr[i][j] = max(arr[i - 1][j - w[i]] + v[i], arr[i - 1][j]);
            }
            else
            {
                arr[i][j] = arr[i - 1][j];
            }
        }
    }

    cout << arr[n][k];

    return 0;
}