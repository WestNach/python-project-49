#!/usr/bin/env python3
import prompt
import random
import sys
sys.path = "python-project-49/brain_games/engine.py"
from brain_games.engine import start
from brain_games.games import prime as game


def main():
    start(game)
    
    
if __name__ == '__main__':
    main()
