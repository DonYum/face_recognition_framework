import sys
import random


if len(sys.argv) != 5:
    raise Exception("Please refer to argument list")

list_file = sys.argv[1]
meta_file = sys.argv[2]
num_split = int(sys.argv[3])
out_prefix = sys.argv[4]


d = dict()

with open(list_file) as f:
    list_lines = f.readlines()

with open(meta_file) as f:
    meta_lines = f.readlines()[1:]

assert len(list_lines) == len(meta_lines)

for l, m in zip(list_lines, meta_lines):
    if m in d:
        d[m].append(l)
    else:
        d[m] = [l]

keys = d.keys()
random.shuffle(keys)

n = len(keys)
sub_n = (n-1) // num_split + 1

i = 0
for beg in range(0, n, sub_n):
    end = min(n, beg+sub_n)
    c = 0
    this_list = []
    this_meta = []
    print(f'generating split {i} ({beg}:{end})...')
    for k in keys[beg:end]:
        this_list.extend(d[k])
        this_meta.extend([f'{c}\n']*len(d[k]))
        c += 1
    print('writing list...')
    with open(f'{out_prefix}_list_{i}.txt', 'w') as f:
        f.writelines(this_list)
    print('writing meta...')
    with open(f'{out_prefix}_meta_{i}.txt', 'w') as f:
        f.write(f'{len(this_list)} {c}\n')
        f.writelines(this_meta)
    i += 1
