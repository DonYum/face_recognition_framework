import torch
import sys


def param_num(state):
    num = 0
    for key in state.keys():
        sz = tuple(state[key].size())
        nn = 1
        for s in sz:
            nn *= s
        print(f'{key}: {sz}    {nn}')
        num += nn
    print(f'total num: {num}')


if __name__ == "__main__":
    fn = sys.argv[1]
    state = torch.load(fn)['state_dict']
    param_num(state)
