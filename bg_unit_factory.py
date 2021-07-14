from bg_unit import Unit

total_list_of_units = []


def create_team_for_tests(team_marker: str = 'solo'):
    return create_custom_team([(2, 2), (1, 3), (2, 2)], team_marker)

def create_custom_unit(atk, hp, name, fraction=0,):
    custom_unit = Unit(atk, hp, name)
    return custom_unit


def create_custom_team(units_stats, marker: str = 'solo'):
    """[(2,1), (2,3), (1,1)] making team [2/1, 2/3, 1/1]"""
    team = []
    count = 1
    for item in units_stats:
        team.append(Unit(item[0], item[1], 'U' + str(count) + '_' + marker))
        count += 1
    return team

def create_unit_by_id(unit_id):
    return total_list_of_units[unit_id]


def preparation_list_of_units():
    total_list_of_units.append(Unit(1,1, 'none'))
    total_list_of_units.append(create_alley_cat()) #1
    total_list_of_units.append(create_dragonspawn_lieutenant()) #2
    total_list_of_units.append(create_hyena()) #3
    total_list_of_units.append(create_micro_machine()) #4
    total_list_of_units.append(create_micro_mummy()) #5
    total_list_of_units.append(create_red_whelp()) #6
    total_list_of_units.append(create_glyph_guardian()) #7
    total_list_of_units.append(create_grand_mother()) #8
    total_list_of_units.append(create_harvest_golem()) #9
    total_list_of_units.append(create_kaboom_bot()) #10
    total_list_of_units.append(create_metaltooth_leaper()) #11
    total_list_of_units.append(create_saurolisk()) #12
    total_list_of_units.append(create_steward_of_time()) #13
    total_list_of_units.append(create_deflect_o_bot()) #14
    total_list_of_units.append(create_hangry_dragon()) #15
    total_list_of_units.append(create_infested_wolf()) #16
    total_list_of_units.append(create_iron_sensei()) #17
    total_list_of_units.append(create_monstrous_macaw()) #18
    total_list_of_units.append(create_rat_pack()) #19
    total_list_of_units.append(create_replication_menace()) #20
    total_list_of_units.append(create_screwjank_clunker()) #21
    total_list_of_units.append(create_twilight_emissary()) #22
    total_list_of_units.append(create_bronze_warden()) #23
    total_list_of_units.append(create_annoy_o_module()) #24
    total_list_of_units.append(create_cave_hydra()) #25
    total_list_of_units.append(create_cobalt_scalebane()) #26
    total_list_of_units.append(create_draconid_enforser()) #27
    total_list_of_units.append(create_herald_of_flame()) #28
    total_list_of_units.append(create_junkbot()) #29
    total_list_of_units.append(create_mechano_egg()) #30
    total_list_of_units.append(create_savannah_highmane()) #31
    total_list_of_units.append(create_security_rover()) #32


def create_alley_cat():
    unit = Unit(1, 1, 'Alley cat', unitid=1)
    unit.star_level = 1
    unit.fraction = 1
    return unit

def create_dragonspawn_lieutenant():
    unit = Unit(2, 3, 'Dragonspawn lieutenant', unitid=2)
    unit.star_level = 1
    unit.fraction = 2
    unit.set_taunt()
    return unit

def create_hyena():
    unit = Unit(2, 2, 'Hyena', unitid=3, sb_event=3)
    unit.star_level = 1
    unit.fraction = 1
    return unit

def create_micro_machine():
    unit = Unit(1, 2, 'Micro machine', unitid=4)
    unit.star_level = 1
    unit.fraction = 3
    return unit

def create_micro_mummy():
    unit = Unit(1, 2, 'Micro mummy', unitid=5)
    unit.star_level = 1
    unit.fraction = 3
    return unit

def create_red_whelp():
    unit = Unit(1, 2, 'Red whelp', unitid=6)
    unit.star_level = 1
    unit.fraction = 2
    return unit

def create_glyph_guardian():
    unit = Unit(2, 4, 'Glyph guardian', unitid=7)
    unit.star_level = 2
    unit.fraction = 2
    return unit

def create_grand_mother():
    unit = Unit(1, 1, 'GrandMother', unitid=8)
    unit.star_level = 2
    unit.fraction = 1
    return unit

def create_harvest_golem():
    unit = Unit(2, 3, 'Harvest golem', unitid=9)
    unit.star_level = 2
    unit.fraction = 3
    return unit

def create_kaboom_bot():
    unit = Unit(2, 2, 'Kaboom bot', unitid=10)
    unit.star_level = 2
    unit.fraction = 3
    return unit

def create_metaltooth_leaper():
    unit = Unit(3, 3, 'Metaltooth leaper', unitid=11)
    unit.star_level = 2
    unit.fraction = 3
    return unit

def create_saurolisk():
    unit = Unit(3, 2, 'Saurolisk', unitid=12)
    unit.star_level = 2
    unit.fraction = 1
    return unit

def create_steward_of_time():
    unit = Unit(3, 3, 'Steward of time', unitid=13)
    unit.star_level = 2
    unit.fraction = 2
    return unit

def create_deflect_o_bot():
    unit = Unit(3, 2, 'Deflect-o-bot', unitid=14)
    unit.star_level = 3
    unit.fraction = 3
    return unit

def create_hangry_dragon():
    unit = Unit(4, 4, 'Hangry dragon', unitid=15)
    unit.star_level = 3
    unit.fraction = 2
    return unit

def create_infested_wolf():
    unit = Unit(3, 3, 'Infested wolf', unitid=16)
    unit.star_level = 3
    unit.fraction = 1
    return unit

def create_iron_sensei():
    unit = Unit(2, 2, 'Iron sensei', unitid=17)
    unit.star_level = 3
    unit.fraction = 3

def create_monstrous_macaw():
    unit = Unit(5, 3, 'Monstrous Macaw', unitid=18)
    unit.star_level = 3
    unit.fraction = 1
    return unit

def create_rat_pack():
    unit = Unit(2, 2, 'Rat pack', unitid=19)
    unit.star_level = 3
    unit.fraction = 1
    return unit

def create_replication_menace():
    unit = Unit(3, 1, 'Replication menace', unitid=20)
    unit.star_level = 3
    unit.fraction = 3
    return unit

def create_screwjank_clunker():
    unit = Unit(2, 5, 'Screwjank clunker', unitid=21)
    unit.star_level = 3
    unit.fraction = 3
    return unit

def create_twilight_emissary():
    unit = Unit(4, 4, 'Twilight emissary', unitid=22)
    unit.star_level = 3
    unit.fraction = 2
    return unit

def create_bronze_warden():
    unit = Unit(2, 1, 'Bronze warden', unitid=23)
    unit.star_level = 3
    unit.fraction = 2
    unit.set_bubble()
    unit.set_reborn()
    return unit

def create_annoy_o_module():
    unit = Unit(2, 4, 'Annoy-o-module', unitid=24)
    unit.star_level = 4
    unit.fraction = 3
    return unit

def create_cave_hydra():
    unit = Unit(2, 4, 'Cave hydra', unitid=25)
    unit.star_level = 4
    unit.fraction = 1
    return unit

def create_cobalt_scalebane():
    unit = Unit(5, 5, 'Cobalt scalebane', unitid=26)
    unit.star_level = 4
    unit.fraction = 2
    return unit

def create_draconid_enforser():
    unit = Unit(3, 6, 'Draconid enforser', unitid=27)
    unit.star_level = 4
    unit.fraction = 2
    return unit

def create_herald_of_flame():
    unit = Unit(6, 6, 'Herald of flame', unitid=28)
    unit.star_level = 4
    unit.fraction = 2
    return unit

def create_junkbot():
    unit = Unit(1, 5, 'Junkbot', unitid=29, sb_event=2)
    unit.star_level = 4
    unit.fraction = 3
    return unit

def create_mechano_egg():
    unit = Unit(0, 8, 'Mechano Egg', unitid=30)
    unit.star_level = 4
    unit.fraction = 3
    return unit

def create_savannah_highmane():
    unit = Unit(6, 6, 'Savannah highmane', unitid=31)
    unit.star_level = 4
    unit.fraction = 1
    return unit

def create_security_rover():
    unit = Unit(2, 6, 'Security rover', unitid=32)
    unit.star_level = 4
    unit.fraction = 3
    return unit


preparation_list_of_units()