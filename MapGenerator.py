from StoredMappings import get_avalable_conversions
import pygame as pg
import time
from copy import deepcopy
pg.init()


xbox_options = {
    'a': ["~xbox_valid_inputs.A~", bool],
    'b': ["~xbox_valid_inputs.B~", bool],
    'x': ["~xbox_valid_inputs.X~", bool],
    'y': ["~xbox_valid_inputs.Y~", bool],
    'back': ["~xbox_valid_inputs.BACK~", bool],
    'start': ["~xbox_valid_inputs.START~", bool],
    'guide': ["~xbox_valid_inputs.GUIDE~", bool],
    'dpad u': ["~xbox_valid_inputs.DPAD_UP~", bool],
    'dpad d': ["~xbox_valid_inputs.DPAD_DOWN~", bool],
    'dpad l': ["~xbox_valid_inputs.DPAD_LEFT~", bool],
    'dpad r': ["~xbox_valid_inputs.DPAD_RIGHT~", bool],
    'l bumper': ["~xbox_valid_inputs.BUMPER_LEFT~", bool],
    'r bumper': ["~xbox_valid_inputs.BUMPER_RIGHT~", bool],
    'l thumb': ["~xbox_valid_inputs.THUMB_LEFT~", bool],
    'r thumb': ["~xbox_valid_inputs.THUMB_RIGHT~", bool],
    
    'l stick x': ["~xbox_valid_inputs.STICK_LEFT_X~", float],
    'l stick y': ["~xbox_valid_inputs.STICK_LEFT_Y~", float],
    'r stick x': ["~xbox_valid_inputs.STICK_RIGHT_X~", float],
    'r stick y': ["~xbox_valid_inputs.STICK_RIGHT_Y~", float],
    'l trigger': ["~xbox_valid_inputs.TRIGGER_LEFT~", float],
    'r trigger': ["~xbox_valid_inputs.TRIGGER_RIGHT~", float],
}


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

WIP_map_inputs = {
    'BUTTON':{i:None for i in range(joyce.get_numbuttons())},
    'AXIS':{i:None for i in range(joyce.get_numaxes())},
    'HAT':{i:None for i in range(joyce.get_numhats())},
    'BALL':{i:None for i in range(joyce.get_numballs())},
}

print("list of this controllers inputs:\n",WIP_map_inputs)

answer = input("would you like to map the controller or test its inputs (map / test)")


if answer == "map":
    print("please press a button or move a stick on the controller you selected")

    current_selection = None
    answer = ""
    while answer != "done":
        answer = ""
        for event in pg.event.get():
            if event.type == pg.JOYBUTTONDOWN and event.instance_id == joyce.get_instance_id():
                current_selection = ["BUTTON", event.button, bool]
            elif event.type == pg.JOYAXISMOTION and event.instance_id == joyce.get_instance_id():
                if abs(event.value) > .5:
                    current_selection = ["AXIS", event.axis, float]
            elif event.type == pg.JOYHATMOTION and event.instance_id == joyce.get_instance_id():
                print(event)
                current_selection = ["HAT", event.hat, float]
            elif event.type == pg.JOYBALLMOTION and event.instance_id == joyce.get_instance_id():
                print(event)
                current_selection = ["BALL", event.value, float] # i dont have access to a ball type input so figure its out yourself
                
        if current_selection != None:
            print("please type the input you would like to map", current_selection, "to\n avalable options are:", list(xbox_options.keys()))
            while answer not in xbox_options.keys():
                answer = input("> ")
            xboxkey = xbox_options[answer]
            
            answer = ''
            print("choose a convertion: ", get_avalable_conversions(current_selection[2], xboxkey[1]))
            while answer not in get_avalable_conversions(current_selection[2], xboxkey[1]):
                answer = input('> ')
                
            WIP_map_inputs[current_selection[0]][current_selection[1]] = {'input':xboxkey[0], 'convert':f"~conversions['{answer}']~"}
            
            print("current input map:", WIP_map_inputs)
            answer = input("\nwould you like to keep mapping? if not type 'done'\n> ")

            current_selection = None
            for event in pg.event.get(): pass # ignore all the inputs pressed while sellecting mapping
            if answer != "done":
                print("press any button on your controller now")


    input_guide = deepcopy(WIP_map_inputs)
    #removes all controllers non set inputs
    for key in input_guide.keys():
        for index in input_guide[key].keys():
            if input_guide[key][index] == None:
                WIP_map_inputs[key].pop(index)
                
    #convert to copyable string and remove all incorrect quotes    
    new_mapping = str(WIP_map_inputs)

    search = new_mapping.split('~')
    for splits in range(len(search))[1::2]:
        search[splits-1] = search[splits-1][:-1]
        search[splits+1] = search[splits+1][1:]
    new_mapping = "".join(search)

    answer = ' '
    while (answer[0].isdigit() or not answer.replace('_', '').isalnum()):
        answer = input("please add a name for the mapping\nthe name can only contain alpha numerical charactors and '_'. all numbers must come after the first charactor\n>")
        
    # combine to creat the mapping line
    new_mapping = answer + " = " + new_mapping

    print("\n\n", new_mapping, "\n\n this is the mapping you created, feel free to copy this into input mappings manually or ")

    # inserts the new mapping into the python file
    do_auto_insert = input("\ntype \"yes\" if you would you like to have this map automatically added to the existing input mappings\n> ")
    if do_auto_insert == "yes":
        import os
        file_location = os.getcwd()+"\\StoredMappings.py"
        # make sure this is run form inside the chatrangler directory
        
        # get the current file contents
        with open(file_location, 'r') as input_mapping_file:
            file_contents = input_mapping_file.read()
            input_mapping_file.close()
        file_contents = file_contents.split("|~>") # find the insertion points
        
        # insert the new map
        file_contents.insert(2, f"|~>\n    \"{answer.replace('_', ' ')}\":{answer},")
        file_contents.insert(1, f"|~>\n{new_mapping}")
            
        # save the file
        with open(file_location, 'w') as input_mapping_file:
            input_mapping_file.write("".join(file_contents))
            input_mapping_file.close()
else:
    while True:
        for event in pg.event.get():
            if event.type == pg.JOYBUTTONDOWN:
                print(event)
            elif event.type == pg.JOYAXISMOTION:
                if abs(event.value) > .5:
                    print(event)
            elif event.type == pg.JOYHATMOTION:
                print(event)
            elif event.type == pg.JOYBALLMOTION:
                print(event)