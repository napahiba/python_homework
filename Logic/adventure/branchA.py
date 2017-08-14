#start game from game.py
from common import *
import start

def roomA1():
    if roomEntered[Rooms.A1] == 'y':
        clearScreen()
        print 'You descend the dark staircase again.'
        if playerStats[Stats.WEAPON] == mageStats[Stats.WEAPON]:
            print 'Your spell looms high in the room,'
            print 'illuminating the winding path ahead of you.'
            print 'Will you traverse the path to the door?'
            whichWay = twoWays('FORWARD', 'BACK')
            if whichWay == '1':
                clearScreen()
                print('You carefully tread along the narrow path and continue through the door on the other side.')
                print('Through the door, you enter the underground catacombs.')
                print('You make your way through the catacombs and escape the dungeon.')
                print('CONGRATULATIONS! You have escaped the dungeon.\n')
                tryAgain()
            else:
                start.dungeonCell()
        else:
            print 'You still can\'t see a thing.'
            print 'Do you want to proceed?'
            whichWay = twoWays( 'FORWARD', 'BACK')
            if whichWay == '1':
                clearScreen()
                print 'You make your way through the darkness, but, after just a few steps,'
                print 'the ground is gone from beneath your feet.'
                print 'You fall into a bottomless pit, never to be seen again.'
                gameOver()
                
            else:
                start.dungeonCell()
    else:
        roomEntered[Rooms.A1] = 'y'
        clearScreen()
        print('You descend the stone steps.')
        print('It gets darker and darker, the farther you go.')
        print('Soon just a tiny glint of light is left from the corridor you just left.')
        print('Finally, you reach the bottom of the stair, but you can\'t see a thing.')
        
        if playerStats[Stats.WEAPON] == mageStats[Stats.WEAPON]:
            clearScreen()
            print('\nYou raise your wand and cast a spell')
            print('\n~CLARA MERIDIEM ILLUSTRANT~\n')
            print('Your wand produces an orb of radiant lavender light.')
            print('With the flick of your wrist, the orb bobs up and hangs in the air above you.')
            print('With the room illuminated, you can see a narrow winding path ahead.')
            print('On either side of the path, bottomless pits. At the other side of the room you see a door.')
            whichWay = twoWays('FORWARD', 'BACK')
            if whichWay == '1':
                clearScreen()
                print('You carefully tread along the narrow path and continue through the door on the other side.')
                print('Through the door, you enter the underground catacombs.')
                print('You make your way through the catacombs and escape the dungeon.')
                print('CONGRATULATIONS! You have escaped the dungeon.\n')
                tryAgain()
            else:
                start.dungeonCell()
        else:
            print 'Do you want to proceed?'
            whichWay = twoWays( 'FORWARD', 'BACK')
            if whichWay == '1':
                clearScreen()
                print 'You make your way through the darkness, but, after just a few steps,'
                print 'the ground is gone from beneath your feet.'
                print 'You fall into a bottomless pit, never to be seen again.'
                gameOver()
                
            else:
                start.dungeonCell()

        