#include <iostream>
#include <vector>

using namespace std;

int main()
{
    // string a, b;
    string a = "ABCBDAB";
    string b = "BDCABA";

    // cin >> a >> b;

    int arr[1001][1001] = {0};
    char arr_s[1001][1001];

    for (int i = 1; i <= a.length(); i++)
    {
        for (int j = 1; j <= b.length(); j++)
        {
            if (a[i - 1] != b[j - 1])
            {
                arr[i][j] = max(arr[i - 1][j], arr[i][j - 1]);
                if (max(arr[i - 1][j], arr[i][j - 1]) == arr[i][j - 1])
                {
                    arr_s[i][j] = 'l';
                }
                else
                    arr_s[i][j] = 'u';
            }
            else
            {
                arr[i][j] = arr[i - 1][j - 1] + 1;
                arr_s[i][j] = 'y';
            }
        }
    }

    for (int i = 1; i <= a.length(); i++)
    {
        for (int j = 1; j <= b.length(); j++)
        {
            cout << arr[i][j] << " ";
        }
        cout << '\n';
    }

    vector<int> v;

    int row = a.length();
    int col = b.length();

    while (row > 0 & col > 0)
    {

        if (arr_s[row][col] == 'y')
        {

            v.push_back(row);
            row -= 1;
            col -= 1;
        }
        else if (arr_s[row][col] == 'l')
        {
            col -= 1;
        }
        else
        {
            row -= 1;
        }
    }

    for (int i = v.size() - 1; i >= 0; i--)
    {
        cout << a[v[i] - 1];
        // cout << v[i];
    }
    cout << '\n';

    cout << arr[a.length()][b.length()];

    return 0;
}