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

def test_gettaunt():
    team2 = bg_unit_factory.create_custom_team([(4, 4), (1, 1)], 'Must win')
    team2[0].set_taunt()
    battle = Battle(pool_teams(1), team2)
    tauntunits = battle.getTauntUnitsFromTeam(1)
    assert len(tauntunits) == 1
    assert tauntunits[0].GetAtk() == 4


def test_taunts_second_team_always_win():
    only_team2_win = True

    for fight in range(0, 20):
        team1 = bg_unit_factory.create_custom_team([(4, 4)], 'Must lose')
        team2 = bg_unit_factory.create_custom_team([(4, 4), (1, 1)], 'Must win')
        team2[0].set_taunt()
        battle = Battle(team1, team2)
        battle.StartBattle()
        if battle.winner != 'Team2':
            only_team2_win = False


    assert only_team2_win is True

def test_bubble_second_team_always_win():
    only_team2_win = True

    for fight in range(0, 20):
        team1 = bg_unit_factory.create_custom_team([(3, 3)], 'Must lose')
        team2 = bg_unit_factory.create_custom_team([(3, 3)], 'Must win')
        team2[0].set_bubble()
        battle = Battle(team1, team2)
        battle.StartBattle()
        if battle.winner != 'Team2':
            only_team2_win = False

    assert only_team2_win is True
    assert team2[0].bubble is False

def test_summon_second_team_wins():
    only_team2_win = True

    for fight in range(0, 20):
        team1 = bg_unit_factory.create_custom_team([(2, 2), (2, 2), (2, 2)], 'Must lose')
        team2 = bg_unit_factory.create_custom_team([(2, 2), (2, 2), (2, 2)], 'Must win')
        team2[0].death_event = 1
        battle = Battle(team1, team2)
        battle.StartBattle()
        if battle.winner != 'Team2':
            only_team2_win = False

    assert only_team2_win is True

def test_hyena_buff_draw():
    only_draw = True

    for fight in range(0, 10):
        team1 = bg_unit_factory.create_custom_team([(8, 8)], 'M')
        team2 = bg_unit_factory.create_custom_team([(1, 1), (1, 1), (2, 2)], 'u')
        team2[0].fraction = 1
        team2[0].set_taunt()
        team2[1].fraction = 1
        team2[1].set_taunt()
        team2[2].self_buff_event = 3
        battle = Battle(team1, team2)
        battle.StartBattle()
        if battle.winner != 'Draw':
            only_draw = False

    assert only_draw is True

def test_junkbot_buff_team2_win():
    only_team2_win = True

    for fight in range(0, 10):
        team1 = bg_unit_factory.create_custom_team([(5, 6)], 'M')
        team2 = bg_unit_factory.create_custom_team([(1, 1), (1, 1), (2, 2)], 'u')
        team2[0].fraction = 3
        team2[0].set_taunt()
        team2[1].fraction = 3
        team2[1].set_taunt()
        team2[2].self_buff_event = 2
        battle = Battle(team1, team2)
        battle.StartBattle()
        if battle.winner != 'Team2':
            only_team2_win = False

    assert only_team2_win is True