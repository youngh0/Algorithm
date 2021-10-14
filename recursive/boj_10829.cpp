// 이진수 변환

#include <iostream>
#include <vector>

using namespace std;

void int_to_binary(unsigned long long int n, vector<unsigned long long int> &arr)
{
    if (n <= 1)
    {
        arr.push_back(n % 2);
        return;
    }
    arr.push_back(n % 2);

    int_to_binary(n / 2, arr);
}

int main()
{
    unsigned long long int n;

    cin >> n;

    vector<unsigned long long int> arr;

    int_to_binary(n, arr);

    for (int i = arr.size() - 1; i >= 0; i--)
    {
        cout << arr[i];
    }

    return 0;
}