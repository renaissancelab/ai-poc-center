#!/usr/bin/env python3

from towhee import pipe


def my_func(x):
   return x + 1


if __name__ == '__main__':
    # add_one is a pipeline
    add_one = (
        pipe.input('x') # input node
        .map('x', 'y', my_func) # map node
        .output('y') # output node
    )

    res = add_one(0).get()

