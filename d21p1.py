input = open('d21.in').readlines()

boss = {
    "HP": int(input[0].split()[2]),
    "DMG": int(input[1].split()[1]),
    "ARM": int(input[2].split()[1]),
}

player = {
    "HP": 100,
    "DMG": 0,
    "ARM": 0
}

weapons = {
    "Dagger":     (8,  4, 0),
    "Shortsword": (10, 5, 0),
    "Warhammer":  (25, 6, 0),
    "Longsword":  (40, 7, 0),
    "Greataxe":   (74, 8, 0),
}

armors = {
    "None":       (0,   0, 0),
    "Leather":    (13,  0, 1),
    "Chainmail":  (31,  0, 2),
    "Splintmail": (53,  0, 3),
    "Bandedmail": (75,  0, 4),
    "Platemail":  (102, 0, 5),
}

rings = {
    "None":       (0,   0, 0),
    "Damage +1":  (25,  1, 0),
    "Damage +2":  (50,  2, 0),
    "Damage +3":  (100, 3, 0),
    "Defense +1": (20,  0, 1),
    "Defense +2": (40,  0, 2),
    "Defense +3": (80,  0, 3),
}


def battle(player, boss, gold):
    p1 = True

    while player[0] > 0 and boss[0] > 0:
        if p1:
            dmg = max([player[1] - boss[2], 1])
            hp = boss[0] - dmg
            boss = (hp, boss[1], boss[2])
        else:
            dmg = max([boss[1] - player[2], 1])
            hp = player[0] - dmg
            player = (hp, player[1], player[2])
        p1 = not p1

    if player[0] > 0:
        print(gold)
        assert False


equipment = set()
for w in weapons.keys():
    for a in armors.keys():
        for r1 in rings.keys():
            for r2 in rings.keys():
                if r1 != r2:
                    g = weapons[w][0] + armors[a][0] + \
                        rings[r1][0] + rings[r2][0]
                    equipment.add((g, w, a, r1, r2))
equipment = sorted(equipment, key=lambda t: t[0])

for g, w, a, r1, r2 in equipment:
    # print(g, w, a, r1, r2)
    hp, dmg, arm = tuple(player.values())
    dmg += weapons[w][1] + armors[a][1] + rings[r1][1] + rings[r2][1]
    arm += weapons[w][2] + armors[a][2] + rings[r1][2] + rings[r2][2]
    battle((hp, dmg, arm), tuple(boss.values()), g)
