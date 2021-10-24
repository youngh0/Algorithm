// 피보나치 함수 0과 1 출력 횟수

#include <iostream>
#include <vector>

using namespace std;

int main()
{

    vector<pair<int, int> > v;

    v.push_back(pair<int, int>(1, 0));
    v.push_back(pair<int, int>(0, 1));

    for (int i = 2; i <= 40; i++)
    {
        v.push_back(pair<int, int>(v[i - 1].first + v[i - 2].first, v[i - 1].second + v[i - 2].second));
    }

    int t;
    cin >> t;

    while (t--)
    {
        int n;
        cin >> n;

        cout << v[n].first << " " << v[n].second << endl;
    }
    return 0;
}