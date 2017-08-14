from common import *
import branchA
import branchB

def dungeonCell():
    
    if roomEntered[Rooms.S1] == 'y':
        clearScreen()
        print 'You are back where you started.'
        print '\"We can\'t stay here much longer!\"'
        print '\nYou are in a narrow corridor.'
        print 'The walls are lined with the iron bars of countless cells.'
        print 'To your LEFT, a dark stairway leads deeper into the dungeon.'
        print 'To your RIGHT, a large wooden door.' 
        exitCell = twoWays('LEFT', 'RIGHT')
        if exitCell == '1':
            branchA.roomA1()
        else:
            branchB.roomB1()
    
    else: 
        roomEntered[Rooms.S1] = 'y'
        clearScreen()
        print 'You wake up on the cold stone floor of a dungeon cell.'
        print 'It is hard to see; the dim light of a torch flickers outside' 
        print 'the bars of your cage door.'
        print 'You try to sit up, but your body aches all over'
        print 'What happened? Your head throbs, and your mind draws a blank.'
        next_clear()
    
        print 'Suddenly, you hear a clamor echoing in the distance.'
        print 'The commotion draws nearer. Sharp yells and clashes of metal ring in your ears.'
        print 'There is the sound of the door unlocking and then the scraping of the heavy door against the floor.'
        print 'You strain to look, but you still cannot move.'
        next_clear()
    
        print 'A figure, shrouded in a dark hood, stands over you.'
        print 'A soft hand touches your forehead.'
        print 'You see a green glowing light.'
        print 'A gentle warmth washes over you, and all your fatigue fades away.'
        next_clear()
    
        print 'She pulls her hood back and scolds you with a harsh whisper, '
        print '\"What are you doing?!\"'
        print '\"GET UP!!\"'
        print '\"We need to get out of here FAST!\"'

        print '\n\"Here take one of these. You\'ll need it.\"'
    
        while True:
        
            print '\nShe offers you a weapon.'
            print '1) OAKEN SHIELD'
            print '2) AMETHYST WAND'
            print '3) SILVER DAGGER'

            weapon = raw_input('Which do you chose?\n')
        
            if weapon == '1':
                weapon = warriorStats
                break
            elif weapon == '2':
                weapon = mageStats
                break
            elif weapon == '3':
                weapon = rogueStats
                break
            else:
                clearScreen()
                print('Please choose from the numbers below.')
            
        
        for item in weapon:
            playerStats.append(item)
    
        clearScreen()
        print 'She hands you the ',(playerStats[Stats.WEAPON]).lower(),'. Then pulls you to your feet.'
        print '\"C\'mon!\", she urges, leading you out of the cell.'

        print '\nYou are in a narrow corridor.'
        print 'The walls are lined with the iron bars of countless cells.'
        print 'To your LEFT, a dark stairway leads deeper into the dungeon.'
        print 'To your RIGHT, a large wooden door.' 
        exitCell = twoWays('LEFT', 'RIGHT')
        if exitCell == '1':
            branchA.roomA1()
        else:
            branchB.roomB1()
            
