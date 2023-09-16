#!/usr/bin/env python3
from brain_games.engine import start
from brain_games.games import progression as game
import prompt
import random
import sys
sys.path = "python-project-49/brain_games/engine.py"


def main():
    start(game)


if __name__ == '__main__':
    main()
