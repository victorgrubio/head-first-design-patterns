from random import randint
from argparse import ArgumentParser
from characters import Archer, Knight
import config


if __name__ == "__main__":
    parser = ArgumentParser()
    parser.add_argument('-h', '--help', )
    player1 = Archer()
    player2 = Knight()
    print(f"Player 1 Character:")
    player1.greet()
    player1.display()
    print(f"Player 2 Character:")
    player2.greet()
    player2.display()
    coin = randint(0, 1)
    if coin <= 0.5:
        print('Player 1 will hit first')
        player1.use_weapon(player2)
    else:
        print('Player 2 will hit first')
        player2.use_weapon(player1)