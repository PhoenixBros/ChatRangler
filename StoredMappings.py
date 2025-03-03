from vgamepad import XUSB_BUTTON

class xbox_valid_inputs:
    '''
    all the valid inputs for an xbox controller
    '''   
    A = {'type':"BUTTON", 'id':XUSB_BUTTON.XUSB_GAMEPAD_A}
    B = {'type':"BUTTON", 'id':XUSB_BUTTON.XUSB_GAMEPAD_B}
    X = {'type':"BUTTON", 'id':XUSB_BUTTON.XUSB_GAMEPAD_X}
    Y = {'type':"BUTTON", 'id':XUSB_BUTTON.XUSB_GAMEPAD_Y}
    
    START = {'type':"BUTTON", 'id':XUSB_BUTTON.XUSB_GAMEPAD_START}
    BACK = {'type':"BUTTON", 'id':XUSB_BUTTON.XUSB_GAMEPAD_BACK}
    GUIDE = {'type':"BUTTON", 'id':XUSB_BUTTON.XUSB_GAMEPAD_GUIDE}
    
    DPAD_UP = {'type':"BUTTON", 'id':XUSB_BUTTON.XUSB_GAMEPAD_DPAD_UP}
    DPAD_DOWN = {'type':"BUTTON", 'id':XUSB_BUTTON.XUSB_GAMEPAD_DPAD_DOWN}
    DPAD_LEFT = {'type':"BUTTON", 'id':XUSB_BUTTON.XUSB_GAMEPAD_DPAD_LEFT}
    DPAD_RIGHT = {'type':"BUTTON", 'id':XUSB_BUTTON.XUSB_GAMEPAD_DPAD_RIGHT}
    
    BUMPER_LEFT = {'type':"BUTTON", 'id':XUSB_BUTTON.XUSB_GAMEPAD_LEFT_SHOULDER}
    BUMPER_RIGHT = {'type':"BUTTON", 'id': XUSB_BUTTON.XUSB_GAMEPAD_RIGHT_SHOULDER}
    
    THUMB_LEFT = {'type':"BUTTON", 'id':XUSB_BUTTON.XUSB_GAMEPAD_LEFT_THUMB}
    THUMB_RIGHT = {'type':"BUTTON", 'id':XUSB_BUTTON.XUSB_GAMEPAD_RIGHT_THUMB}
    
    TRIGGER_LEFT = {'type':"TRIGGER", 'id':"tr left"}
    TRIGGER_RIGHT = {'type':"TRIGGER", 'id':"tr right"}
    
    STICK_LEFT_X = {'type':"STICK", 'id':"left x"}
    STICK_LEFT_Y = {'type':"STICK", 'id':"left y"}
    STICK_RIGHT_X = {'type':"STICK", 'id':"right x"}
    STICK_RIGHT_Y = {'type':"STICK", 'id':"right y"}


# conversions take the input and convert it to another type or value
# button to axis is possible and so is axis to button
# however axis to button cant destinguish -1 and +1 so both will activate the same button, inputs cant be mapped to more than one output

# common conversions
conversions = {
    "pass": lambda x : x, # types must match
    "-b" : lambda x : not x, # bool to bool
    "b -> +a": lambda x : 1.0 if x else 0.0, # bool to float
    "b -> -a": lambda x : -1.0 if x else 0.0, # bool to float
    "a -> b": lambda x : True if abs(x) > .5 else False, # float to bool
    "a -> -b": lambda x : False if abs(x) > .5 else True, # float to bool
    "-a": lambda x : -x, # float to float
    "a -> [0,1]": lambda x : (x+1)/2, # flaot to float
}

# a lookup table for legal conversions
con_type_lookup = {
    bool:{
        bool:['pass', '-b'],
        float:['b -> +a', 'b -> -a'],
    },
    float:{
        float:['pass', '-a', 'a -> [0,1]'],
        bool:['a -> b', 'a -> -b'],
    }
}

def get_avalable_conversions(t1:type, t2:type) -> list:
    if t1 in con_type_lookup.keys():
        if t2 in con_type_lookup[t1].keys():
            return con_type_lookup[t1][t2]
    

# --------------------------------------------------------------
#                    controller mapping
# --------------------------------------------------------------
# mappings have 3 types "BUTTON"s, "AXIS"s, and "HAt"s
# each mapping coresponds to a valid input id on the controller in use and a convertion to a valid xbox controller input
# thay can be blank if we dont want to map an input
# one input cannot be mapped to two outputs
# each input that gets mapped also gets its value converted
# conversions can go between types (i.e. converting dpad buttons to joystick motion)

# you can use the bottom of this page to help construct a mapping of controllers you dont have https://www.pygame.org/docs/ref/joystick.html
# you can also use the MapGenerator.py to help generate a map for a controller you have access to 

# maps are stuctured like this:
# name =  {
#   'BUTTON': {
#       id: {'input:xbox_valid_inputs, 'convert':function}
#   },
#   'AXIS': {
#       id: {'input:xbox_valid_inputs, 'convert':function}
#   },
#   'BUTTON': {
#       id: {'input:xbox_valid_inputs, 'convert':function}
#   },
#   'BUTTON': {
#       id: {'input:xbox_valid_inputs, 'convert':function}
#   },
# }


######################
# Pre built mappings

# this mapping is the defualt and wont do anything
emptymap = {'BUTTON':{},'AXiS':{},'HAT':(),}

# defualt mapping for xbox 360 controller
xbox360_map = {'BUTTON': { 0: {'input': xbox_valid_inputs.A, "convert":conversions['pass']}, 1: {'input': xbox_valid_inputs.B, "convert":conversions['pass']}, 2: {'input': xbox_valid_inputs.X, "convert":conversions['pass']}, 3: {'input': xbox_valid_inputs.Y, "convert":conversions['pass']}, 4: {'input': xbox_valid_inputs.BUMPER_LEFT, "convert":conversions['pass']}, 5: {'input': xbox_valid_inputs.BUMPER_RIGHT, "convert":conversions['pass']}, 6: {'input': xbox_valid_inputs.BACK, "convert":conversions['pass']}, 7: {'input': xbox_valid_inputs.START, "convert":conversions['pass']}, 8: {'input': xbox_valid_inputs.THUMB_LEFT, "convert":conversions['pass']},9: {'input': xbox_valid_inputs.THUMB_RIGHT, "convert":conversions['pass']},10: {'input': xbox_valid_inputs.GUIDE, "convert":conversions['pass']},},'AXIS': { 0: {'input': xbox_valid_inputs.STICK_LEFT_X, "convert":conversions['pass']}, 1: {'input': xbox_valid_inputs.STICK_LEFT_Y, "convert":conversions['pass']}, 2: {'input': xbox_valid_inputs.TRIGGER_LEFT, "convert":conversions['pass']}, 3: {'input': xbox_valid_inputs.STICK_RIGHT_X, "convert":conversions['pass']}, 4: {'input': xbox_valid_inputs.STICK_RIGHT_Y, "convert":conversions['pass']}, 5: {'input': xbox_valid_inputs.TRIGGER_RIGHT, "convert":conversions['pass']},}, 'HAT': { 11: {'input': xbox_valid_inputs.DPAD_UP, "convert":conversions['pass']}, 12: {'input': xbox_valid_inputs.DPAD_DOWN, "convert":conversions['pass']}, 13: {'input': xbox_valid_inputs.DPAD_LEFT, "convert":conversions['pass']}, 14: {'input': xbox_valid_inputs.DPAD_RIGHT, "convert":conversions['pass']},}}

# defualt mapping for ps4 controller
ps4_map = {'BUTTON': { 0: {'input': xbox_valid_inputs.A, "convert":conversions['pass']}, 1: {'input': xbox_valid_inputs.B, "convert":conversions['pass']}, 2: {'input': xbox_valid_inputs.X, "convert":conversions['pass']}, 3: {'input': xbox_valid_inputs.Y, "convert":conversions['pass']}, 6: {'input': xbox_valid_inputs.START, "convert":conversions['pass']}, 5: {'input': xbox_valid_inputs.GUIDE, "convert":conversions['pass']}, 4: {'input': xbox_valid_inputs.BACK, "convert":conversions['pass']}, 11: {'input': xbox_valid_inputs.DPAD_UP, "convert":conversions['pass']}, 12: {'input': xbox_valid_inputs.DPAD_DOWN, "convert":conversions['pass']}, 13: {'input': xbox_valid_inputs.DPAD_LEFT, "convert":conversions['pass']}, 14: {'input': xbox_valid_inputs.DPAD_RIGHT, "convert":conversions['pass']}, 15: {'input': xbox_valid_inputs.BACK, "convert":conversions['pass']}, 9: {'input': xbox_valid_inputs.BUMPER_LEFT, "convert":conversions['pass']}, 10: {'input': xbox_valid_inputs.BUMPER_RIGHT, "convert":conversions['pass']}, 7: {'input': xbox_valid_inputs.THUMB_LEFT, "convert":conversions['pass']}, 8: {'input': xbox_valid_inputs.THUMB_RIGHT, "convert":conversions['pass']}},'AXIS': { 0: {'input': xbox_valid_inputs.STICK_LEFT_X, "convert":conversions['pass']}, 1: {'input': xbox_valid_inputs.STICK_LEFT_Y, "convert":conversions['-a']}, 2: {'input': xbox_valid_inputs.STICK_RIGHT_X, "convert":conversions['pass']}, 3: {'input': xbox_valid_inputs.STICK_RIGHT_Y, "convert":conversions['-a']}, 4: {'input': xbox_valid_inputs.TRIGGER_LEFT, "convert":conversions['pass']},5: {'input': xbox_valid_inputs.TRIGGER_RIGHT, "convert":conversions['pass']}},}

######################
# custom built mappings
# feel free to write your own mappings here

######################
# MapGenerator created mappings
#!IMPORTANT: DO NOT DELETE THIS LINE |~>


# make sure to keep all map names lowercase
controller_mappings = {
    # pre built mappings
    "none":emptymap, 
    "xbox 360 controller":xbox360_map, 
    "ps4 controller":ps4_map,
    
    # custom built mappings
    
    # MapGenerator mappings
    #!IMPORTANT: DO NOT DELETE THIS LINE |~>
    
}
