#include <iostream>

using namespace std;

int main()
{

    long long s;

    cin >> s;

    int cnt = 0;
    int plusVlaue = 1;
    long long sum = 0;

    while (sum <= s)
    {
        sum += plusVlaue;
        plusVlaue++;
        cnt++;
    }

    if (sum > s)
    {
        cout << cnt - 1 << endl;
    }
    else
    {
        cout << cnt;
    }

    return 0;
}