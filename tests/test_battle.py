import pytest
from bg_unit import Unit
from bg_battle import Battle, create_test_battle
import bg_unit_factory

def pool_teams(index):
    teams = []
    teams.append(bg_unit_factory.create_custom_team([(1, 1), (1, 1), (1, 1), (1, 1)], 'ones'))
    teams.append(bg_unit_factory.create_custom_team([(2, 2), (2, 2)], 'twos'))
    teams.append(bg_unit_factory.create_custom_team([(1, 2), (1, 2), (1, 2), (1, 2), (1, 2), (1, 2)], 'onetwos'))
    teams.append(bg_unit_factory.create_custom_team([(1, 3), (1, 3), (1, 3), (1, 3), (1, 3), (1, 3)], 'onethrees'))
    return teams[index]


def kill_first_unit(team):
    del(team[0])


def test_team_loss_correct():
    team0 = bg_unit_factory.create_team_for_tests(team_marker='red')
    team1 = bg_unit_factory.create_team_for_tests(team_marker='blue')
    for unit in team0:
        unit.hp = 0
        unit.CheckForDeath()
    battle = Battle(team0, team1)
    battle.isTeamLoss()
    assert battle.winner == 'Team2'


def test_team_loss_check_false():
    battle = create_test_battle()
    battle.isTeamLoss()
    assert battle.winner == '_'


def test_remove_death_units_correct():
    battle = create_test_battle()
    battle.team1[0].hp = 0
    battle.team1[0].CheckForDeath()
    battle.remove_death_units(battle.team1)
    assert len(battle.team1) == 2


def test_four_oneone_vs_two_twotwo():
    team1 = pool_teams(0)
    team2 = pool_teams(1)
    battle = Battle(team1, team2)
    battle.StartBattle()
    assert battle.winner == 'Draw'

def test_three_oneone_vs_two_twotwo():
    team1 = pool_teams(0)
    kill_first_unit(team1)
    team2 = pool_teams(1)
    battle = Battle(team1, team2)
    battle.StartBattle()
    assert battle.winner == 'Team2'


def test_four_oneone_vs_one_twotwo():
    team1 = pool_teams(0)
    team2 = pool_teams(1)
    kill_first_unit(team2)
    battle = Battle(team1, team2)
    battle.StartBattle()
    assert battle.winner == 'Team1'

def test_few_rounds_battle():
    team1 = pool_teams(2)
    team2 = pool_teams(3)
    battle = Battle(team1, team2)
    battle.StartBattle()
    assert battle.winner == 'Team2'
