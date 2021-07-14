import bg_unit_factory
from bg_battle import Battle

team1 = bg_unit_factory.create_custom_team([(2, 2), (2, 2)], 'Red')
team2 = bg_unit_factory.create_custom_team([(1, 1), (1, 1), (1, 1), (1, 1)], 'Blue')

battle = Battle(team1, team2)
