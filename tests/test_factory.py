import pytest
from bg_unit import Unit
import bg_unit_factory


def test_custom_unit():
    unit = bg_unit_factory.create_custom_unit(2, 1, 'SomeTestUnit')
    assert type(unit) == Unit


def test_custom_team_create_count():
    team = bg_unit_factory.create_team_for_tests()
    assert len(team) == 3


def test_custom_team_create_types():
    team = bg_unit_factory.create_team_for_tests()
    assert type(team[1].atk) == int
    assert type(team[1].hp) == int
    assert type(team[1].name) == str


def test_custom_team_create_alive():
    team = bg_unit_factory.create_team_for_tests()
    assert team[0].death is False


def test_custom_team_create_alive_after_damage():
    team = bg_unit_factory.create_team_for_tests()
    team[0].TakeDamage(1)
    assert team[0].death is False

def test_custom_team_create_unit_death():
    team = bg_unit_factory.create_team_for_tests()
    team[0].TakeDamage(2)
    assert team[0].death is True

