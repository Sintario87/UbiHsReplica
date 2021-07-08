from bg_unit import Unit
import random
import bg_unit_factory
import time


def create_test_battle():
    team0 = bg_unit_factory.create_team_for_tests(team_marker='red')
    team1 = bg_unit_factory.create_team_for_tests(team_marker='blue')
    battle = Battle(team0, team1)
    return battle


class Battle:

    isOver = False
    winner = '_'
    team1 = []
    team2 = []

    team1_next_unit = 0
    team2_next_unit = 0

    turn_team = 0

    def __init__(self, team1_units, team2_units):
        self.team1 = team1_units
        self.team2 = team2_units

    def isTeamLoss(self):
        team1_loss = True
        team2_loss = True
        t1 = self.GetTeamByIndex(0)
        t2 = self.GetTeamByIndex(1)

        for unit in t1:
            if not unit.CheckForDeath():
                team1_loss = False
        for unit in t2:
            if not unit.CheckForDeath():
                team2_loss = False

        if team1_loss and team2_loss:
            self.isOver = True
            self.winner = 'Draw'
        if team1_loss and not team2_loss:
            self.isOver = True
            self.winner = 'Team2'
        if not team1_loss and team2_loss:
            self.isOver = True
            self.winner = 'Team1'


    def isDraw(self):
        draw = True
        if len(self.team1) > 0:
            draw = False
        if len(self.team2) > 0:
            draw = False
        return draw

    def check_team_for_death_units(self, team):
        death_units_count = 0
        for unit in team:
            if unit.death:
                death_units_count += 1
        return death_units_count

    def remove_death_units(self, team):
        death_units = []
        for unit in team:
            if unit.death:
                death_units.append(unit)

        for unit in death_units:
            team.remove(unit)


    def ChooseUnitToAttack(self, teamindex:int): ## 0 team1; 1 team2
        team = self.GetTeamByIndex(teamindex)
        if len(team) == 1:
            return team[0]

        taunt_units = self.getTauntUnitsFromTeam(teamindex)
        if len(taunt_units) > 0:
            team = taunt_units

        if len(team) == 1:
            return team[0]
        else:
            target_unit = team[random.randint(0, len(team)-1)]
            return target_unit

    def GetTeamByIndex(self, team_index):
        team = []
        if team_index == 0:
            team = self.team1
        else:
            team = self.team2
        return  team

    def GetUnitFromTeamByIndex(self,team_index, unit_index):
        team = self.GetTeamByIndex(team_index)
        unit = team[unit_index]
        return unit

    def str_winner(self, team_index):
        if team_index == 0:
            return 'Team1'
        if team_index == 1:
            return 'Team2'

    def PrintTableState(self):
        team1 = ''
        team2 = ''
        for unit in self.GetTeamByIndex(0):
            team1 += unit.GetName() + '(' + str(unit.GetAtk()) + '/' + str(unit.GetHp()) + ') '
            if unit.isTaunt():
                team1 += 'taunt'
        for unit in self.GetTeamByIndex(1):
            team2 += unit.GetName() + '(' + str(unit.GetAtk()) + '/' + str(unit.GetHp()) + ') '
            if unit.isTaunt():
                team2 += 'taunt'
        print('-' * 30)
        print('|  ' + team1 + '  |')
        print('|  ' + team2 + '  |')
        print('-' * 30)

    def preparation(self):
        for unit in self.team1:
            unit.teamindex = 0
            unit.battle = self

        for unit in self.team2:
            unit.teamindex = 1
            unit.battle = self

    def StartBattle(self, first_turn_team=-1, first_turn_unit_index=-1):
        self.preparation()
        print('New battle started')

        self.team1_next_unit = 0
        self.team2_next_unit = 0
        self.turn_team = random.randint(0, 1)

        if first_turn_team != -1:
            self.turn_team = first_turn_team
            if first_turn_unit_index != -1:
                if first_turn_team == 0:
                    self.team1_next_unit = first_turn_unit_index
                else:
                    self.team2_next_unit = first_turn_unit_index


        while not self.isOver:
            self.PrintTableState()

            attacker_unit_index = self.team1_next_unit if self.turn_team == 0 else self.team2_next_unit
            defence_team_index = 1 if self.turn_team == 0 else 0
            defence_unit = self.ChooseUnitToAttack(defence_team_index)
            attacker_unit = self.GetUnitFromTeamByIndex(self.turn_team, attacker_unit_index)

            death_event = attacker_unit.MakeAttack(defence_unit)
            log_line = self.GetUnitFromTeamByIndex(self.turn_team, attacker_unit_index).GetName() + ' атаковал ' \
                       + defence_unit.GetName()
            if death_event > 0:
                self.InvokeEvent(death_event, self.turn_team, attacker_unit_index)
            if defence_unit.invoke_death_event > 0:
                def_team = self.GetTeamByIndex(defence_unit.teamindex)
                index = def_team.index(defence_unit)
                self.InvokeEvent(defence_unit.invoke_death_event, def_team, index)

            self.remove_death_units(self.team1)
            self.remove_death_units(self.team2)





            self.isTeamLoss()

            if self.turn_team == 0:
                self.team1_next_unit += 1
            else:
                self.team2_next_unit += 1

            if self.team1_next_unit >= len(self.GetTeamByIndex(0)):
                self.team1_next_unit = 0

            if self.team2_next_unit >= len(self.GetTeamByIndex(1)):
                self.team2_next_unit = 0

            self.turn_team = 1 if self.turn_team == 0 else 0
            print(log_line)
            self.PrintTableState()
            print('*' * 20)

        print('Winner team is ' + self.winner)
        #time.sleep(1)

    def getTauntUnitsFromTeam(self, team_index):
        units = self.GetTeamByIndex(team_index)
        total = []
        for unit in units:
            if unit.isTaunt():
                total.append(unit)
        return total
    
    def is_unit_attacker(self, team_index):
        if team_index == self.turn_team:
            return True
        else:
            return False


    def InvokeEvent(self, event_index, team_index, unit_index):
        if event_index == 1:
            self.DR_Harvest_golem(team_index, unit_index)


    def summon(self, atk, hp, name, team_index, index, special_event=0, fraction = 0):
        team = self.GetTeamByIndex(team_index)
        if special_event == 0:
            unit = bg_unit_factory.create_custom_unit(atk, hp, name, fraction=fraction)
            team.insert(index, unit)

        if self.is_unit_attacker(team_index):
            if team_index == 0:
                self.team1_next_unit -= 1
            else:
                self.team2_next_unit -= 1


    def DR_Harvest_golem(self, team_index, index:int):
        self.summon(2, 1, 'harvest golem summon', team_index, index, fraction=3)
