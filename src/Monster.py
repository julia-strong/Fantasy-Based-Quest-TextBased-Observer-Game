class Monster:
  hitPoints = 20
  loot = ["5 gold pieces", "0 silver pieces", "0 copper pieces"]
  damage = 1

  def attack(Player):
    Player.hitPoints -= Monster.damage
    print(f"The monster dealt {Monster.damage} damage to you!")
    print(f"You have {Player.hitPoints} hit points left.")