
"""Tally the results of a football competition."""


def tally(rows):
    """Calculate match statistics and return the formatted table."""
    teams = {}

    for row in rows:
        if not row.strip():
            continue

        team1, team2, result = row.split(";")

        if team1 not in teams:
            teams[team1] = [0, 0, 0, 0, 0]

        if team2 not in teams:
            teams[team2] = [0, 0, 0, 0, 0]

        teams[team1][0] += 1
        teams[team2][0] += 1

        if result == "win":
            teams[team1][1] += 1
            teams[team1][4] += 3
            teams[team2][3] += 1

        elif result == "loss":
            teams[team2][1] += 1
            teams[team2][4] += 3
            teams[team1][3] += 1

        elif result == "draw":
            teams[team1][2] += 1
            teams[team2][2] += 1
            teams[team1][4] += 1
            teams[team2][4] += 1

    sorted_teams = sorted(
        teams.items(),
        key=lambda item: (-item[1][4], item[0])
    )

    table = ["Team                           | MP |  W |  D |  L |  P"]

    for team, stats in sorted_teams:
        table.append(
            f"{team:<31}| {stats[0]:2} | {stats[1]:2} | "
            f"{stats[2]:2} | {stats[3]:2} | {stats[4]:2}"
        )

    return table
