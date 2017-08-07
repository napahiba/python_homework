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
sys.stdout.write('A hooded figure stand over you.')
sys.stdout.write('\n')
sys.stdout.write('A warm hand touches your forehead. You see a green glowing light, and a gentle warmth washes over you.')
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
    weapon = raw_input('Which do you chose.')
    if weapon == '1' or weapon == 'oaken shield':
        weapon = 'oaken shield'
        strength = 12
        agility = 7
        wisdom = 5
        weapon_choice = True
    elif weapon == '2' or weapon == 'amethyst wand':
        weapon = 'amethyst wand'
        strength = 7
        agility = 5
        wisdom = 12
        weapon_choice = True
    elif weapon_choice == '3' or weapon == 'silver dagger':
        weapon = 'silver dagger'
        strength = 5
        agility = 12
        wisdom = 7
        weapon_choice = True
    else:
        sys.stdout.write('Please choose one of the weapons.')
        sys.stdout.write('\n')
    
        

sys.stdout.write('\n' * 2)
sys.stdout.write('You chose the ')
sys.stdout.write(weapon)
sys.stdout.write('.')
sys.stdout.flush()



