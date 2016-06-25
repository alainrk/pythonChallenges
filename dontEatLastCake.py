'''
Inside a room, there is a table with a pile of cakes. One of these cakes is filled with poison. Every turn, we will take cakes from this pile and eat them, leaving the last one to be the poisonous cake. Whoever eats the poisonous cake will die. The poisonous cake is clearly marked, so you do not have to guess. Rather you need to rely on your logic to save you.

The rules are simple:

1. Do not eat the last cake. It's obivious that poisonous cake will be the last to be eaten, so, DON'T EAT THE LAST CAKE. Try to make your opponent eat it.
2. When it is your turn, you can only take one, two or three cakes. The same rules apply to your opponent on there turn. You cannot skip your move, so choose wisely how many cakes to eat. Both opponents will be able to see how many cakes the other eats on each turn.
3. You cannot copy your opponent's previous move, likewise they cannot copy yours. If your opponent takes one cake, next move you can only choose between two or three. If you take three cakes, your opponent can only choose one or two. This doesn't effect the first move, only to subsequent.
4. If one of the players has no valid moves (e.g one cake left and previous move was one cake), that player will lose his turn and be skipped. Then the other player will be forced to eat the last cake. This is the ONLY case of turn skipping.
5. You can choose whether or not to go first. This decision is key to victory, so don't hurry, choose wisely!
'''

class Player:
  def __init__(self, cakes):
    pass

  def firstmove(self, cakes):
    return (cakes%4 != 2) if cakes != 1 else False

  def move(self, cakes, last):
    print cakes, last
    case = cakes%4
    if (case == 1):
        return 3
    if (case == 3):
        return 1 if last != 1 else 2
    if (case == 0):
        return 2 if last != 2 else 3
    return 1
