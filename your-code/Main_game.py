# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import pygame
import random
import time
from pygame import mixer

pygame.init()



# define rooms and items

couch = {
    "name": "couch",
    "type": "furniture",
}

door_a = {
    "name": "door a",
    "type": "door",
}

key_a = {
    "name": "key for door a",
    "type": "key",
    "target": door_a,
}

piano = {
    "name": "piano",
    "type": "furniture",
}

game_room = {
    "name": "game room",
    "type": "room",
}

vaultdoor = {
    "name": "vaultdoor",
    "type": "door",
}

# outside = {
#   "name": "outside"
# }

#bedroom1
bedroom1 = {
    "name": "bedroom1",
    "type": "room",
}

queenbed = {
    "name": "queenbed",
    "type": "furniture",
}

door_b = {
    "name": "door b",
    "type": "door",
}

key_b = {
    "name": "key for door b",
    "type": "key",
    "target": door_b,
}

door_c = {
    "name": "door c",
    "type": "door",
}

#bedroom2
bedroom2 = {
    "name": "bedroom2",
    "type": "room",
}

doublebed = {
    "name": "doublebed",
    "type": "furniture",
}


key_c = {
    "name": "key for door c",
    "type": "key",
    "target": door_c,
}

dresser = {
    "name": "dresser",
    "type": "furniture",
}

vaultkey = {
    "name": "key for vaultdoor",
    "type": "key",
    "target": vaultdoor,
}

#livingroom

livingroom = {
    "name": "livingroom",
    "type": "room",
}

diningtable = {
    "name": "diningtable",
    "type": "furniture",
}

door_d = {
    "name": "door d",
    "type": "door",
}

outside = {
    "name": "outside",
    "type": "room",
}

#Vault Room

vaultroom = {
    "name": "vaultroom",
    "type": "room",
}

vaultdoor = {
    "name": "vaultdoor",
    "type": "door",
}

vault = {
    "name": "vault",
    "type": "furniture",
}

key_d = {
    "name": "key for door d",
    "type": "key",
    "target": door_d,
}


all_rooms = [game_room, outside, bedroom1, bedroom2, livingroom, vaultroom]

all_doors = [door_a, door_b, door_c, door_d, vaultdoor]

# define which items/rooms are related

object_relations = {
    "game room": [couch, piano, door_a, vaultdoor],
    "piano": [key_a],
    "outside": [door_d],
    "door a": [game_room, bedroom1],
    "bedroom1": [queenbed, door_c, door_b, door_a],
    "queenbed" : [key_b],
    "door d" : [outside, livingroom],
    "bedroom2": [doublebed, dresser, door_b],
    "livingroom": [diningtable, door_c, door_d],
    "door b": [bedroom2, bedroom1],
    "door c": [bedroom1, livingroom],
    "dresser": [vaultkey],
    "doublebed": [key_c],
    "vault": [key_d],
    "vaultroom": [vault, vaultdoor],
    "vaultdoor": [game_room, vaultroom],
}

# define game state. Do not directly change this dict. 
# Instead, when a new game starts, make a copy of this
# dict and use the copy to store gameplay state. This 
# way you can replay the game multiple times.

INIT_GAME_STATE = {
    "current_room": game_room,
    "keys_collected": [],
    "target_room": outside
}


############################# FUNCTIONS #############################

def linebreak():
    """
    Print a line break
    """
    print("\n\n")

def start_game():
    """
    Start the game
    """
    print('\n')
    print('\n')
    print('\n')
    print('\n')
    print('\n')
    print('\n')
    print('\n')
    print('\n')
    print('ESCAPE ROOM: THE JOURNEY!')
    print('\n')
    print("You wake up on a couch and find yourself in a strange house with no windows which you have never been to before. You don't remember why you are here and what had happened before. You feel some unknown danger is approaching and you must get out of the house, NOW!")
    print("There's a map somewhere! Search for it! ")
    print('\n')
    print('\n')
    print('\n')
    print('\n')
   
    play_room(game_state["current_room"])

def play_room(room):
    """
    Play a room. First check if the room being played is the target room.
    If it is, the game will end with success. Otherwise, let player either 
    explore (list all items in this room) or examine an item found here.
    """
    game_state["current_room"] = room
    if(game_state["current_room"] == game_state["target_room"]):
        music = r"C:\Users\PC\Desktop\Projects\Week1\python-project\Sound\Friday.wav"
        pygame.mixer.music.load(music)
        pygame.mixer.music.play()
        imshow('escaperoom.jpg')
        time.sleep(5)
        imclose()
       
    else:
        print("You are now in " + room["name"])
        intended_action = input("What would you like to do? Type 'explore' or 'examine'?").strip().lower()
        if intended_action == "explore":
            explore_room(room)
            play_room(room)
        elif intended_action == "examine":
            examine_item(input("What would you like to examine?").strip().lower())
        else:
            print("Not sure what you mean. Type 'explore' or 'examine'.")
            play_room(room)
        linebreak()

def explore_room(room):
    """
    Explore a room. List all items belonging to this room.
    """
    items = [i["name"] for i in object_relations[room["name"]]]
    print("You explore the room. This is " + room["name"] + ". You find " + ", ".join(items))

def get_next_room_of_door(door, current_room):
    """
    From object_relations, find the two rooms connected to the given door.
    Return the room that is not the current_room.
    """
    connected_rooms = object_relations[door["name"]]
    for room in connected_rooms:
        if(not current_room == room):
            return room

 ################################################# GAME HEADS & TAILS #################################################      
def heads_or_tails():
    state=True
    while state :
        score = random.random()
        answer = input("Let's play a game! If you win you open the vault! Heads or Tails?")
        if answer.lower() == 'heads' or answer.lower()=='tails':
            if score>0.5:
                response = "You lost! Try again!"
            else:
                response = "You opened the vault!"
                state=False
            print(response)
        else:
            print('You have to choose Heads or Tails!')
    return response
    
 ################################################# GAME HEADS & TAILS #################################################     

 ################################################# MAPA #################################################    

def imshow(filename):
    #pygame.init()
    img = pygame.image.load(filename)
    size = img.get_rect().size
    screen = pygame.display.set_mode(size)
    screen.blit(img, (0, 0))
    pygame.display.flip()
    #pygame.event.clear()
def imclose():
    #pygame.quit()
    pygame.display.quit()

 ################################################# MAPA #################################################    

def examine_item(item_name):
    """
    Examine an item which can be a door or furniture.
    First make sure the intended item belongs to the current room.
    Then check if the item is a door. Tell player if key hasn't been 
    collected yet. Otherwise ask player if they want to go to the next
    room. If the item is not a door, then check if it contains keys.
    Collect the key if found and update the game state. At the end,
    play either the current or the next room depending on the game state
    to keep playing.
    """
    current_room = game_state["current_room"]
    next_room = ""
    output = None
    
    for item in object_relations[current_room["name"]]:
        if(item["name"] == item_name):
            output = "You examine " + item_name + ". "
            if(item["type"] == "door"):
                have_key = False
                for key in game_state["keys_collected"]:
                    if(key["target"] == item):
                        have_key = True
                if(have_key):
                    output += "You unlock it with a key you have."
                    next_room = get_next_room_of_door(item, current_room)
                else:
                    output += "It is locked but you don't have the key."
                    music = r"C:\Users\PC\Desktop\Projects\Week1\python-project\Sound\locked_door.wav"
                    pygame.mixer.music.load(music)
                    pygame.mixer.music.play()
            elif (item['name'] == 'vault'):
                    heads_or_tails()
                    if(item["name"] in object_relations and len(object_relations[item["name"]])>0):
                        item_found = object_relations[item["name"]].pop()
                        game_state["keys_collected"].append(item_found)
                        output += "You find " + item_found["name"] + "."
                
                
            else:
                if(item["name"] == 'couch'):
                    print('YOU FOUND THE MAP!!')
                    print("The map is attached to the couch, you can't take it you!")
                    imshow('Vault Room.jpg')
                    time.sleep(10)
                    imclose()
                elif(item["name"] in object_relations and len(object_relations[item["name"]])>0):
                    item_found = object_relations[item["name"]].pop()
                    game_state["keys_collected"].append(item_found)
                    output += "You find " + item_found["name"] + "."
                else:
                    output += "There isn't anything interesting about it."
            print(output)
            break

    if(output is None):
        print("The item you requested is not found in the current room.")
    
    if(next_room and input("Do you want to go to the next room? Enter 'yes' or 'no'").strip().lower() == 'yes'):
        music = r"C:\Users\PC\Desktop\Projects\Week1\python-project\Sound\door_opening.wav"
        pygame.mixer.music.load(music)
        pygame.mixer.music.play()
        play_room(next_room)

    else:
        play_room(current_room)
        
        
####################################### START GAME / LOOP ###############################


game_state = INIT_GAME_STATE.copy()
playAgain = "yes"
while playAgain.lower() == "yes":
    game_state = INIT_GAME_STATE.copy()
    
    object_relations = {
    "game room": [couch, piano, door_a, vaultdoor],
    "piano": [key_a],
    "outside": [door_d],
    "door a": [game_room, bedroom1],
    "bedroom1": [queenbed, door_c, door_b, door_a],
    "queenbed" : [key_b],
    "door d" : [outside, livingroom],
    "bedroom2": [doublebed, dresser, door_b],
    "livingroom": [diningtable, door_c, door_d],
    "door b": [bedroom2, bedroom1],
    "door c": [bedroom1, livingroom],
    "dresser": [vaultkey],
    "doublebed": [key_c],
    "vault": [key_d],
    "vaultroom": [vault, vaultdoor],
    "vaultdoor": [game_room, vaultroom],
}
    
    INIT_GAME_STATE = {
    "current_room": game_room,
    "keys_collected": [],
    "target_room": outside
}

    start_game()
    playAgain = input("Do you want to play again?: ")
    
    