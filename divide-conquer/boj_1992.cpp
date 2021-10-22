#include <iostream>
#include <string>

using namespace std;

int arr[64][64];

void quad_tree(int row, int col, int size)
{

    if (size == 1)
    {
        cout << arr[row][col];
        return;
    }
    int standard = arr[row][col];

    bool pass = true;

    for (int i = row; i < row + size; i++)
    {
        for (int j = col; j < col + size; j++)
        {
            if (standard != arr[i][j])
            {
                pass = false;
                break;
            }
        }
    }
    if (pass)
    {
        cout << standard;
        return;
    }

    cout << '(';
    quad_tree(row, col, size / 2);                       // 왼쪽 위
    quad_tree(row, col + size / 2, size / 2);            // 오른쪽 위
    quad_tree(row + size / 2, col, size / 2);            // 왼쪽 아래
    quad_tree(row + size / 2, col + size / 2, size / 2); // 오른쪽 아래
    cout << ')';
    return;
}

int main()
{

    int n;
    cin >> n;

    string aa[64];

    cout << n << endl;
    for (int i = 0; i < n; i++)
    {
        string s;
        cin >> s;
        for (int j = 0; j < n; j++)
        {
            arr[i][j] = s[j] - '0';
        }
    }

    quad_tree(0, 0, 8);

    return 0;
}
