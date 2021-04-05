def snail(snail_map):

    result = []
    while len(snail_map):
        result += snail_map.pop(0)
        snail_map = list(zip(*snail_map))[::-1]

    return result