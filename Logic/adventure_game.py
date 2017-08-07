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
    next()
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
                return 'FORWARD'
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
                sys.stdout.write('You carefully tread along the narrow path and continue through the door on the other side.')
                return 'FORWARD'
            elif which_way == 'BACK':
                proceed = True
                cell_hall()
            else:
                sys.stdout.write('Please choose FORWARD or BACK.')
        

def door1():
    sys.stdout.write('Door Room 1')

def game():

    dungeon_cell()
    junction1 = cell_hall()
    if junction1 == 'LEFT':
        stairs1()
    elif junction1 == 'RIGHT':
        door1()
    
game()   

