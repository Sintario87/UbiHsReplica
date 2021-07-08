class Unit:

    death = False
    name = ''

    baseatk = 0
    basehp = 0

    atk = 0
    hp = 0

    taunt = False
    bubble = False

    def __init__(self, attack, health, name, taunt=False, bubble=False):
        self.baseatk = attack
        self.atk = attack
        self.basehp = health
        self.hp = health
        self.name = name
        self.taunt = taunt
        self.bubble = bubble

    def MakeAttack(self, target_unit):
        target_unit.TakeDamage(self.atk)
        self.TakeDamage(target_unit.atk)


    def TakeDamage(self, dmg):
        if self.bubble:
            self.bubble = False
        else:
            self.hp = self.hp - dmg
            self.CheckForDeath()

    def CheckForDeath(self):
        if self.hp < 1:
            self.death = True
            return True
        else:
            return False

    def IsDeath(self):
        return self.alive

    def GetName(self):
        return self.name

    def GetAtk(self):
        return self.atk

    def GetHp(self):
        return self.hp

    def isTaunt(self):
        return self.taunt

    def set_taunt(self):
        self.taunt = True

    def set_bubble(self):
        self.bubble = True
