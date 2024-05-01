loot = "5 gold pieces", "0 silver pieces", "0 copper pieces"
crabLoot = "One small figurine in the shape of a crab (This is worth approximately 3 sivler pieces if it is needed later on)"
class Monster:
  hitPoints = 20
  damage = 1

  def attack(Player):
    Player.hitPoints -= Monster.damage
    print(f"The monster dealt {Monster.damage} damage to you!")
    print(f"You have {Player.hitPoints} hit points left.")