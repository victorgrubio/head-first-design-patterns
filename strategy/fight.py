from characters.archer import Archer
from characters.knight import Knight
from random import randint

if __name__ == "__main__":
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