n,m,k = map(int, input().split())

cur_team_num = min(n//2, m)

while k > 0:
    if n//2 > cur_team_num:
        contest = n - cur_team_num * 2
        k -= contest
        n -= contest
    elif m > cur_team_num:
        contest = m - cur_team_num
        k -= contest
        m -= contest
    else:
        k-=3
        n-=2
        m-=1
        cur_team_num-=1
print(cur_team_num)