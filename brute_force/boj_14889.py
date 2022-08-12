from itertools import combinations

n = int(input())
player = [i for i in range(n)]

abilities = []
for i in range(n):
    abilities.append(list(map(int, input().split())))

abilities_array = []

player_array= list(combinations(player,n//2))
player_array.sort()

answer = 1e9

for i in range(len(player_array)//2):
    team_a = player_array[i]
    team_b = player_array[(i+1)*-1]

    total = 0

    team_a_total = 0
    team_b_total = 0

    for duo in combinations(range(n//2),2):
        a = duo[0]
        b = duo[1]

        a_a = team_a[a]
        a_b = team_a[b]

        b_a = team_b[a]
        b_b = team_b[b]

        team_a_total += abilities[a_a][a_b] + abilities[a_b][a_a]
        team_b_total += abilities[b_a][b_b] + abilities[b_b][b_a]


    total = abs(team_a_total - team_b_total)
    if total < answer :
        answer = total

print(answer)