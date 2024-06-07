team = [input().split() for _ in range(3)]

def first_way(team):
    team_name = []
    for i in range(3):
        team_name.append(str(int(team[i][1]) % 100))

    return sorted(team_name)


def second_way(team):
    team_name = []
    solve_p = []
    for i in range(3):
        solve_p.append([int(team[i][0]), team[i][2]])
    sorted_data = sorted(solve_p, key=lambda x: x[0], reverse=True)
    for i in range(3):
        team_name.append(sorted_data[i][1][0])
    return team_name

print(''.join(first_way(team)))
print(''.join(second_way(team)))