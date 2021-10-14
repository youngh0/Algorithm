#include <iostream>

using namespace std;

int **arr;
int blue, white = 0;

void search(int x, int y, int n);

void search(int x, int y, int n)
{
    // int temp = arr[x][y];

    for (int i = x; i < x + n; i++)
    {
        for (int j = y; j < y + n; j++)
        {
            if (arr[x][y] != arr[i][j])
            {
                search(x, y, n / 2);                 // 왼쪽 위
                search(x + n / 2, y, n / 2);         // 오른쪽 위
                search(x, y + n / 2, n / 2);         // 왼쪽 아래
                search(x + n / 2, y + n / 2, n / 2); // 오른쪽 아래
                return;
            }
        }
    }

    if (arr[x][y] == 1)
        blue++;
    else
        white++;
}

int main()
{
    int n;

    cin >> n;

    arr = new int *[n];
    for (int i = 0; i < n; i++)
    {
        arr[i] = new int[n];
    }

    for (int i = 0; i < n; i++)
    {
        for (int j = 0; j < n; j++)
        {
            cin >> arr[i][j];
        }
    }

    // for (int i = 0; i < n; i++)
    // {
    //     for (int j = 0; j < n; j++)
    //     {
    //         cout << arr[i][j];
    //     }
    //     cout << '\n';
    // }

    search(0, 0, n);

    cout << white << endl;
    cout << blue << endl;

    for (int i = 0; i < n; i++)
    {
        delete[] arr[i];
    }

    delete[] arr;

    return 0;
}
