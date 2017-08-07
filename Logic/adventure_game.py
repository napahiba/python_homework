import sys
from time import sleep

def clear_screen():
    sys.stdout.write('\n' * 50)
    
def next():
    sys.stdout.write('\n')
    sys.stdout.flush()
    raw_input('Press ENTER to continue...')

def next_clear():
    next()
    clear_screen()
    
def display_stats():
    sys.stdout.write('\n' * 2)
    sys.stdout.write('Weapon: ')
    sys.stdout.write(game.weapon)
    sys.stdout.write('\n')
    sys.stdout.write('Strength: ')
    sys.stdout.write(str(game.strength))
    sys.stdout.write('\n')
    sys.stdout.write('Agility: ')
    sys.stdout.write(str(game.agility))
    sys.stdout.write('\n')
    sys.stdout.write('Wisdom: ')
    sys.stdout.write(str(game.wisdom))
    next_clear()

def dungeon_cell():
    clear_screen()
    sys.stdout.write('You wake up on the cold stone floor of a dungeon cell.')
    sys.stdout.write('\n')
    sys.stdout.write('It is hard to see; the dim light of a torch flickers outsied the bars of your cage door.')
    sys.stdout.write('\n')
    sys.stdout.write('You try to sit up, but your body aches all over')
    sys.stdout.write('\n')
    sys.stdout.write('What happened? Your head throbs, and your mind draws a blank.')
    next()

    sys.stdout.write('\n' * 2)
    sys.stdout.write('Suddenly, you hear a clamor echoing in the distance.')
    sys.stdout.write('\n')
    sys.stdout.write('The commotion draws nearer. Sharp yells and clashes of metal ring in your ears.')
    sys.stdout.write('\n')
    sys.stdout.write('There is the sound of the door unlocking and then the scraping of the heavy door against the floor.')
    sys.stdout.write('\n')
    sys.stdout.write('You strain to look, but you still cannot move.')
    next_clear()

    sys.stdout.write('\n' * 2)
    sys.stdout.write('A figure, shrouded in a dark hood, stands over you.')
    sys.stdout.write('\n')
    sys.stdout.write('A soft hand touches your forehead. You see a green glowing light, and a gentle warmth washes over you.')
    sys.stdout.write('\n')
    sys.stdout.write('All your fatigue fades away.')
    next()

    sys.stdout.write('\n' * 2)
    sys.stdout.write('She pulls her hood back and scolds you with a harsh whisper, ')
    sys.stdout.write('\n')
    sys.stdout.write('\"What are you doing?! Get up we have to get out of here FAST!\"')
    next()

    sys.stdout.write('\n' * 2)
    sys.stdout.write('Here take one of these. You\'ll need it.')
    sys.stdout.write('\n')
    weapon_choice = False
    while weapon_choice == False:
        sys.stdout.write('\n')
        sys.stdout.write('She offers you a weapon.')
        sys.stdout.write('\n')
        sys.stdout.write('\n')
        sys.stdout.write('1) OAKEN SHIELD')
        sys.stdout.write('\n')
        sys.stdout.write('2) AMETHYST WAND')
        sys.stdout.write('\n')
        sys.stdout.write('3) SILVER DAGGER')
        sys.stdout.write('\n')
        sys.stdout.write('\n')
        weapon = raw_input('Which do you chose?')
        
        if weapon == '1' or weapon == 'oaken shield':
            game.weapon = 'oaken shield'
            game.strength = 12
            game.agility = 7
            game.wisdom = 5
            weapon_choice = True
        elif weapon == '2' or weapon == 'amethyst wand':
            game.weapon = 'amethyst wand'
            game.strength = 7
            game.agility = 5
            game.wisdom = 12
            weapon_choice = True
        elif weapon == '3' or weapon == 'silver dagger':
            game.weapon = 'silver dagger'
            game.strength = 5
            game.agility = 12
            game.wisdom = 7
            weapon_choice = True
        else:
            sys.stdout.write('Please choose one of the weapons.')
            sys.stdout.write('\n')
    
        
    sys.stdout.write('\n' * 2)
    sys.stdout.write('She hands you the ')
    sys.stdout.write(game.weapon)
    sys.stdout.write('. Then pulls you to your feet.')
    sys.stdout.write('\n')
    sys.stdout.write('\"C\'mon!\", she urges, leading you out of the cell.')
    next_clear()

def cell_hall():    
    sys.stdout.write('\n')
    sys.stdout.write('You are in a narrow corridor, the walls lined by the iron bars of countless cells.')
    way_choice = False
    while way_choice == False:
        sys.stdout.write('\n')
        sys.stdout.write('To your LEFT, a dark stairway leads deeper into the dungeon.')
        sys.stdout.write('\n')
        sys.stdout.write('To your RIGHT, a large wooden door.')
        sys.stdout.write('\n')
        sys.stdout.write('\n')
        which_way = raw_input('Which way will do you go?')
        which_way.lower()
    
        if which_way == 'LEFT':
            way_choice = True
            return 'LEFT'
        elif which_way == 'RIGHT':
            way_choice = True
            return 'RIGHT'
        else:
            sys.stdout.write('Please choose LEFT or RIGHT.')
    
def stairs1():
    clear_screen()
    sys.stdout.write('You descend the stone steps.')
    sys.stdout.write('\n')
    sys.stdout.write('It gets darker and darker, the farther you go.')
    sys.stdout.write('\n')
    sys.stdout.write('Soon just a tiny glint of light is left from the corridor you just left.')
    sys.stdout.write('\n')
    sys.stdout.write('Finally, you reach the bottom of the stair, but you can\'t see a thing.')
    sys.stdout.write('\n')
    next_clear()
    
    if game.weapon == 'amethyst wand':
        sys.stdout.write('You raise your wand and cast a spell')
        sys.stdout.write('\n')
        sys.stdout.write('~CLARA MERIDIEM ILLUSTRANT~')
        sys.stdout.write('\n')
        sys.stdout.write('Your wand produces an orb of radiant lavender light.')
        sys.stdout.write('\n')
        sys.stdout.write('With the flick of your wrist, the orb bobs up and hangs in the air above you.')
        sys.stdout.write('\n')
        sys.stdout.write('With the room illuminated, you can see a narrow winding path ahead.')
        sys.stdout.write('\n')
        sys.stdout.write('On either side of the path, bottomless pits. At the other side of the room you see a door.')
        proceed = False
        while proceed == False:
            which_way = raw_input('Will you proceed? FORWARD/BACK')
            if which_way == 'FORWARD':
                proceed = True
                sys.stdout.write('You carefully tread along the narrow path and continue through the door on the other side.')
                sys.stdout.write('\n')
                sys.stdout.write('Through the door, you enter the underground catacombs.')
                sys.stdout.write('\n')
                sys.stdout.write('You make your way through the catacombs and escape the dungeon.')
                sys.stdout.write('\n')
                sys.stdout.write('CONGRATULATIONS! You have escaped the dungeon.')
            elif which_way == 'BACK':
                cell_hall()
            else:
                sys.stdout.write('Please choose FORWARD or BACK.')
    else:
        proceed = False
        while proceed == False:
            which_way = raw_input('Will you proceed? FORWARD/BACK')
            if which_way == 'FORWARD':
                proceed = True
                sys.stdout.write('You make your way through the darkness, but, after just a few steps,')
                sys.stdout.write('\n')
                sys.stdout.write('the ground is gone from beneath your feet.')
                sys.stdout.write('\n')
                sys.stdout.write('You fall into a bottomless pit, never to be seen again.')
                
            elif which_way == 'BACK':
                proceed = True
                cell_hall()
            else:
                sys.stdout.write('Please choose FORWARD or BACK.')
        

def door1():
    clear_screen()
    sys.stdout.write('You make your way to the large wooden door.')
    door_choice = False
    while door_choice == False:
        sys.stdout.write('\n')
        which_way = raw_input('What will you do? OPEN or PEEK')
        if which_way == 'OPEN':
            door_choice = True
            sys.stdout.write('\n')
            sys.stdout.write('You wrench the door open with a loud creak, calling the attention of the sentry at watch.')
            sys.stdout.write('\n')
            sys.stdout.write('He promptly draws his sword and runs you through.')
        elif which_way == 'PEEK':
            door_choice = True
            sys.stdout.write('\n')
            sys.stdout.write('You gently inch the door open. Peering through the sliver of doorway,')
            sys.stdout.write('\n')
            sys.stdout.write('you see a single sentry standing watch, his back almost touching the door.')
            if game.weapon == 'silver dagger':
                sys.stdout.write('\n')
                sys.stdout.write('With dagger in hand, you thrust it\'s sharp tip into his side.')
                sys.stdout.write('\n')
                sys.stdout.write('His body false limp, and you let his body slide to the floor.')
                sys.stdout.write('\n')
                next_clear()
                sys.stdout.write('Keeping to the shadows, you and your companion stealthily make your way to the dungeon entrance.')
                sys.stdout.write('\n')
                sys.stdout.write('You slip out undetected.')
                sys.stdout.write('\n' * 2)
                sys.stdout.write('CONGRATULATIONS! You escaped the dungeon.')
            elif game.weapon == 'oaken shield':
                sys.stdout.write('\n')
                sys.stdout.write('You wrench the door open with a loud creak.')
                sys.stdout.write('\n')
                sys.stdout.write('Before the guard realizes what is happening, you lunge with all your weight behind your shield.')
                sys.stdout.write('\n')
                sys.stdout.write('You both land in a pile on the floor. He\'s out cold, but you give him a sharp jab to the nose for good measure.')
                next_clear()
                sys.stdout.write('The ruckus of your attack has alerted the other guards. You hear them assembling in the next room.')
                sys.stdout.write('\n')
                sys.stdout.write('"Now you\'ve done it," you hear your companion grumble behind you.')
                sys.stdout.write('\n')
                sys.stdout.write('She draws her blade and readies for battle.')
                sys.stdout.write('\n')
                fight_choice = False
                fight = raw_input('What will you do? DEFEND or ATTACK')
                while fight_choice == False:
                    if fight == 'DEFEND':
                        fight_choice = True
                        sys.stdout.write('\n')
                        sys.stdout.write('You upturn a table and brace the door. With your shield on guard, ')
                        sys.stdout.write('\n')
                        sys.stdout.write('you await the skirmish about to erupt.')
                        sys.stdout.write('\n')
                        sys.stdout.write('The door bursts open with a fireball. The soldiers rush in.')
                        sys.stdout.write('\n')
                        sys.stdout.write('You fight your hardest, but there are just too many of them.')
                        sys.stdout.write('\n')
                        sys.stdout.write('You succumb to their military strength.')
                    elif fight == "ATTACK":
                        fight_choice = True
                        clear_screen()
                        sys.stdout.write('You nod to your companion, waiting at the next door.')
                        sys.stdout.write('\n')
                        sys.stdout.write('You give her a confident nod.')
                        sys.stdout.write('\n')
                        sys.stdout.write('She swings the door open, and you barrell through the door way at ramming speed.')
                        sys.stdout.write('\n')
                        sys.stdout.write('You can hear the clashing of swords just at your back.')
                        sys.stdout.write('\n')
                        sys.stdout.write('You hear the zip of loosed arrows.')
                        sys.stdout.write('\n')
                        sys.stdout.write('You duck behind your shield and feel the thud as they make contact with you shield.')
                        sys.stdout.write('\n')
                        sys.stdout.write('There\'s no looking back.')
                        sys.stdout.write('\n')
                        sys.stdout.write('You continue on at top speed, hurling your shield against oncoming soldiers.')
                        sys.stdout.write('\n')
                        sys.stdout.write('You finally make it to the dungeon\'s entrance.')
                        sys.stdout.write('\n')
                        sys.stdout.write('You burst through with your comrade close at your heels.')
                        sys.stdout.write('\n')
                        sys.stdout.write('\n')
                        sys.stdout.write('CONGRATULATIONS! You have escaped the dungeon.')
                        
                        
            elif game.weapon == 'amethyst wand':
                sys.stdout.write('\n')
                sys.stdout.write('Suddenly, the guard turns around. He promptly draws his sword and runs you through.')
        else:
            sys.stdout.write('\n')
            sys.stdout.write('Please choose OPEN or PEEK.')
        

def game():

    dungeon_cell()
    junction1 = cell_hall()
    if junction1 == 'LEFT':
        stairs1()
    elif junction1 == 'RIGHT':
        door1()
    
game()   

