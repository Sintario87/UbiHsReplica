class Unit:

    death = False
    name = ''

    teamindex = -1
    battle = None

    baseatk = 0
    basehp = 0

    atk = 0
    hp = 0

    taunt = False
    bubble = False
    reborn = False

    death_event = 0
    invoke_death_event = 0
    self_buff_event = 0   # 1-blockbot 2-junkbot 3-hyena

    fraction = 0
    # 0 - neutral
    # 1 - beast
    # 2 - dragon
    # 3 - mech

    def __init__(self, attack, health, name, taunt=False, bubble=False, reborn=False, fraction=0, death_event=0):
        self.baseatk = attack
        self.atk = attack
        self.basehp = health
        self.hp = health
        self.name = name
        self.taunt = taunt
        self.bubble = bubble
        self.fraction = fraction
        self.reborn = reborn
        self.death_event = death_event
        self.invoke_death_event = 0

    def MakeAttack(self, target_unit):
        target_unit.TakeDamage(self.atk)
        self.TakeDamage(target_unit.atk)
        return self.invoke_death_event


    def TakeDamage(self, dmg):
        if self.bubble:
            self.bubble = False
        else:
            self.hp = self.hp - dmg
            self.CheckForDeath()

    def CheckForDeath(self):
        if self.hp < 1:
            self.death = True
            self.invoke_death_event = self.death_event
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

    def self_buff(self, buff): #(atk,hp) tuple
        self.atk += buff[0]
        self.hp += buff[1]

    def blockbot_self_buff(self):
        self.self_buff((2, 0))

    def junkbot_self_buff(self):
        self.self_buff((2, 2))

    def hyena_self_buff(self):
        self.self_buff((2, 1))

    def invoke_buff_on_death_event(self, death_unit_fraction):
        if self.self_buff_event > 0:
            if death_unit_fraction == 3:
                if self.self_buff_event == 1:
                    self.blockbot_self_buff()
                if self.self_buff_event == 2:
                    self.junkbot_self_buff()
            if death_unit_fraction == 1:
                if self.self_buff_event == 3:
                    self.hyena_self_buff()