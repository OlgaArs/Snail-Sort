def snail(snail_map):
    if not snail_map: return []

    result = []
    dir = 1
    while True:
        i = j = 0
        if dir == 1:
            for _ in range(len(snail_map[0])):
                result.append(snail_map[i].pop(0))
            else:
                snail_map.pop(0)
            dir = 2
        elif dir == 2:
            j = len(snail_map)
            for i in range(len(snail_map)):
                result.append(snail_map[i][j])
                del snail_map[i][j]
            dir = 3
        elif dir == 3:
            i = len(snail_map[0])-1
            for _ in range(len(snail_map[0]),0 ,-1):
                result.append(snail_map[i].pop(-1))
            else:
                snail_map.pop(-1)
            dir = 4
        elif dir == 4:
            if len(snail_map) == 1:
                result.append(snail_map[0].pop(0))
            else:
                for i in range(len(snail_map)-1,0,-1):
                    result.append(snail_map[i].pop(0))
            dir = 1

        if not snail_map:
            break

    return result