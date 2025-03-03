from InputMapping import xbox_valid_inputs as xbox
from InputMapping import conversions
import pygame as pg
import time
pg.init()

joyce = None
joysticks = []
for event in pg.event.get():
    if event.type == pg.JOYDEVICEADDED:
        joy = pg.joystick.Joystick(event.device_index)
        joysticks.append(joy)
        
        
print("please type index of the joystick you wish to map from the list below")
indexed_joys = {i:joysticks[i].get_name() for i in range(len(joysticks))}
print(indexed_joys)
answer = ""
while not answer.isdigit() or not (int(answer) in indexed_joys.keys()):
    answer = input(">")

joyce = joysticks[int(answer)]

unmapped_inputs = {
    'BUTTON':{i:None for i in range(joyce.get_numbuttons())},
    'AXIS':{i:None for i in range(joyce.get_numaxes())},
    'HAT':{i:None for i in range(joyce.get_numhats())},
    'BALL':{i:None for i in range(joyce.get_numballs())},
}

print("list of this controllers inputs:\n",unmapped_inputs)


print("please press a button or move a stick on the controller you selected")

xbox_options = {
    'a': xbox.A,
    'b': xbox.B,
    'x': xbox.X,
    'y': xbox.Y,
    'back': xbox.BACK,
    'start': xbox.START,
    'guide': xbox.GUIDE,
    'dpad u': xbox.DPAD_UP,
    'dpad d': xbox.DPAD_DOWN,
    'dpad l': xbox.DPAD_LEFT,
    'dpad r': xbox.DPAD_RIGHT,
    'l bumper': xbox.BUMPER_LEFT,
    'r bumper': xbox.BUMPER_RIGHT,
    'l thumb': xbox.THUMB_LEFT,
    'r thumb': xbox.THUMB_RIGHT,
    
    'l stick x': xbox.STICK_LEFT_X,
    'l stick y': xbox.STICK_LEFT_Y,
    'r stick x': xbox.STICK_RIGHT_X,
    'r stick y': xbox.STICK_RIGHT_Y,
    'l trigger': xbox.TRIGGER_LEFT,
    'r trigger': xbox.TRIGGER_RIGHT,
}
current_selection = None
answer = ""
while answer != "quit":
    answer = ""
    for event in pg.event.get():
        if event.type == pg.JOYBUTTONDOWN:
            current_selection = ["BUTTON", event.button, bool]
        elif event.type == pg.JOYAXISMOTION:
            if abs(event.value) > .5:
                current_selection = ["AXIS", event.axis, float]
        elif event.type == pg.JOYHATMOTION:
            print(event)
            current_selection = ["HAT", event.hat, ]
        elif event.type == pg.JOYBALLMOTION:
            print(event)
            current_selection = ["BALL", event.value] # i dont have access to a ball type input so this is based on the documentation and has not been tested
            
    if current_selection != None:
        print("please type the input you would like to map", current_selection, "to\n avalable options are:", list(xbox_options.keys()))
        while answer not in xbox_options.keys():
            answer = input("> ")
        xboxkey = xbox_options[answer]
        
        answer = ''
        print("choose a convertion: ", list(conversions.keys()))
        while answer not in conversions.keys():
            answer = input('> ')
            
        unmapped_inputs[current_selection[0]][5] = {'input':xboxkey, 'convert':conversions[answer]}
        print("current input map:", unmapped_inputs)
        answer = input("would you like to keep mapping? if not type quit\n> ")
        