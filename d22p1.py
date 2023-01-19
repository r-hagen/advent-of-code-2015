import heapq

boss = [int(x.split(':')[1]) for x in open('d22.in').readlines()]
player = [50, 500]

spells = {
    "Magic Missile": 53,
    "Drain": 73,
    "Shield": 113,
    "Poison": 173,
    "Recharge": 229,
}

seen = set()
q = [(0, 'player', player, boss, 0, 0, 0)]

while q:
    mana, turn, player, boss, shield, poison, recharge = heapq.heappop(q)
    arm = 0

    if shield > 0:
        arm = 7
        shield -= 1

    if poison > 0:
        boss = [boss[0]-3, boss[1]]
        poison -= 1

    if recharge > 0:
        player = [player[0], player[1]+101]
        recharge -= 1

    if player[0] <= 0 or boss[0] <= 0:
        if player[0] > 0:
            print(mana)
            assert False
        continue

    key = (mana, turn, tuple(player), tuple(boss), shield, poison, recharge, arm)
    if key in seen:
        continue
    seen.add(key)

    if turn == 'player':
        for spell, cost in spells.items():
            if player[1] >= cost:
                if spell == 'Magic Missile':
                    heapq.heappush(q, (mana+cost, 'boss', (player[0], player[1]-cost), (boss[0]-4, boss[1]), shield, poison, recharge))
                elif spell == 'Drain':
                    heapq.heappush(q, (mana+cost, 'boss', (player[0]+2, player[1]-cost), (boss[0]-2, boss[1]), shield, poison, recharge))
                elif spell == 'Shield':
                    heapq.heappush(q, (mana+cost, 'boss', (player[0], player[1]-cost), (boss[0], boss[1]), 6, poison, recharge))
                elif spell == 'Poison':
                    heapq.heappush(q, (mana+cost, 'boss', (player[0], player[1]-cost), (boss[0], boss[1]), shield, 6, recharge))
                elif spell == 'Recharge':
                    heapq.heappush(q, (mana+cost, 'boss', (player[0], player[1]-cost), (boss[0], boss[1]), shield, poison, 5))
    elif turn == 'boss':
        dmg = max([boss[1] - arm, 1])
        heapq.heappush(q, (mana, 'player', (player[0]-dmg, player[1]), (boss[0], boss[1]), shield, poison, recharge))

