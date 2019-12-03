#!/usr/bin/python
# -*- coding: utf-8 -*-

from game import Game

def main():
    game = Game(10)

    game.board[0][1].state = 'alive'
    game.board[1][2].state = 'alive'
    game.board[2][0].state = 'alive'
    game.board[2][1].state = 'alive'
    game.board[2][2].state = 'alive'

    for i in range(10):
        game.print_board()
        game.next_step()
        print('\n')

if __name__ == '__main__':
    main()
