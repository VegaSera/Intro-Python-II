from room import Room
from player import Player
from item import Item, Weapon, LightSource, Gold
from utils import dice



items = {
    'lantern': LightSource("Lantern", "A brightly shining oil lantern. Seems to have plenty of fuel.", 50),
    'sword': Weapon("Longsword", "A simple longsword, but sturdy and dependable.", 200, (1,8,0)),
    'gold': Gold("Gold Pieces", "Glorious currency", 24)
}


# Declare all the rooms


room = {
    'outside':  Room("Outside Cave Entrance",
                     "North of you, the cave mount beckons",
                     s_to_err="You refuse to leave this area without claiming the treasure.",
                     e_to_err="You refuse to leave this area without claiming the treasure.",
                     w_to_err="You refuse to leave this area without claiming the treasure.",
                     items=[items['lantern']],
                     is_light=True),

    'foyer':    Room("Foyer", """Dim light filters in from the south. Dark, dusty
passages run north and east.""", w_to_err="A solid wall blocks your path westward.", is_light=True),

    'overlook': Room("Grand Overlook", """A steep cliff appears before you, falling
into the darkness. Ahead to the north, a light flickers in
the distance, but there is no way across the chasm.""",
                     n_to_err="You begin to take a step into the open air of the chasm, "
                     "but you remember at the last moment that gravity exists.",
                     e_to_err="There is no way to shimmy along the cliff eastward.",
                     w_to_err="There is no way to shimmy along the cliff westward.",
                     dark="You enter into this dark room and feel a sudden rush of wind and echoes off of distant walls. "
                          "You get the distinct feeling that this room is very dangerous and you should turn back.."),

    'narrow':   Room("Narrow Passage", """The narrow passage bends here from west
to north. The smell of gold permeates the air.""", s_to_err="A solid wall of rock bars your path southwards",
                     e_to_err="There is no way to get through the stone to the east.",
                     dark="You bump into a number of stone walls, completely unable to see.",
                     items=[Gold("Gold Pieces", 'Glorious Currency', dice(1,10,2))]),

    'treasure': Room("Treasure Chamber", """You've found the long-lost treasure
chamber! Sadly, it has already been completely emptied by
earlier adventurers. The only exit is to the south.""", n_to_err="A decorated wall blocks you from going to the north.",
                     e_to_err="You look closely to the east and you find a hidden door! Oh wait.. no that's not a hidden door. Just some tiny cracks in the wall.",
                     w_to_err="The wall to the west seems to taunt you, daring you to try to go through it. "
                     "You give into the taunts and run into the wall. You remain in this room, feeling somewhat silly.",
                     items=[Gold("Gold Pieces", "Glorious Currency", dice(10,6,20))]),
}


# Link rooms together

room['outside'].n_to = room['foyer']
room['foyer'].s_to = room['outside']
room['foyer'].n_to = room['overlook']
room['foyer'].e_to = room['narrow']
room['overlook'].s_to = room['foyer']
room['narrow'].w_to = room['foyer']
room['narrow'].n_to = room['treasure']
room['treasure'].s_to = room['narrow']

#
# Main
#

# Make a new player object that is currently in the 'outside' room.
player = Player(input('What is your name, adventurer?'), room['outside'], 100, 100, 0)

# Write a loop that:
#
# * Prints the current room name
# * Prints the current description (the textwrap module might be useful here).
# * Waits for user input and decides what to do.
#
# If the user enters a cardinal direction, attempt to move to the room there.
# Print an error message if the movement isn't allowed.
#
# If the user enters "q", quit the game.
game_running = True
print(f"\n\nYou are {player.name}, an adventurer who has come to this cave seeking adventure and riches.")

current_loc = player.cur_loc
print(player.cur_loc.name)
print(player.cur_loc.desc)
while game_running:
    print()
    light_source = False
    for item in player.inventory:
        if isinstance(item, LightSource):
            light_source = True
    for item in player.cur_loc.items:
        if isinstance(item, LightSource):
            light_source = True
    if player.cur_loc.is_light or light_source:
        is_light = True
    else:
        is_light = False

    if is_light:
        if player.cur_loc != current_loc:
            print(player.cur_loc.name)
            print(player.cur_loc.desc)
        if len(player.cur_loc.items) > 0:
            for item in player.cur_loc.items:
                print(f"You see a {item.name} here!")
    else:
        if player.cur_loc != current_loc:
            print(player.cur_loc.dark)
    current_loc = player.cur_loc


    user_input = input('Action:').lower()
    user_split = user_input.split(" ", maxsplit=1)
    if len(user_split) == 1:
        if user_split[0] in ['q', 'quit']:
            print("\n\n-=Game terminated=-\n\n")
            game_running = False
        elif user_split[0] in ['n', 'north']:
            print(player.move('north', is_light))
        elif user_split[0] in ['s', 'south']:
            print(player.move('south', is_light))
        elif user_split[0] in ['e', 'east']:
            print(player.move('east', is_light))
        elif user_split[0] in ['w', 'west']:
            print(player.move('west', is_light))
        elif user_split[0] in ['u', 'up', 'd', 'down']:
            print(
                "Please purchase our Three Dimensions DLC to access this content. Free tier is restricted to two dimensions.")
        elif user_split[0] in ['i', 'inventory']:
            player.show_inventory()
        elif user_split[0] in ['l', 'look']:
            if is_light:
                print(player.cur_loc.name)
                print(player.cur_loc.desc)
            else:
                print(player.cur_loc.dark)
        else:
            print("Unknown input")
    elif len(user_split) == 2:
        if user_split[0] in ['go', 'move']:
            if user_split[1] in ['n', 'north']:
                print(player.move('north', is_light))
            elif user_split[1] in ['s', 'south']:
                print(player.move('south', is_light))
            elif user_split[1] in ['e', 'east']:
                print(player.move('east', is_light))
            elif user_split[1] in ['w', 'west']:
                print(player.move('west', is_light))
            elif user_split[1] in ['u', 'up', 'd', 'down']:
                print("Please purchase our Three Dimensions DLC to access this content. Free tier is restricted to two dimensions.")
            else:
                print("I dont know which way you want to go. Try 'north', 'south', 'east', or 'west'.")
        elif user_split[0] in ['get', 'take']:
            if is_light:
                success = False
                for item in player.cur_loc.items:
                    if user_split[1] == item.name.lower():
                        if isinstance(item, Gold):
                            player.gold += item.value
                            item.on_take()
                        else:
                            player.inventory.append(item)
                            item.on_take()
                        success = True
                        player.cur_loc.items.remove(item)
                if not success:
                    print(f"I dont see a {user_split[1]} here.")
            else:
                print("It's too dark to see anything in this room.")

        elif user_split[0] in ['drop']:
            success = False
            for item in player.inventory:
                if user_split[1] == item.name.lower():
                    player.cur_loc.items.append(item)
                    item.on_drop()
                    success = True
                    player.inventory.remove(item)
            if not success:
                print(f"You dont have a {user_split[1]}.")

    else:
        print("Can you try typing less words for me, buddy? I'm kinda dumb.")
