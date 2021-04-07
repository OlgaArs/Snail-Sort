def snail(snail_map):

    result = []
    while len(snail_map):
        result += snail_map.pop(0)
        snail_map = list(zip(*snail_map))[::-1]

    return result

if __name__ == '__main__':
    assert snail([[1,2,3],[4,5,6],[7,8,9]]) == [1,2,3,6,9,8,7,4,5]
    assert snail([[1,2,3],[8,9,4],[7,6,5]]) == [1,2,3,4,5,6,7,8,9]
    assert snail([[1,2,3,1],[4,5,6,4],[7,8,9,7],[7,8,9,7]]) == [1,2,3,1,4,7,7,9,8,7,7,4,5,6,9,8]