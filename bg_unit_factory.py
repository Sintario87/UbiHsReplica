from bg_unit import Unit


def create_team_for_tests(team_marker: str = 'solo'):
    return create_custom_team([(2, 2), (1, 3), (2, 2)], team_marker)

def create_custom_unit(atk, hp, name):
    custom_unit = Unit(atk, hp, name)
    return custom_unit


def create_custom_team(units_stats, marker: str = 'solo'):
    """[(2,1), (2,3), (1,1)] making team [2/1, 2/3, 1/1]"""
    team = []
    count = 1
    for item in units_stats:
        team.append(Unit(item[0], item[1], 'CustomUnit' + str(count) + '_' + marker))
        count += 1
    return team
