#!/usr/bin/env python3
from brain_games.engine import game_proc
from brain_games.games import gcd as game
import sys
sys.path = "python-project-49/brain_games/engine.py"


def main():
    game_proc(game)


if __name__ == '__main__':
    main()
