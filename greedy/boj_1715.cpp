#include <iostream>
#include <queue>

using namespace std;

int main()
{
    priority_queue<int, vector<int>, greater<int> > q;

    int n;
    cin >> n;
    while (n--)
    {
        int card;
        cin >> card;
        q.push(card);
    }
    int answer = 0;
    while (q.size() >= 2)
    {
        int min_1 = q.top();
        q.pop();
        int min_2 = q.top();
        q.pop();
        answer += min_1 + min_2;
        if (q.size() == 0)
        {
            break;
        }
        q.push(min_1 + min_2);
    }
    cout << answer;

    return 0;
}