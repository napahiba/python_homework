def clear_screen():
    print('\n' * 50)
    
def next():
    raw_input('Press ENTER to continue...\n')

def next_clear():
    next()
    clear_screen()
    
def display_stats():
    print('\nSTATS')
    #print('Weapon: '    +   game.weapon)
    print('Strength: '  +   str(game.strength))
    print('Stealth: '   +   str(game.stealth))
    print('Wisdom: '    +   str(game.wisdom))
    next()

def twoWays(option1, option2):
    while True:
        print "What will you choose?"
        print '1) ', option1
        print '2) ', option2
        choice = raw_input()

        if choice == 1 or 2:
            return choice
        else:
            print "Please choose from the numbers below."
        
    

def dungeon_cell():
    clear_screen()
    print('You wake up on the cold stone floor of a dungeon cell.')
    print('It is hard to see; the dim light of a torch flickers outsied the bars of your cage door.')
    print('You try to sit up, but your body aches all over')
    print('What happened? Your head throbs, and your mind draws a blank.')
    next()
    
    print('Suddenly, you hear a clamor echoing in the distance.')
    print('The commotion draws nearer. Sharp yells and clashes of metal ring in your ears.')
    print('There is the sound of the door unlocking and then the scraping of the heavy door against the floor.')
    print('You strain to look, but you still cannot move.')
    next_clear()

    print('A figure, shrouded in a dark hood, stands over you.')
    print('A soft hand touches your forehead. You see a green glowing light, and a gentle warmth washes over you.')
    print('All your fatigue fades away.')
    next()

    print('She pulls her hood back and scolds you with a harsh whisper, ')
    print('\"What are you doing?! Get up we have to get out of here FAST!\"')
    next()

    print('\"Here take one of these. You\'ll need it.\"')
    
    weapon_choice = False
    while weapon_choice == False:
        
        print('\nShe offers you a weapon.')
        print('1) OAKEN SHIELD')
        print('2) AMETHYST WAND')
        print('3) SILVER DAGGER')

        weapon = raw_input('Which do you chose?\n')
        
        if weapon == '1' or weapon == 'oaken shield':
            
            weapon_choice = True
        elif weapon == '2' or weapon == 'amethyst wand':
            game.weapon = 'amethyst wand'
            game.strength = 7
            game.stealth = 5
            game.wisdom = 12
            weapon_choice = True
        elif weapon == '3' or weapon == 'silver dagger':
            game.weapon = 'silver dagger'
            game.strength = 5
            game.stealth = 12
            game.wisdom = 7
            weapon_choice = True
        else:
            print('Please choose one of the weapons.')
    
        
    display_stats()
    print('She hands you the ' + game.weapon + '. Then pulls you to your feet.')
    print('\"C\'mon!\", she urges, leading you out of the cell.')
    next_clear()

def cell_hall():    
    print('You are in a narrow corridor, the walls lined by the iron bars of countless cells.')
    way_choice = False
    while way_choice == False:
        print('To your LEFT, a dark stairway leads deeper into the dungeon.')
        print('To your RIGHT, a large wooden door.')
        whichWay('LEFT', 'RIGHT')
        """
        which_way = raw_input('Which way will do you go?\n')
        which_way = which_way.upper()
    
        if which_way == 'LEFT':
            way_choice = True
            return 'LEFT'
        elif which_way == 'RIGHT':
            way_choice = True
            return 'RIGHT'
        else:
            print('Please choose LEFT or RIGHT.')
    """
def stairs1():
    clear_screen()
    print('You descend the stone steps.')
    print('It gets darker and darker, the farther you go.')
    print('Soon just a tiny glint of light is left from the corridor you just left.')
    print('Finally, you reach the bottom of the stair, but you can\'t see a thing.')
    next_clear()
    
    if game.weapon == 'amethyst wand':
        print('You raise your wand and cast a spell')
        print('~CLARA MERIDIEM ILLUSTRANT~')
        print('Your wand produces an orb of radiant lavender light.')
        print('With the flick of your wrist, the orb bobs up and hangs in the air above you.')
        print('With the room illuminated, you can see a narrow winding path ahead.')
        print('On either side of the path, bottomless pits. At the other side of the room you see a door.')
        proceed = False
        while proceed == False:
            which_way = raw_input('Will you proceed? FORWARD/BACK')
            if which_way == 'FORWARD':
                proceed = True
                print('You carefully tread along the narrow path and continue through the door on the other side.')
                print('Through the door, you enter the underground catacombs.')
                print('You make your way through the catacombs and escape the dungeon.')
                print('CONGRATULATIONS! You have escaped the dungeon.')
            elif which_way == 'BACK':
                cell_hall()
            else:
                print('Please choose FORWARD or BACK.')
    else:
        proceed = False
        while proceed == False:
            which_way = raw_input('Will you proceed? FORWARD/BACK')
            if which_way == 'FORWARD':
                proceed = True
                print('You make your way through the darkness, but, after just a few steps,')
                print('\n')
                print('the ground is gone from beneath your feet.')
                print('\n')
                print('You fall into a bottomless pit, never to be seen again.')
                
            elif which_way == 'BACK':
                proceed = True
                cell_hall()
            else:
                print('Please choose FORWARD or BACK.')
        

def door1():
    clear_screen()
    print('You make your way to the large wooden door.')
    door_choice = False
    while door_choice == False:
        print('\n')
        which_way = raw_input('What will you do? OPEN or PEEK')
        if which_way == 'OPEN':
            door_choice = True
            print('\n')
            print('You wrench the door open with a loud creak, calling the attention of the sentry at watch.')
            print('\n')
            print('He promptly draws his sword and runs you through.')
        elif which_way == 'PEEK':
            door_choice = True
            print('\n')
            print('You gently inch the door open. Peering through the sliver of doorway,')
            print('\n')
            print('you see a single sentry standing watch, his back almost touching the door.')
            if game.weapon == 'silver dagger':
                print('\n')
                print('With dagger in hand, you thrust it\'s sharp tip into his side.')
                print('\n')
                print('His body false limp, and you let his body slide to the floor.')
                print('\n')
                next_clear()
                print('Keeping to the shadows, you and your companion stealthily make your way to the dungeon entrance.')
                print('\n')
                print('You slip out undetected.')
                print('\n' * 2)
                print('CONGRATULATIONS! You escaped the dungeon.')
            elif game.weapon == 'oaken shield':
                print('\n')
                print('You wrench the door open with a loud creak.')
                print('\n')
                print('Before the guard realizes what is happening, you lunge with all your weight behind your shield.')
                print('\n')
                print('You both land in a pile on the floor. He\'s out cold, but you give him a sharp jab to the nose for good measure.')
                next_clear()
                print('The ruckus of your attack has alerted the other guards. You hear them assembling in the next room.')
                print('\n')
                print('"Now you\'ve done it," you hear your companion grumble behind you.')
                print('\n')
                print('She draws her blade and readies for battle.')
                print('\n')
                fight_choice = False
                fight = raw_input('What will you do? DEFEND or ATTACK')
                while fight_choice == False:
                    if fight == 'DEFEND':
                        fight_choice = True
                        print('\n')
                        print('You upturn a table and brace the door. With your shield on guard, ')
                        print('\n')
                        print('you await the skirmish about to erupt.')
                        print('\n')
                        print('The door bursts open with a fireball. The soldiers rush in.')
                        print('\n')
                        print('You fight your hardest, but there are just too many of them.')
                        print('\n')
                        print('You succumb to their military strength.')
                    elif fight == "ATTACK":
                        fight_choice = True
                        clear_screen()
                        print('You nod to your companion, waiting at the next door.')
                        print('\n')
                        print('You give her a confident nod.')
                        print('\n')
                        print('She swings the door open, and you barrell through the door way at ramming speed.')
                        print('\n')
                        print('You can hear the clashing of swords just at your back.')
                        print('\n')
                        print('You hear the zip of loosed arrows.')
                        print('\n')
                        print('You duck behind your shield and feel the thud as they make contact with you shield.')
                        print('\n')
                        print('There\'s no looking back.')
                        print('\n')
                        print('You continue on at top speed, hurling your shield against oncoming soldiers.')
                        print('\n')
                        print('You finally make it to the dungeon\'s entrance.')
                        print('\n')
                        print('You burst through with your comrade close at your heels.')
                        print('\n')
                        print('\n')
                        print('CONGRATULATIONS! You have escaped the dungeon.')
                        
                        
            elif game.weapon == 'amethyst wand':
                print('\n')
                print('Suddenly, the guard turns around. He promptly draws his sword and runs you through.')
        else:
            print('\n')
            print('Please choose OPEN or PEEK.')
        

def game():
    weapon = 'none'
    strength = 0
    stealth = 0
    wisdom = 0
    stats = ['Weapon', 'Strength', 'Stealth', 'Wisdom']
    player = []
    warrior = ['oaken shield', 12, 5, 7]
    mage = ['amethyst wand', 5, 7, 12]
    rogue = ['silver dagger', 7, 12, 5]
    dungeon_cell()
    junction1 = cell_hall()
    if junction1 == 'LEFT':
        stairs1()
    elif junction1 == 'RIGHT':
        door1()

game()   

