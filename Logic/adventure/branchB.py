from common import *
import start

def roomB1():
    if roomEntered[Rooms.B1] == 'y':
        print 'Entered already'
    
    else:
        roomEntered[Rooms.B1] = 'y'
        clearScreen()
        print 'You make your way to the large wooden door.'
        whichWay = twoWays('OPEN', 'PEEK')
        if whichWay == '1':
            clearScreen()
            print 'You wrench the door open with a loud creak, calling the attention of the sentry at watch.'
            print 'He draws his sword.'
            print 'Brandishing your ', (playerStats[Stats.WEAPON]).lower(), ','
            print 'you give an uneasy glance towards your companion.'
            
            print '\nShe offers an apathetic shrug.'
            print '\"There\'s no other way; you\'ll have to fight.\"'
            next_clear()
            
            battle(soldierStats, playerStats)
            
            print 'Having defeated the sentry, you loot the key to the main gate.'
            print 'Before any other guards can realize you have escaped,'
            print 'you and your companion easily make your way to the entrance.'
            print 'You unlock the main gate and run for the hills.\n'
            print 'CONGRATULATIONS! You have escaped the dungeon.'
            tryAgain()
            
        else:
            clearScreen()
            print('You gently inch the door open. Peering through the sliver of doorway,')
            print('you see a single sentry standing watch, his back almost touching the door.')
            
            if playerStats[Stats.WEAPON] == rogueStats[Stats.WEAPON]:
                print('With dagger in hand, you thrust it\'s sharp tip into his side.')
                print('His body false limp, and you let his body slide to the floor.')
                
                next_clear()
                print('Keeping to the shadows, you and your companion stealthily make your way to the dungeon entrance.')
                print('You slip out undetected.')
                print('CONGRATULATIONS! You escaped the dungeon.')
                tryAgain()
        
            elif playerStats[Stats.WEAPON] == warriorStats[Stats.WEAPON]:
                print('You wrench the door open with a loud creak.')
                print('Before the guard realizes what is happening, you lunge with all your weight behind your shield.')
                print('You both land in a pile on the floor. He\'s out cold, but you give him a sharp jab to the nose for good measure.')
                next_clear()
                
                print('The ruckus of your attack has alerted the other guards. You hear them assembling in the next room.')
                print('"Now you\'ve done it," you hear your companion grumble behind you.')
                print('She draws her blade and readies for battle.')
                
                fight = twoWays('DEFEND', 'ATTACK')
                if fight == '1':
                    clearScreen()
                    print('You upturn a table and brace the door. With your shield on guard, ')
                    print('you await the skirmish about to erupt.')
                    print('The door bursts open with a fireball. The soldiers rush in.')
                    print('You fight your hardest, but there are just too many of them.')
                    print('You succumb to their military strength.')
                    gameOver()
                    
                else:
                    clearScreen()
                    print('You look to your companion, waiting at the next door.')
                    print('Readying your shield, you give her a confident nod.')
                    print('She swings the door open, and you barrell through the door way at ramming speed.')
                    print('You can hear the clashing of swords just at your back.')
                    
                    print('\nYou hear the zip of loosed arrows.')
                    print('You duck behind your shield and feel the thud as they make contact with you shield.')
                    
                    print('\nThere\'s no looking back.')
                    print('You continue on at top speed, slamming your shield against oncoming soldiers.')
                    print('You finally make it to the dungeon\'s entrance.')
                    print('You burst through with your comrade close at your heels.')
                    print('CONGRATULATIONS! You have escaped the dungeon.\n')
                    tryAgain()
                        
            else:
                
                print('Suddenly, the guard turns around. He promptly draws his sword and runs you through.')
                gameOver()