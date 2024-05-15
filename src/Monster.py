import Player
loot = "5 gold pieces", "0 silver pieces", "0 copper pieces"
crabLoot = "One small figurine in the shape of a crab (This is worth approximately 3 sivler pieces if it is needed later on)"
birdLoot = "1 gold piece" , "10 silver pieces"
batLoot = "a bat tooth"
class Monster:
  hitPoints = 20
  damage = 3
  

  def attack(Player):
    Player.hitPoints -= Monster.damage
    print(f"The creature dealt {Monster.damage} damage to you!")
    print(f"You have {Player.hitPoints} hit points left.")