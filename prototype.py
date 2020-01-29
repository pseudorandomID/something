import random

def createCharacter():
    def isValid(stat):
        if stat > 100 or stat < 1:
            return False;
        return True;

    def printRem(rem):
        print("남은 스탯: " + str(rem))

    def getInput(text):
        while(True):
            strength = int(input(text))
            if isValid(strength):
                return strength
            else:
                print("error")

    def isConfirmed():
        while(True):
            confirm = input("confirm? (y/n) : ")
            if confirm == 'y':
                return True
            if confirm == 'n':
                return False

            print("Invalid input")

    org_dice = random.randint(1,801);
    while(True):
        curr_dice = org_dice
        printRem(curr_dice)

        strength = getInput("힘: ")
        curr_dice -= strength
        printRem(curr_dice)

        mp = getInput("mp: ")
        curr_dice -= mp
        printRem(curr_dice)

        hp = getInput("hp: ")
        curr_dice -= hp
        printRem(curr_dice)

        intel = getInput("int: ")
        curr_dice -= intel
        printRem(curr_dice)

        crit = getInput("crit : ")
        curr_dice -= crit
        printRem(curr_dice)

        eva = getInput("eva: ")
        curr_dice -= eva
        printRem(curr_dice)

        spd = getInput("spd: ")
        curr_dice -= spd
        printRem(curr_dice)

        confirm = isConfirmed()

        if confirm == True:
            break
        else:
            continue
        
    return character(strength, mp, hp, intel, crit, eva, spd)
    
class character:
    def __init__(self, strength, mp, hp, intel, crit, eva, spd):
        self.strength = strength
        self.mp = mp
        self.hp = hp
        self.intel = intel
        self.crit = crit
        self.eva = eva
        self.spd = spd
        self.level = 1

    def printStat(self):
        print("level:%d "%(self.level))
        print("str:%d "%(self.strength))
        print("mp:%d "%(self.mp))
        print("hp:%d "%(self.hp))
        print("int:%d "%(self.intel))
        print("crit:%d "%(self.crit))
        print("eva:%d "%(self.eva))
        print("spd:%d "%(self.spd))

#test
if __name__ =="__main__":
    mychar = createCharacter()
    mychar.printStat()
    #print("test passed")
    #pass
    
