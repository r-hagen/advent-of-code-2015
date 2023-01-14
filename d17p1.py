LIT = 150

containers = [int(x) for x in open('d17.in')]
containers.sort(reverse=True)

ans = []
SEEN = set()


def dfs(used_containers, available_containers, liters):
    key = tuple(sorted(used_containers))
    if key in SEEN:
        return
    SEEN.add(key)

    if liters == LIT:
        ans.append([containers[x] for x in used_containers])
        return

    if len(available_containers) == 0 or liters > LIT:
        return

    for container in available_containers:
        dfs(used_containers | {container}, available_containers -
            {container}, liters + containers[container])


dfs(set(), set(range(len(containers))), 0)


print(len(ans))
