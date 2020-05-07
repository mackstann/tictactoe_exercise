#!/usr/bin/env python3

import itertools
import re


def grouper(iterable, n, fillvalue=None):
    "Collect data into fixed-length chunks or blocks"
    args = [iter(iterable)] * n
    return itertools.zip_longest(fillvalue=fillvalue, *args)


class Board:
    def __init__(self):
        self.board = ['-']*9

    def add(self, x, y, symbol):
        assert 0 <= x <= 2
        assert 0 <= y <= 2
        assert symbol in ('X', 'O')
        index = y * 3 + x
        self.add_at_index(index, symbol)

    def add_at_index(self, index, symbol):
        assert 0 <= index <= 8
        self.board[index] = symbol

    def display(self):
        rows = grouper(self.board, 3)
        for row in rows:
            print('|'.join(row))

    def full(self):
        return '-' not in self.board

    def taken(self, x, y):
        index = y * 3 + x
        return self.board[index] != '-'

    def won(self):
        for char in ('X', 'O'):
            patterns = [
                '^nnn......$',
                '^...nnn...$',
                '^......nnn$',
                '^n..n..n..$',
                '^.n..n..n.$',
                '^..n..n..n$',
                '^n...n...n$',
                '^..n.n.n..$',
            ]
            for pat in patterns:
                pat = pat.replace('n', char)
                if re.match(pat, ''.join(self.board)):
                    return True
        return False

    # this is where i ran out of time
    #def move_would_win(self, symbol):
    #    for i in range(9):
    #        copy = Board()
    #        copy.board = self.board[:] # force a copy
    #        copy.add_at_index(i, symbol)
    #        if 


class AI:
    board = None

    def __init__(self, board):
        self.board = board

    def make_any_move(self):
        if self.board.full():
            raise RuntimeError("No spots left")

        first_index = self.board.board.index('-')
        self.board.add_at_index(first_index, 'O')


def game_loop():
    b = Board()
    ai = AI(b)
    while not b.full():
        human_input = input()
        if not re.match(r'^\s*[012]\s+[012]\s*$', human_input):
            print('Please enter a move in the format: "x y"')
            continue

        x, y = [ int(n) for n in human_input.strip().split() ]
        if b.taken(x, y):
            print('Spot at %d,%d is taken; try again' % (x, y))


        b.add(x, y, 'X')
        if b.won():
            b.display()
            print('The game is done!')
            break

        if not b.full():
            ai.make_any_move()

        if b.won():
            b.display()
            print('The game is done!')
            break

        b.display()


def main():
    #b = Board()
    #b.add(0, 0, 'X')
    #b.display()

    #assert not b.full()
    #for y in (0,1,2):
    #    for x in (0,1,2):
    #        b.add(x, y, 'X')
    #assert b.full()

    #ai = AI(b)
    #ai.make_any_move()
    #b.display()

    game_loop()


if __name__ == '__main__':
    main()
