#include <iostream>

using namespace std;

// 2로 안나눠지고, 10으로 나눴을 때 나머지가 1인 경우에만 나눠주고
// 위에 해당 안되면 무조건 -1
// 26번째 줄을 그냥 else로 해서 des가 43일때도 2로 안나눠지니까 바로 10으로 나눠서 4가 되므로 틀렸음

int main()
{
    int src;
    int des;

    cin >> src >> des;

    int answer = 1;

    while (des > src)
    {

        if (des % 2 == 0)
        {
            des /= 2;
        }
        else if (des % 10 == 1)
        {
            des /= 10;
        }
        else
        {
            answer = -1;
            break;
        }
        answer++;

        if (des < src)
        {
            answer = -1;
            break;
        }
    }

    cout << answer;

    return 0;
}