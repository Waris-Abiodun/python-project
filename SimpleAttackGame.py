import random
import math

class Warrior:
    def __init__(self, name="Warrior", health=0, attackMax=0, shieldMax=0):
        self.name = name
        self.health = health
        self.attackMax = attackMax
        self.shieldMax = shieldMax
    def attack(self):
        attackAmount = self.attackMax * (random.random() + 0.5)
        return attackAmount
    def shield(self):
        ShieldAmount = self.shieldMax * (random.random() + 0.5)
        return ShieldAmount

class Battle:
    def StartBattle(self, warrior1, warrior2):
        while True:
            if self.getAttackResult(warrior1, warrior2) == "Game Over":
                print("Game Over")
                break
            elif self.getAttackResult(warrior2, warrior1) == "Game Over":
                print("Game Over")
                break
    @staticmethod
    def getAttackResult(Warrior1, Warrior2):
        Warrior1AttackAmount = Warrior1.attack()
        Warrior2ShieldAmount = Warrior2.shield()
        Warrior2DamageAmount = math.ceil(Warrior1AttackAmount - Warrior2ShieldAmount)
        if Warrior2DamageAmount > 0:
            Warrior2.health = Warrior2.health - Warrior2DamageAmount

        print("{} attacks {} and deals {} damage".format(Warrior1.name, Warrior2.name, Warrior2DamageAmount))
        print("{} is down to {} health".format(Warrior2.name, Warrior2.health))
        if Warrior2.health < 1 or Warrior1.health < 1:
            print("{} has Died and {} is Victorious".format(Warrior2.name, Warrior1.name))
            return "Game Over"
        else:
            return "Battle Continue"

def main():
    Jack = Warrior("Jack", 200, 38, 20)
    Sparrow = Warrior("Sparrow", 100, 40, 30)
    battle = Battle()
    battle.StartBattle(Jack, Sparrow)
main()
    
