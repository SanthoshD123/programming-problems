dict = {
    'whale' : 'whale iS largest animal iN the world',
    'lion' : 'lion iS a brave animal iN savana',
    'tiger' : 'tiger iS a strongest animal'
}

key = list(dict.keys())
value = list(dict.values())
lens = [len(x) for x in value]

max_len = max(lens)
min_len = min(lens)

index_max = lens.index(max_len)
index_min = lens.index(min_len)

print(key[index_min],value[index_min])
