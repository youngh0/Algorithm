// 1로 만들기

#include <iostream>

using namespace std;

void make1(int n, int *arr)
{

    for (int i = 2; i < n + 1; i++)
    {
        arr[i] = arr[i - 1] + 1;
        if (i % 3 == 0 && arr[i / 3] + 1 < arr[i])
        {
            arr[i] = arr[i / 3] + 1;
        }

        if (i % 2 == 0 && arr[i / 2] + 1 < arr[i])
        {
            arr[i] = arr[i / 2] + 1;
        }
    }
}

int main()
{
    int n;

    cin >> n;

    int *arr = new int[n + 1]();

    make1(n, arr);

    cout << arr[n];

    return 0;
}