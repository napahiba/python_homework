import start
from random import randint

class Stats:
    WEAPON, HP, AP, STR, WIS, AGL = range(6)
    
warriorStats = ['OAKEN SHIELD', 25, 10, 12, 5, 7]
mageStats = ['AMETHYST WAND', 12, 20, 5, 8, 7]
rogueStats = ['SILVER DAGGER', 18, 15, 7, 5, 12]
soldierStats = ['BROADSWORD', 30, 0, 6, 5, 5]
playerStats = []

class Rooms:
    S1, A1, B1 = range(3)
roomEntered = [ 'n', 'n', 'n']

def clearScreen():
    print('\n' * 50)

def next_clear():
    raw_input('Press ENTER to continue...\n')
    clearScreen()

def twoWays(option1, option2):
    while True:
        print "What will you choose?"
        print '1) ', option1
        print '2) ', option2
        choice = raw_input()

        if choice == '1' or choice == '2':
            return choice
        else:
            clearScreen()
            print "Please choose from the numbers below."
    
def displayStats(arr):
    print '\nWEAPON:\t', arr[Stats.WEAPON]
    print 'HP:\t', arr[Stats.HP]
    print 'AP:\t', arr[Stats.AP]
    print 'STR:\t', arr[Stats.STR]
    print 'WIS:\t', arr[Stats.WIS]
    print 'AGL:\t', arr[Stats.AGL]
    next_clear()

def gameOver():
    print 'GAME OVER'
    print 'Try again?'
    tryAgain = twoWays('YES', 'NO')
    if tryAgain == '1':
        for rooms in range(len(roomEntered)):
            roomEntered[rooms] = 'n'
        for stats in range(len(playerStats)):
            del playerStats[-1]
        soldierStats[Stats.HP] = 30
        start.dungeonCell()
    else:
        return 0
        
def tryAgain():
    print 'Try again?'
    tryAgain = twoWays('YES', 'NO')
    if tryAgain == '1':
        for rooms in range(len(roomEntered)):
            roomEntered[rooms] = 'n'
            for stats in range(len(playerStats)):
                del playerStats[-1]
            soldierStats[Stats.HP] = 30
        start.dungeonCell()
    else:
        return 0
        
def battle(enemy, player):
    while player[Stats.HP] > 0 and enemy[Stats.HP] > 0:
        #player turn
        clearScreen()
        print '==========BATTLE=========='
        print 'Soldier HP: ', enemy[Stats.HP]
        print 'Your HP: ', player[Stats.HP], '\n'
        action = battleMenu(player)
        if action == '1':
            attack(enemy, player)
        next_clear()
        
        #enemy turn
        if enemy[Stats.HP] > 0:
            print '==========BATTLE=========='
            print 'Soldier HP: ', enemy[Stats.HP]
            print 'Your HP: ', player[Stats.HP], '\n'
            enemyAttack = randint(0, enemy[Stats.STR])
            if enemyAttack == 0:
                print 'Your enemy swings his sword wildly, narrowly missing you.'
                next_clear()
            else:
                print 'Your enemy lands a blow, dealing', enemyAttack, 'damage to you.'
                player[Stats.HP] = player[Stats.HP] - enemyAttack
                next_clear()
                
    if player[Stats.HP] < 0:
        print "You were defeated!\n"
        gameOver()
    else:
        print "Your enemy has fallen!"
    
    
def battleMenu(player):
    if player[Stats.WEAPON] == warriorStats[Stats.WEAPON]:
        return twoWays('SHIELD BASH', 'SHIELD BLOCK')
    
    elif player[Stats.WEAPON] == mageStats[Stats.WEAPON]:
        return twoWays('FIREBALL', 'DEFLECT')
        
    elif player[Stats.WEAPON] == rogueStats[Stats.WEAPON]:
        return twoWays('BACKSTAB', 'DODGE')
        
def attack(enemy, player):
    hit = 0
    if player[Stats.WEAPON] == warriorStats[Stats.WEAPON]:
        hit = randint(0, player[Stats.STR])
        if hit == 0:
            print 'You lunged with your shield, but your enemy dodged your attack.'
        else:
            print 'You lunged with your shield, and did', hit, 'points of damage.'
            enemy[Stats.HP] = enemy[Stats.HP] - hit
    
    elif player[Stats.WEAPON] == mageStats[Stats.WEAPON]:
        hit = randint(0, player[Stats.WIS])
        if hit == 0:
            print 'You hurl a fireball from your wand, but miss your target.'
        else:
            print 'Launching a fireball straight at your enemy, you deal', hit, 'points of damage.'
            enemy[Stats.HP] = enemy[Stats.HP] - hit
            
    elif player[Stats.WEAPON] == rogueStats[Stats.WEAPON]:
        hit = randint(0, player[Stats.STR])
        backstab = randint(0, player[Stats.AGL])
        if hit == 0:
            print 'You thrust your dagger at your enemy, but he expertly deflects it with his sword.'
        elif backstab < (player[Stats.AGL])/2:
            print 'You thrust your dagger at your enemy, dealing', hit, 'points of damage.'
            enemy[Stats.HP] = enemy[Stats.HP] - hit
        elif backstab > (player[Stats.AGL])/2:
            print 'You stealthily maneuver behind your enemy. A single slash deals', hit, 'points of damage.'
            bonus = player[Stats.STR]/2
            hit = hit + bonus
            print 'He is caught by surprise!'
            print 'You swiftly thrust your dagger for an extra', bonus, 'points of damage.'
            enemy[Stats.HP] = enemy[Stats.HP] - hit